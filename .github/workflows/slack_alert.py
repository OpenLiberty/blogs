import requests
import json
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
                    "text": {
                        "type": "mrkdwn",
                        "text": "*First Draft PR:* <fakeLink.toEmployeeProfile.com| #pr_number>"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*<fakeLink.toEmployeeProfile.com| Preview Draft Post>*"
                    }
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
    "Content-type": "application/json"
}

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('version', type=str)
    parser.add_argument('publish_date', type=str)
    parser.add_argument('author', type=str)
    parser.add_argument('github_username', type=str)
    parser.add_argument('pr_number', type=str)
    parser.add_argument('draft_url', type=str)
    parser.add_argument('slackhook', type=str)
    args = parser.parse_args()

    if "beta" in args.version.lower():
        message["attachments"][0]["blocks"][0]["text"] = "Beta Release Blog Post"
    else:
        message["attachments"][0]["blocks"][0]["text"] = "GA Release Blog Post"

    github_url = f"https://github.com/{args.github_username}"
    message["attachments"][0]["blocks"][1]["fields"][0]["text"] = f"*Version:*\n {args.version}"
    message["attachments"][0]["blocks"][1]["fields"][1]["text"] = f"*Publish Date:*\n {args.publish_date}"
    message["attachments"][0]["blocks"][1]["fields"][2]["text"] = f"*Author:*\n {args.author}"
    message["attachments"][0]["blocks"][1]["fields"][3]["text"] = f"*Author GitHub:*\n <{github_url}| {args.github_username}>"

    pr_url = f"https://github.com/OpenLiberty/blogs/pull/{args.pr_number}"
    message["attachments"][0]["blocks"][2]["text"]["text"] = f"*First Draft PR:* <{pr_url}| #{args.pr_number}>"

    message["attachments"][0]["blocks"][3]["text"]["text"] = f"*<{args.draft_url}| Preview Draft Post>*"

    version_no_dots = args.version.replace('.', '')
    ISSUE_URL = f"https://api.github.com/repos/OpenLiberty/open-liberty/issues?labels=blog,target:{version_no_dots}"
    issues = json.loads(requests.get(ISSUE_URL).text)

    for i, issue in enumerate(issues):
        issue_url = issue["html_url"]
        issue_title = issue["title"]
        issue_number = issue["number"]
        message["attachments"][0]["blocks"][4]["text"]["text"] += f"\n <{issue_url}| {issue_title}> #{issue_number}"
    
    print(message)

    requests.post(args.slackhook, headers=headers, data=json.dumps(message))
