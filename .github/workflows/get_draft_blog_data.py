# Copyright (c) 2022 IBM Corporation and others.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v1.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v10.html
#
# Contributors:
#     IBM Corporation - initial API and implementation

import sys
import re
import os

def main():
    arg_count = len(sys.argv) - 1
    if arg_count != 1:
        print("Expecting 1 arguments (version number). Check the GitHub action.", file=sys.stderr)
        exit(1);

    version = sys.argv[1]

    REVIEWERS_COMMENT_START = "// Contact/Reviewer: "
    reviewers = set()

    # Find the post and then search for reviewers
    posts = ""
    dir = 'posts'
    publish_date = "Not Found"
    author = "Not Found"
    github_username = "Not Found"
    posts = ""
    dir = 'posts'
    for filename in os.listdir(dir):
        file = os.path.join(dir, filename)
        if filename.endswith('-' + version + '.adoc') and os.path.isfile(file):
            print("Found file: " + filename)
            publish_date = filename.partition('-' + version + '.adoc')[0]
            print("Publish date: " + publish_date)
            with open(file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if github_username == "Not Found" and line.find("author_github: https://github.com/") != -1:
                        github_username = line.partition("author_github: https://github.com/")[2].strip()
                        print("GH Username: " + github_username)
                    if author == "Not Found" and line.endswith(" <https://github.com/" + github_username + ">\n"):
                        author = line.partition(" <https://github.com/" + github_username + ">\n")[0]
                        print("Author: " + author)
                    if line.find(REVIEWERS_COMMENT_START) != -1:
                        reviewers.update(line.partition(REVIEWERS_COMMENT_START)[2].strip().split(","))
            break


    # for filename in os.listdir(dir):
    #     file = os.path.join(dir, filename)
    #     if filename.endswith('-' + version + '.adoc') and os.path.isfile(file):
    #         print("Found file: " + filename)
    #         with open(file, 'r') as file:
    #             lines = file.readlines()
    #             for line in lines:
    #                 if line.find(REVIEWERS_COMMENT_START) != -1:
    #                     reviewers.update(line.partition(REVIEWERS_COMMENT_START)[2].strip().split(","))
    #         break

    # print('::set-output name=publish-date::' + filename.partition('-' + version + '.adoc')[0])
    print('::set-output name=publish-date::' + publish_date)
    print('::set-output name=author-name::' + author)
    print('::set-output name=github-username::' + github_username)
    print('::set-output name=reviewers::' + ','.join(sorted(list(reviewers))))
                
if __name__ == "__main__":
    main()