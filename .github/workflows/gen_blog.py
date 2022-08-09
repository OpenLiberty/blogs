import sys
import requests
import json
import re

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

people = set()

def get_linked_issue(body):
    result = re.search(r'See (?:the )?Beta blog issue.+?(\d+)', body, re.IGNORECASE)
    if result:
        return json.loads(requests.get(f'https://api.github.com/repos/OpenLiberty/open-liberty/issues/{result.group(1)}').text)['body']
    return None

def make_blog(issues, is_beta):
    titles = []
    contents = []
    prefix = "BETA BLOG - " if is_beta else "GA BLOG - "

    for i, issue in enumerate(issues):
        people.add(issue['user']['login'])
        people.update([assignee['login'] for assignee in issue['assignees']])
        title = issue["title"].replace(prefix, "")
        body = get_linked_issue(issue['body']) or issue['body']
        closed_issue_warning = ' - WARNING: CLOSED ISSUE! VERIFY IF IT SHOULD BE INCLUDED IN BLOG!' if issue['state'] == 'closed' else ''

        # TODO: add markers in templates so it's easier to locate and less easier to break when template gets updated
        # find the content of blog
        splitted = body.split(r'Write a paragraph to summarise the update, including the following points:')
        # There's a typo in old templates so we have to try both
        if len(splitted) < 2:
            splitted = body.split(r'Write a paragraph to summarises the update, including the following points:')

        if len(splitted) >= 2:
            body = splitted[1].split("## What happens next?")[0].replace('- A sentence or two that introduces the update to someone new to the general technology/concept.\r\n\r\n   - What was the problem before and how does your update make their life better? (Why should they care?)\r\n   \r\n   - Briefly explain how to make your update work. Include screenshots, diagrams, and/or code snippets, and provide a `server.xml` snippet.\r\n   \r\n   - Where can they find out more about this specific update (eg Open Liberty docs, Javadoc) and/or the wider technology?\r\n', '');
        else:
            body = "Could not locate the summary."

        titles.append(f'* <<SUB_TAG_{i}, {title}>>') # TODO: get/make meaningful tags
        contents.append(f'// {issue["html_url"]}{closed_issue_warning}\n[#SUB_TAG_{i}]\n== {title}\n{body}')

    return '\n'.join(titles), '\n'.join(contents)

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
    # print(issues)
    toc, content = make_blog(issues, is_beta)

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
                           .replace('RELEASE_VERSION_NO_PERIOD', version_no_dots) \
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
