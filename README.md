# Writing and publishing blog posts on the OpenLiberty.io blog

* [Authors: creating a new blog post](#Authors-creating-a-new-blog-post)
* [Editors: editing and publishing a post](#Editors-editing-and-publishing-a-post)
* [Authors and Editors: updating a published post](#Authors-and-Editors-updating-a-published-post)
* [Troubleshooting Asciidoc](#Troubleshooting-Asciidoc)
* [Running a Docker container for local preview](#Running-a-Docker-container-for-local-preview)


## Authors: creating a new blog post

These steps are to be completed by the author of the blog post.

1. Create [an issue](https://github.com/OpenLiberty/blogs/issues/new) for the blog post. This is to help the editors track the progress of the post.

   * **All blog posts except release blog posts**

     Create a normal issue. In the description, give a simple outline of the purpose of the blog post. If there is a specific date by which the post must be available, mention that in the description too.

  * **Release blog posts** (Open Liberty release announcements only)

    Create an issue using the `Open Liberty release notes` issue template. Make sure to select each task in the issue as you complete it to show progress.
    

2. Clone the repo and create your feature branch off of the default `prod` branch. From the `prod` branch, run: `git branch -b branch_name`, where `branch_name` is a name you give your new branch.

    Do _all_ your editing in this branch.

3. Create your blog post using [Asciidoc](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/) markup (use an editor such as [VSCode with the Asciidoc plugin](https://marketplace.visualstudio.com/items?itemName=joaompinto.asciidoctor-vscode)):

    * **Blog post** (probably what you're doing)
    
      Copy the [post-single-author.adoc](./templates/post-single-author.adoc) file (or [post-multiple-authors.adoc](./templates/post-multiple-authors.adoc) for multiple authors) to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date (e.g. `2021-11-21-open-liberty-is-awesome.adoc`).

      Place any images in [img/blog](./img/blog/). For multiple authors, third-party posts, etc, see the documentation at the end of this README.
  
    * **Release blog post** (Open Liberty release announcements only)

      Copy the [release-post.adoc](./templates/release-post.adoc) file to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date (e.g. `2021-11-21-open-liberty-is-awesome-210011.adoc`).

      Place any images in [img/blog](./img/blog/). For multiple authors, see the documentation at the end of this README.

      Ensure that the tags (e.g. `// tag::intro[]` and `// end::intro[]`) in the template are retained around the relevant parts of the release post. The release post will contain GA and beta content but the tags will be used to build GA-only versions of the post content.

    * **Third-party blog post** (externally hosted posts only)

      Copy the [third-party-blog-post.adoc](./templates/third-party-blog-post.adoc) file to the [posts](./posts) directory and rename the file using the format `YYYY-MM-DD-post-title.adoc`, where the date represents the expected publication date (e.g. `2021-11-21-open-liberty-is-awesome.adoc`).

4. If you are not employed by IBM, in at least one of your commits, sign off the commit using [the Developer Certificate process](./CONTRIBUTING.md).

4. When you have finished the post, check that it renders correctly. If you have a preview function in your editor, use that (eg the Asciidoc plugin in VSCode). Alternatively, you can use the [Docker image to run a local build of the file](#running-a-docker-container-for-local-preview).

5. Push the file to GitHub, then create a pull request (PR) into the `draft` branch.

   Link the PR to the issue you created in Step 1.

5. Request a build of the [draft openliberty.io site](https://draft-openlibertyio.mybluemix.net/blog/):
    1. Sign in to [Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io) with your GitHub account.
    2. Click **More Options > Trigger Build**. Make sure the `master` branch is selected, then click **Trigger custom build**.
    
          The draft site build starts running.

6. When the build is finished, check that the blog renders correctly on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/).

  If you see any problems (e.g. formatting or typos), resolve them first in your branch, create another PR into `draft` branch (link the PR to the issue again), then run the [draft site build from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io) again.

7. When you're happy with the post, create a PR from your branch (_not_ from the `draft` branch) to the `staging` branch.

   Link the PR to the issue.

   In the PR, provide a link to your post on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/).
   
   Add @lauracowen, your technical reviewer, and any other reviewers to get their final approval for both content and format.
   
   As before, make any changes in your branch, push the changes to the `draft` branch, then run the [draft site build from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io) again to check that they are fine on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/).

   This automatically updates the PR to `staging`.

You've written a post!

The editors will now review and edit the post. Please respond to any questions they ask or suggestions they make. Their aim is to make the post readable and useful to its target audience.


## Editors: editing and publishing a post

These steps are completed by the editors of the blog. They might ask questions or make suggestions to the author of the post. They might also make edits directly in the post to prepare it for publishing.

1. Review the post on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/) as linked from the issue.

   Ask the author to make changes by adding review comments to the PR.

   For edits such as punctuation, formatting, highlighting, adding SEO details, or larger changes discussed with the author, the editor can make the edits directly in the author's branch and push the changes to `draft` branch, then rebuild the [draft site from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io) to check them.
   
   To check out the author's branch locally: `git fetch origin` then `git checkout -b branch_name origin/branch_name`, which creates a new local branch that's linked to their remote branch. When you've made changes, push them back to `origin/branch_name`.

2. Add tags to the blog post:

   a. In the author's branch, update the [blogs_tags.json](./blog_tags.json) file by adding the slug of the blog post (the file name without the date part or the `.adoc`) to the start of the `posts` array (1-2 entries per line) for each appropriate tag. Do this in an editor (such as VSCode) and make sure the syntax is correct.

   b. Push the changes to `draft` branch as before and check that they get built correctly on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/).

2. When a publishing date has been decided:

   * Check that the post looks fine.
   
   * Check that the author's details and the SEO details, including front matter, the title, and the filename slug, are appropriate for the post.
   
   * Check that the post has tags defined in the `blogs_tags.json` file in the same PR.

   * If necessary, rename the file with the planned publication date.

3. On the day of publication (or the day before):

   a. Approve the PR.
   
   b. Ask @lauracowen (or another admin) to merge the PR into `staging`.
   
4. Request a build of the [staging openliberty.io site from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io).

5. When the build has finished, check to make sure the blog renders correctly on the [staging site](https://staging-openlibertyio.mybluemix.net/blog/). 

   This is the final check before the post is published live on the [production site](https://openliberty.io/blog/).

   If there are any problems found on the [staging site](https://staging-openlibertyio.mybluemix.net/blog/), you must resolve them quickly or revert the PR.
   
   Make any changes in the author's branch, and push to both `draft` and `staging`.
   
6. To publish the post, create a PR from `staging` branch to `prod` branch and add @lauracowen (or other admin) as approver.

7. When the PR is approved, merge it into `prod`.

12. Rebuild the [production site from the IBM Cloud console](https://console.bluemix.net/devops/pipelines/fcc7c3e9-9c40-4a58-8a7f-09c08413ab7d?env_id=ibm:yp:us-south).

    When the build has finished, check that the post looks as expected on [openliberty.io/blog](https://openliberty.io/blog/).

    If the post's file name uses a future date, the post will not exist on the production site until at least that date and the production site has been rebuilt.

13. When the post is published, and any changes you made are in all three branches (`draft`, `staging`, and `prod`), delete the author's branch.

You've published a post!



## Authors and Editors: updating a published post

If a published post on openliberty.io/blog contains an error or needs updating in any way, anyone can create a PR to get it fixed.

1. As when creating a new post (see above), clone the `blogs` repo and create a new branch based on the `prod` branch. You will do all your work in this branch.

2. Open the file in an editor (e.g. [VSCode with the Asciidoc plugin](https://marketplace.visualstudio.com/items?itemName=joaompinto.asciidoctor-vscode)) and make any changes needed.

3. If the tags need correcting, update the [blogs_tags.json](./blog_tags.json) file. If you add new tags, make sure to add the blog post's slug to the beginning of the `posts` arrays (1-2 entries per line) for each tag.

4. Create a PR from your branch to the `draft` branch, then run the [draft site build from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io) to check that the changes are fine on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/).

   Make any changes in your branch then push to `draft` branch again rebuild.

5. When the post is ready to publish, create a PR from your branch to `staging branch` (not from `draft` branch) and add @lauracowen as reviewer.

6. When approved, @lauracowen (or other admin) will merge to `staging`, then run the [build for the staging site from Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io) and check that it looks fine on the [staging site](https://staging-openlibertyio.mybluemix.net/blog/).

7. The approver will then create a PR from `staging` to `prod`, then merge and [rebuild the production site from the IBM Cloud console](https://console.bluemix.net/devops/pipelines/fcc7c3e9-9c40-4a58-8a7f-09c08413ab7d?env_id=ibm:yp:us-south) to publish the updates on the [openliberty.io/blog](https://openliberty.io/blog/).



## Troubleshooting Asciidoc

Certain characters (eg apostrophe ' ) in the main heading are displayed incorrectly. To fix, escape with a backslash (`\`).
eg `= Minimise turnaround times with Open Liberty\'s dev mode`

See also:
* [Asciidoc quick syntax](https://asciidoctor.org/docs/asciidoc-syntax-quick-reference/)
* [Asciidoc user manual (more detailed)](https://asciidoctor.org/docs/user-manual/)



## Running a Docker container for local preview

Github.com does a pretty good job of rendering asciidoc so you can preview your file there, but to see exactly what it will
look like you can run the website locally. 

### Running the website on your local machine
```
git clone https://github.com/OpenLiberty/blogs.git
git clone https://github.com/OpenLiberty/openliberty.io.git
docker pull kinueng/openliberty.io
```
Replace "currentFolder" in the following command with the full path to the folder you are in. 
```
docker run --rm --name website -it -p 4000:4000 -v currentFolder/openliberty.io:/home/jekyll kinueng/openliberty.io

# example when current directory is /Users/bruce/projects/blog/website:
# docker run --name website -it -p 4000:4000 -v /Users/bruce/projects/blog/website/openliberty.io:/home/jekyll kinueng/openliberty.io
```

### Update the running container with your edits
Before your new or updated blog entry will appear on the website, you will need to run the script below to update the container with your latest changes, then wait for the container to finish processing them.  Then you can see your changes at http://localhost:4000/blog/

Note that blogs named with dates in the future, e.g. 2099-01-05, will not be shown, so don't do that. 

```
./blogs/scripts/refresh_docker_image.sh
```

### How to know when your changes are rendered by the container
You will see `Jekyll` detect your new files and regenerate the blog files.  You will want to wait for the line "...done in XXXX seconds."

```
      Regenerating: 101 file(s) changed at 2018-10-29 18:53:10
      ...
      Jekyll Feed: Generating feed for posts
      ...
            ...done in 121.8705398 seconds.
```



