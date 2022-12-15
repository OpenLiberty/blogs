# Copyright (c) 2022 IBM Corporation and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     IBM Corporation - initial API and implementation

import sys
import requests
import json
import re
import os

BETA_TEMPLATE_URL = 'https://raw.githubusercontent.com/OpenLiberty/blogs/prod/templates/beta-release-post.adoc'
GA_TEMPLATE_URL = 'https://raw.githubusercontent.com/OpenLiberty/blogs/prod/templates/ga-release-post.adoc'

BETA_TOC_SECTION = '''* <<SUB_TAG_1, SUB_FEATURE_TITLE>>
* <<SUB_TAG_2, SUB_FEATURE_TITLE>>
* <<SUB_TAG_3, SUB_FEATURE_TITLE>>'''

GA_TOC_SECTION = '''* <<TAG_1, FEATURE_1_HEADING>>
* <<TAG_2, FEATURE_2_HEADING>>
** <<SUB_TAG_1, SUB_FEATURE_1_HEADING>>
** <<SUB_TAG_2, SUB_FEATURE_2_HEADING>>
* <<TAG_3, FEATURE_3_HEADING>>'''

BETA_CONTENT_SECTION = '''[#SUB_TAG_1]
=== SUB_FEATURE_TITLE

// // // // // // // //
// FURTHER EXPLANATION OF THIS FEATURE/FUNCTION
// // // // // // // //



[source, java]
----
// // // // // // // //
// EXAMPLE CODE
// // // // // // // //
----'''

BLOG_ISSUE_URL_PLACEHOLDER = "BLOG_ISSUE_URL_PLACEHOLDER"
BLOG_CONTACT_PLACEHOLDER = "BLOG_CONTACT_PLACEHOLDER"
BLOG_ISSUE_SECTION_START = f"// // // // DO NOT MODIFY THIS COMMENT BLOCK <GHA-BLOG-TOPIC> // // // // \n// Blog issue: {BLOG_ISSUE_URL_PLACEHOLDER}\n// Contact/Reviewer: {BLOG_CONTACT_PLACEHOLDER}\n// // // // // // // //"
BLOG_ISSUE_SECTION_END = '// DO NOT MODIFY THIS LINE. </GHA-BLOG-TOPIC> '

people = set()

def get_linked_issue(body):
    result = re.search(r'See (?:the )?Beta blog issue.+?(\d+)', body, re.IGNORECASE)
    if result:
        response = json.loads(requests.get(f'https://api.github.com/repos/OpenLiberty/open-liberty/issues/{result.group(1)}').text)
        print("Found linked beta issue: " + response["html_url"])
        return response
    return None

def find_previous_posts(issue_url):
    # Iterate through beta posts looking for the same blog issue
    print("Scanning beta blog posts for issue: " + issue_url)
    posts = ""
    dir = 'posts'
    
    thingToFind = BLOG_ISSUE_SECTION_START.partition("// Contact/Reviewer: ")[0].replace(BLOG_ISSUE_URL_PLACEHOLDER, issue_url)

    for filename in os.listdir(dir):
        file = os.path.join(dir, filename)
        if filename.endswith('-beta.adoc') and os.path.isfile(file):
            with open(file, 'r') as file:
                post = file.read()
                start = post.find(thingToFind)
                if start != -1:
                    start += len(thingToFind)
                    end = post.find(BLOG_ISSUE_SECTION_END, start)
                    excerpt = ""
                    if end != -1:
                        excerpt = post[start:end]
                        print('Found excerpt in beta blog ' + filename)
                    else:
                        excerpt = f"// The issue {issue_url} was found in {file}, however, no closing tag was found.  You must manually pull in the content."
                    posts += f'// The following excerpt for issue {issue_url} was found in {filename}.\n// ------ <Excerpt From Previous Post: Start> ------\n{excerpt}\n// ------ <Excerpt From Previous Post: End> ------ \n'
    return posts

def make_blog(issues, is_beta):
    titles = []
    contents = []
    prefix = "BETA BLOG - " if is_beta else "GA BLOG - "

    for i, issue in enumerate(issues):
        print("\nProcessing Issue: " + issue["html_url"])
        people.add(issue['user']['login'])
        people.update([assignee['login'] for assignee in issue['assignees']])
        reviewers = set()
        reviewers.add(issue['user']['login'])
        reviewers.update([assignee['login'] for assignee in issue['assignees']])
        reviewers_string = ','.join(reviewers)
        print("Reviewers for " + issue["html_url"] + ": " + reviewers_string)
        
        closed_issue_warning = '\n// WARNING: THIS ISSUE IS CLOSED! VERIFY IF IT SHOULD BE INCLUDED IN BLOG!' if issue['state'] == 'closed' else ''

        previous_posts = ""
        linked_issue = get_linked_issue(issue['body'])
        # Try to find corresponding beta issue.  First use the new GHA tags, otherwise try and find embedded link.
        if not is_beta:
            beta_issue_link = issue['body'].partition("<GHA-BLOG-BETA-LINK>")[2].partition("</GHA-BLOG-BETA-LINK>")[0]
            print("Beta issue URL from TAG: " + beta_issue_link)
            
            if beta_issue_link == "" and linked_issue != None:
                beta_issue_link = linked_issue["html_url"]

            if beta_issue_link != "":
                previous_posts = find_previous_posts(beta_issue_link)
            else:
                print('Could not find any corresponding beta issue to scan previous posts for when processing the GA issue: ' + issue["html_url"])
                            
        title = issue["title"].replace(prefix, "").strip()
        
        # Get the issue body.  First look for tags, then for linked issues, and finally the issue itself
        body = ""
        # For now, just be greedy and grab everything between "<GHA-BLOG-RELATED-FEATURES>" and "</GHA-BLOG-SUMMARY>"
        if "<GHA-BLOG-RELATED-FEATURES>" in issue['body'] and "</GHA-BLOG-SUMMARY>" in issue['body'] :
            body = issue['body'].partition("<GHA-BLOG-RELATED-FEATURES>")[2].partition("</GHA-BLOG-SUMMARY>")[0]
        else:
            body = linked_issue['body'] if (linked_issue != None and linked_issue['body']) else issue['body']
            # find the content of blog for old template formats
            if ("Please provide the following information the week before the GA/beta date (to allow for review and publishing):" in body):
                body = body.partition("Please provide the following information the week before the GA/beta date (to allow for review and publishing):")[2]
            elif ("Please provide the following information the week before the GA date (to allow for review and publishing):" in body):
                body = body.partition("Please provide the following information the week before the GA date (to allow for review and publishing):")[2]

            if "If you have previously provided this information for an Open Liberty beta blog post and nothing has changed since the beta, just provide a link to the published beta blog post and we'll take the information from there." in body:
                body = body.partition("If you have previously provided this information for an Open Liberty beta blog post and nothing has changed since the beta, just provide a link to the published beta blog post and we'll take the information from there.")[0]
            else: 
                body = body.partition("## What happens next?")[0]
            if body == "":
                body = issue['body']

        titles.append(f'* <<SUB_TAG_{i}, {title}>>') # TODO: get/make meaningful tags
        blogSection = BLOG_ISSUE_SECTION_START.replace(BLOG_ISSUE_URL_PLACEHOLDER, issue["html_url"]).replace(BLOG_CONTACT_PLACEHOLDER, reviewers_string)
        contents.append(f'{blogSection} {closed_issue_warning}\n[#SUB_TAG_{i}]\n== {title}\n{previous_posts}{body}\n{BLOG_ISSUE_SECTION_END}\n')
        # contents.append(f'{BLOG_ISSUE_SECTION_START} {issue["html_url"]}{closed_issue_warning}\n[#SUB_TAG_{i}]\n== {title}\n{previous_posts}{body}\n{BLOG_ISSUE_SECTION_END}\n')

    return '\n'.join(titles), '\n'.join(contents)

def convert_markdown_links_to_asciidoc(content):
    # May need to expend support beyond just inline links without titles
    inline_links_regex = re.compile(r'\[(?P<text>.+?)\]\((?P<url>.+?)\)')
    
    return inline_links_regex.sub(r'link:\2[\1]', content)


def main():
    arg_count = len(sys.argv) - 1
    if arg_count != 4:
        print("Expecting 4 arguments (version number, data of publish, author name, GitHub username), most likely you didn't put quotes around the name. Check the GitHub action.", file=sys.stderr)
        exit(1);

    version = sys.argv[1]
    version_no_dots = version.replace('.', '');
    is_beta = version_no_dots.endswith('beta')
    publish_date = sys.argv[2]
    author_name = sys.argv[3]
    github_username = sys.argv[4]

    BLOG_ISSUE_URL = f"https://api.github.com/repos/OpenLiberty/open-liberty/issues?labels=blog,target:{version_no_dots};state=all"

    issues = json.loads(requests.get(BLOG_ISSUE_URL).text)
    toc, content = make_blog(issues, is_beta)

    content = convert_markdown_links_to_asciidoc(content)

    template = requests.get(BETA_TEMPLATE_URL if is_beta else GA_TEMPLATE_URL).text;

    if is_beta:
        template = template.replace(BETA_TOC_SECTION, toc) \
                           .replace(BETA_CONTENT_SECTION, content)
    else:
        # generate fixed bugs section
        BUG_ANCHOR = 'full list of bugs fixed in RELEASE_VERSION].'
        BUG_ISSUE_URL = f"https://api.github.com/repos/OpenLiberty/open-liberty/issues?labels=release%20bug,release:{version_no_dots};state=all"
        bug_desc_regex = re.compile(r'\*\*Describe the bug\*\*  \r\n(.*)\r\n\*\*Steps to Reproduce\*\*', re.DOTALL);
        bug_issues = json.loads(requests.get(BUG_ISSUE_URL).text)
        bugs = []
        for issue in bug_issues:
            res = bug_desc_regex.match(issue['body'])
            bug_title = issue["title"].replace(']', '\\]') # escape ]
            bug_desc = res.group(1).replace("\r\n\r\n", "\n+\n") if res else "" # add + to keep indentation
            bugs.append(f'* link:{issue["html_url"]}[{bug_title}]\n+\n{bug_desc}')

        template = template.replace(GA_TOC_SECTION, toc) \
                           .replace('RELEASE_VERSION_NO_PERIODS', version_no_dots) \
                           .replace(BUG_ANCHOR, '{}\n\n{}'.format(BUG_ANCHOR, "\n".join(bugs))) # fixed bugs
        # put feature content
        template = re.sub(r'\[#TAG_1\].*//Add the introduction to the feature and description here', content, template, flags=re.DOTALL)

    template = template.replace("RELEASE_VERSION", version) \
                       .replace('AUTHOR_NAME', author_name) \
                       .replace('GITHUB_USERNAME', github_username)
    filename = f"{publish_date}-{version}.adoc"
    with open(f"posts/{filename}", "w") as fp:
        fp.write(template)
    print('::set-output name=reviewers::' + ','.join(sorted(list(people))))

if __name__ == "__main__":
    main()
