# Copyright (c) 2022 IBM Corporation and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     IBM Corporation - initial API and implementation

import requests
import json
import os
from argparse import ArgumentParser

message = {
    "attachments": [
        {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Release Blog Post"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*Version:*\n "
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Publish Date:*\n 2050-01-01"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*Author:*\n "
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*GitHub Username:*\n "
                        }
                    ]
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": "*PR:* <fakeLink.toEmployeeProfile.com| #pr_number>"
                        },
                        {
                            "type": "mrkdwn",
                            "text": "*<fakeLink.toEmployeeProfile.com| Preview Draft Post>*"
                        }
                    ]
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*Corresponding Blog Issues:*"
                    }
                }
            ]
        }
    ]
}

headers = {
    'Content-Type': 'application/json'
}

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('version', type=str)
    parser.add_argument('publish_date', type=str)
    parser.add_argument('author', type=str)
    parser.add_argument('github_username', type=str)
    parser.add_argument('slack_notification', type=str)
    parser.add_argument('slackhook', type=str)
    parser.add_argument('slackhook_test', type=str)
    parser.add_argument('pr_url', type=str)
    parser.add_argument('pr_branch', type=str)
    parser.add_argument('url', type=str)
    args = parser.parse_args()

    if "off" == args.slack_notification.lower():
        quit()

    # If publish_date, author, and github_username are missing, retrieve them from draft blog
    if args.version != "" and args.publish_date == "" and args.author == "" and args.github_username == "":
        args.publish_date = "Not Found"
        args.author = "Not Found"
        args.github_username = "Not Found"
        posts = ""
        dir = 'posts'
        for filename in os.listdir(dir):
            file = os.path.join(dir, filename)
            if filename.endswith('-' + args.version + '.adoc') and os.path.isfile(file):
                print("Found file: " + filename)
                args.publish_date = filename.partition('-' + args.version + '.adoc')[0]
                print("Publish date: " + args.publish_date)
                with open(file, 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if line.find("author_github: https://github.com/") != -1:
                            args.github_username = line.partition("author_github: https://github.com/")[2].strip()
                            print("GH Username: " + args.github_username)
                        if line.endswith(" <https://github.com/" + args.github_username + ">\n"):
                            args.author = line.partition(" <https://github.com/" + args.github_username + ">\n")[0]
                            print("Author: " + args.author)
                break

    if "beta" in args.version.lower():
        message["attachments"][0]["blocks"][0]["text"]["text"] = "Beta Release Blog Post"
    else:
        message["attachments"][0]["blocks"][0]["text"]["text"] = "GA Release Blog Post"

    github_url = f"https://github.com/{args.github_username}"
    message["attachments"][0]["blocks"][1]["fields"][0]["text"] = f"*Version:*\n {args.version}"
    message["attachments"][0]["blocks"][1]["fields"][1]["text"] = f"*Publish Date:*\n {args.publish_date}"
    message["attachments"][0]["blocks"][1]["fields"][2]["text"] = f"*Author:*\n {args.author}"
    message["attachments"][0]["blocks"][1]["fields"][3]["text"] = f"*Author GitHub:*\n <{github_url}| {args.github_username}>"

    #draft_pr_url = f"https://github.com/OpenLiberty/blogs/pull/{args.pr_number}"
    pr_number = args.pr_url.rsplit('/', 1)[-1]
    message["attachments"][0]["blocks"][2]["fields"][0]["text"] = f"*{args.pr_branch} PR:* <{args.pr_url}| #{pr_number}>"
    message["attachments"][0]["blocks"][2]["fields"][1]["text"] = f"*<{args.url}| Preview {args.pr_branch} Post>*"

    version_no_dots = args.version.replace('.', '')
    ISSUE_URL = f"https://api.github.com/repos/OpenLiberty/open-liberty/issues?labels=blog,target:{version_no_dots};state=all"
    issues = json.loads(requests.get(ISSUE_URL).text)
    if len(issues) > 0:
        for i, issue in enumerate(issues):
            issue_url = issue["html_url"]
            issue_title = issue["title"]
            issue_number = issue["number"]
            message["attachments"][0]["blocks"][3]["text"]["text"] += f"\n <{issue_url}| {issue_title}> #{issue_number}"

    bug_issue_url = f"https://github.com/OpenLiberty/open-liberty/issues?q=+label%3A%22release+bug%22+label%3Arelease%3A{version_no_dots}"    
    if not "beta" in args.version.lower():
        message["attachments"][0]["blocks"].append({
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*<{bug_issue_url}| Corresponding Notable Fixes>*"
                }
            }
        )
    
    slackhook = args.slackhook
    if "test channel" == args.slack_notification.lower():
        slackhook = args.slackhook_test
    
    print("Request data: " + json.dumps(message))
    testData = {"attachments": [{"blocks": [{"text": {"text": "GA Release Blog Post", "type": "plain_text"}, "type": "header"}, {"fields": [{"text": "*Version:*\n 23.0.0.3", "type": "mrkdwn"}, {"text": "*Publish Date:*\n 2050-01-01", "type": "mrkdwn"}, {"text": "*Author:*\n Michal Broz", "type": "mrkdwn"}, {"text": "*Author GitHub:*\n <https://github.com/mbroz2| mbroz2>", "type": "mrkdwn"}], "type": "section"}, {"fields": [{"text": "*Draft PR:* <https://github.com/mbroz2/blogs/pull/32| #32>", "type": "mrkdwn"}, {"text": "*<https://blogs-draft-openlibertyio.mqj6zf7jocq.us-south.codeengine.appdomain.cloud/blog/2050/01/01/23.0.0.3.html| Preview Draft Post>*", "type": "mrkdwn"}], "type": "section"}, {"text": {"text": "*Corresponding Blog Issues:*\n <https://github.com/OpenLiberty/open-liberty/issues/24759| GA BLOG - Support for Java 20> #24759\n <https://github.com/OpenLiberty/open-liberty/issues/24758| GA BLOG - Jakarta EE 10 Platform and Web Profile> #24758\n <https://github.com/OpenLiberty/open-liberty/issues/24741| GA BLOG - Jakarta Batch 2.1> #24741\n <https://github.com/OpenLiberty/open-liberty/issues/24709|  Jakarta EE 10: Jakarta Messaging 3.1 GA BLOG> #24709", "type": "mrkdwn"}, "type": "section"}, {"text": {"text": "*<https://github.com/OpenLiberty/open-liberty/issues?q=+label%3A%22release+bug%22+label%3Arelease%3A23003| Corresponding Notable Fixes>*", "type": "mrkdwn"}, "type": "section"}]}]}
    print("Test data: " + json.dumps(testData))
    response = requests.post(slackhook, headers=headers, data=testData)

    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
