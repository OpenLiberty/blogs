# Writing and publishing blog posts on the OpenLiberty.io blog

* [Authors: creating a new blog post](#Authors-creating-a-new-blog-post)
* [Editors: editing and publishing a post](#Editors-editing-and-publishing-a-post)
* [Authors and Editors: updating a published post](#Authors-and-Editors-updating-a-published-post)
* [Troubleshooting Asciidoc](#Troubleshooting-Asciidoc)
* [Troubleshooting GitHub workflow](#troubleshooting-github-workflow)


## Authors: creating a new blog post

These steps are to be completed by the author of the blog post.

1. Create [an issue](https://github.com/OpenLiberty/blogs/issues/new) for the blog post. This is to help the editors track the progress of the post.

   * **All blog posts except release blog posts**

     Create a normal issue. In the description, give a simple outline of the purpose of the blog post. If there is a specific date by which the post must be available, mention that in the description too.

   * **GA release blog posts** (Open Liberty GA release announcements only)

     Create an issue using the `Open Liberty release notes` issue template. Make sure to select each task in the issue as you complete it to show progress.

   * **Beta release blog posts** (Open Liberty beta release announcements only)

     Create a normal issue. In the title, make clear that it's for the beta release and which release version.

2. Clone the repo and create a branch off the default `prod` branch. Be sure to clone using SSH (`git clone git@github.com:OpenLiberty/blogs.git`), not HTTPS, or you won't be able to push to the repo in GitHub. From the `prod` branch, run: `git checkout -b branch_name`, where `branch_name` is a name you give your new branch.

    Do _all_ your editing in this branch so that the blog editors can make any necessary edits directly in the branch before publishing your post. You'll push this branch directly to the shared repo (not a fork) in a later step.

3. Create your blog post using [Asciidoc](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/) markup (use an editor such as [VSCode with the Asciidoc plugin](https://marketplace.visualstudio.com/items?itemName=joaompinto.asciidoctor-vscode)):

    * **Blog post** (probably what you're doing)
    
      Copy the [post-single-author.adoc](./templates/post-single-author.adoc) file (or [post-multiple-authors.adoc](./templates/post-multiple-authors.adoc) for multiple authors) to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date (e.g. `2021-11-21-open-liberty-is-awesome.adoc`).

      Place any images in [img/blog](./img/blog/).
  
    * **GA release blog post** (Open Liberty GA release announcements only)

      Copy the [ga-release-post.adoc](./templates/ga-release-post.adoc) file to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date and the end of the file name is the release version number without periods (e.g. `2021-11-21-open-liberty-is-awesome-210011.adoc`).

      Place any images in [img/blog](./img/blog/).

      Ensure that the Asciidoc tags (e.g. `// tag::intro[]` and `// end::intro[]`) in the template are retained around the relevant parts of the release post. These Asciidoc tags will be used to build alternative versions of the post content.
   
    * **Beta release blog post** (Open Liberty beta release announcements only)

      Copy the [beta-release-post.adoc](./templates/beta-release-post.adoc) file to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date and the end of the post title is the beta release version number without periods or hyphens (e.g. `2021-11-21-new-awesomeness-coming-soon-210012beta.adoc`).

      Place any images in [img/blog](./img/blog/).

    * **Third-party blog post** (externally hosted posts only)

      Copy the [third-party-blog-post.adoc](./templates/third-party-blog-post.adoc) file to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date (e.g. `2021-11-21-open-liberty-is-awesome.adoc`).

4. If you are not employed by IBM, in at least one of your commits, sign off the commit using [the Developer Certificate process](./CONTRIBUTING.md).

4. When you have finished the post, check that it renders correctly. If you have a preview function in your editor, use that (eg the Asciidoc plugin in VSCode). Otherwise, you can check that GitHub renders it properly when you push to GitHub in the next step.

5. Push the file to GitHub, then create a pull request (PR) into the `draft` branch.

   Link the PR to the issue you created in Step 1.
   Anyone can review/approve the PR before you merge it.

   (If you've been working in a fork for some reason, create a feature branch [see Step 2] and push your changes to the feature branch, then create a PR to the `draft` branch from there.)

   If you find there are a load of merge conflicts at this stage, see [Troubleshooting GitHub workflow](#troubleshooting-github-workflow).


5. Currently, Travis is no longer building our non-prod sites. All the builds and deployments of non-prod sites have been moved to IBM Cloud and now build automatically whenever the a PR is merged into their respective branch. These builds are private and, therefore, their detailed build/deploy progress can't be tracked. However, if you have access to the [Slack channel](https://app.slack.com/client/T15GKHBT4/C01GXGW1DGQ), you can at least track when the builds start and finish.  
   ~~Request a build of the [draft openliberty.io site](https://draft-openlibertyio.mybluemix.net/blog/):~~
    1. ~~Sign in to [Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io/branches) with your GitHub account.~~
    2. ~~Click **More Options > Trigger Build**. Type `draft` in the **Branch** field, then click **Trigger custom build**.~~
    
          ~~The draft site build starts running.~~

6. When the build is finished, check that the blog renders correctly on either the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or the [full draft site](https://draft-openlibertyio.mybluemix.net/blog/).  

   In addition to the existing [full draft site](https://draft-openlibertyio.mybluemix.net/blog/) we now have a [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/), which contains only the blog content, allowing it to build and deploy much quicker. However, since this site contains only the blog content, any links to other parts of openliberty.io will not resolve. In general, use the blogs-draft site to review content because it updates much quicker than the full site. However, if you need to review content that links to pages on openliberty.io that are not in the blogs, use the full draft site.

   If you see any problems , such as formatting issues or typos, resolve them first in your branch. Then, create another PR into `draft` branch, link the PR to the issue again,  and get the PR merged. Wait for IBM Cloud to rebuild [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or [draft site](https://draft-openlibertyio.mybluemix.net/blog/) and verify the change.

7. When you're happy with the post:
   - Create a PR from your branch (_not_ from the `draft` branch) to the `staging` branch.
   - Link the PR to the issue.
   - In the PR, provide a link to your post on the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or [draft site](https://draft-openlibertyio.mybluemix.net/blog/). 
   - Ideally, also paste a screenshot of the entire blog post page as this will allow reviewers to see the rendered post content even while the sites are innaccessible (e.g. redeploys). 
   - Add @GraceJansen, as well as your technical reviewer and any other reviewers to get their final approval for both content and format.
8. The editors will now review and edit the post. Please respond to any questions they ask or suggestions they make. Their aim is to make the post readable and useful to its target audience.
9. If you need to make changes based on review comments, as before: 
   - Make any changes in your feature branch
     - The updates that you make to your branch for the `draft` PR will be automatically picked up by your `staging` PR; there is no need to update it. 
   - Create a PR to the `draft` branch 
   - Link the PR to the issue
   - Merge the PR
   - Once the site rebuilds, check that everything is correct on the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or [draft site](https://draft-openlibertyio.mybluemix.net/blog/).
10. Get reviewers to review the updates in your new PR.

You're done! The editors will handle the rest.

Please note that if you have a specific date in mind that you want this blog to be published by, we need a final draft of the blog to be ready for editing in the draft repo a minimum of two weeks prior to the desired publish date.

## Editors: editing and publishing a post

These steps are completed by the editors of the blog. As editor, you might ask questions or make suggestions to the author of the post. You might also make edits directly in the post to prepare it for publishing.

1. Review the post on the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or [draft site](https://draft-openlibertyio.mybluemix.net/blog/) as linked from the issue.

   Ask the author to make changes by adding review comments to the PR.

   For edits such as punctuation, formatting, highlighting, adding SEO details, or larger changes discussed with the author, the editor can make the edits directly in the author's branch and push the changes to `draft` branch, which automatically rebuilds the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) and [draft site](https://draft-openlibertyio.mybluemix.net/blog/) where you can verify the changes.
   
   To check out the author's branch locally: `git fetch origin` then `git checkout -b branch_name origin/branch_name`, which creates a new local branch that's linked to their remote branch. When you've made changes, push them back to `origin/branch_name`.

2. When a publishing date has been decided:

   * Check that the post looks fine.
   
   * Check that the author's details and the SEO details, including front matter, the title, and the filename slug, are appropriate for the post.

   * If necessary, rename the file with the planned publication date.

2. Add blog tags to the blog post:

   a. In the `staging` branch, update the [blogs_tags.json](./blog_tags.json) file by adding the slug of the blog post (the file name without the date part or the `.adoc`) to the start of the `posts` array (1-2 entries per line) for each appropriate tag. You can do this in the web UI editor as long as you're careful with the syntax. This is done in staging to reduce the number of merge conflicts in the `draft` branch later. However, you should backport this change to draft once it is verified on staging.

   b. Merge the changes to `staging` branch. You can do this in advance of the post being ready (as long as the post's file name doesn't change). It's fine if this file gets merged to `prod` earlier than the post itself.

3. On the day of publication (or the day before):

   a. Approve the PR.
   
   b. Merge the PR into `staging`.
   
4. IBM Cloud will automatically rebuild the [blogs-staging site](https://blogs-staging-openlibertyio.mybluemix.net/blog/) and [staging site](https://staging-openlibertyio.mybluemix.net/blog/). If you have access, you can track the progress in the [Slack channel](https://app.slack.com/client/T15GKHBT4/C01GXGW1DGQ).  
~~Request a build of the [staging openliberty.io site from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io/branches) (type `staging` in the **Branch** field of the dialog).~~

5. When the build has finished, check to make sure the blog with its blog tags render correctly on the [blogs-staging site](https://blogs-staging-openlibertyio.mybluemix.net/blog/) or [staging site](https://staging-openlibertyio.mybluemix.net/blog/). The latter includes the entire site, while the former just has the blog content.  If you need to verify links to other parts of the site (outside of the /blogs/ content) then you'll need to wait for the full [staging site](https://staging-openlibertyio.mybluemix.net/blog/) to build.  

   This is the final check before the post is published live on the [production site](https://openliberty.io/blog/).

   If there are any problems with the content in the `staging` branch, you must resolve them quickly or revert the PR (the post must not stay in `staging` longer than a couple of hours or you risk someone accidentally publishing it for you).
   
   Make any changes in the author's branch, and push to both `draft` and `staging`.
   
6. To publish the post, create a PR from `staging` branch to `prod` branch and add the author of the post or another editor as approver.

7. When the PR is approved, merge it into `prod`.

12. Rebuild the [production site from the IBM Cloud console](https://cloud.ibm.com/devops/pipelines/063d397c-febc-4f73-8340-61da6bc775f5?env_id=ibm:yp:us-south).

    When the build has finished, check that the post looks as expected on [openliberty.io/blog](https://openliberty.io/blog/).

    If the post's file name uses a future date, the post will not exist on the production site until at least that date and the production site has been rebuilt.

13. When the post is published, and any changes you made are in all three branches (`draft`, `staging`, and `prod`), delete the author's branch.

You've published a post!



## Authors and Editors: updating a published post

If a published post on openliberty.io/blog contains an error or needs updating in any way, anyone can create a PR to get it fixed.

1. As when creating a new post (see above), clone the `blogs` repo and create a new branch based on the `prod` branch. You will do all your work in this branch.

2. Open the file in an editor (e.g. [VSCode with the Asciidoc plugin](https://marketplace.visualstudio.com/items?itemName=joaompinto.asciidoctor-vscode)) and make any changes needed.

3. If the blog tags need correcting, update the [blogs_tags.json](./blog_tags.json) file. If you add new tags, make sure to add the blog post's slug to the beginning of the `posts` arrays (1-2 entries per line) for each tag.

4. Create a PR from your branch to the `draft` branch. After the PR is merged, wait for IBM Cloud to rebuild the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or [full draft site](https://draft-openlibertyio.mybluemix.net/blog/). If you have access to [this Slack channel](https://app.slack.com/client/T15GKHBT4/C01GXGW1DGQ), you can use it to track build/deploy progress.  Verify the changes on the [blogs-draft site](https://blogs-draft-openlibertyio.mybluemix.net/blog/) or [draft site](https://draft-openlibertyio.mybluemix.net/blog/).

   Make any changes in your branch, then push to the `draft` branch again  and verify the changes after rebuild.

5. Create a PR from your branch to `staging branch` (not from `draft` branch) and add @GraceJansen as reviewer. You can create this PR at any point because any new changes you make in your branch are automatically added to the PR.

6. When the PR is approved, the editor will merge it the `staging` branch, causing IBM Cloud to automatically kick off a build of both the [blogs-staging site](https://blogs-staging-openlibertyio.mybluemix.net/blog/) and [staging site](https://staging-openlibertyio.mybluemix.net/blog/), which you can use to verify the changes look correct.

7. The approver will then create a PR from `staging` to `prod`, then merge and [rebuild the production site from the IBM Cloud console](https://cloud.ibm.com/devops/pipelines/063d397c-febc-4f73-8340-61da6bc775f5?env_id=ibm:yp:us-south) to publish the updates on the [openliberty.io/blog](https://openliberty.io/blog/).



## Troubleshooting Asciidoc

Certain characters (eg apostrophe ' ) in the main heading are displayed incorrectly. To fix, escape with a backslash (`\`).
eg `= Minimise turnaround times with Open Liberty\'s dev mode`

See also:
* [Asciidoc quick syntax](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/)
* [Asciidoc user manual (more detailed)](https://asciidoctor.org/docs/user-manual/)

## Troubleshooting GitHub workflow

When you create a PR from your feature branch to the `draft` branch, you might find that you have some conflicts. If you use the Web UI to resolve the conflicts and commit those changes, you will find that GitHub has merged _everything_ from the `draft` branch into your feature branch, including other people's drafts. You _must not_ try to merge all those changes to `staging` or else you'll end up publishing a load of half-finished work. Instead, create a new feature branch off `prod` and use the `git cherry-pick` command to select only the files that you want to publish from the `draft` branch. Then use this new feature branch to create the PR to `staging`.

For more about the `git cherry-pick` command, see [StackOverflow](https://stackoverflow.com/questions/9339429/what-does-cherry-picking-a-commit-with-git-mean) (or search online for more help). You might need some practice to get the hang of it but it's a useful skill to acquire if you do much in GitHub.
