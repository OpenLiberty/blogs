# Contributing to the blogs

1. Create an issue for your blog post in this repository.
2. Clone the repo and create your feature branch off of the default `prod` branch.  Alternatively, you can fork this repo and create your personal branch in your fork, but this may make collaboration with others, including reviewers like @lauracowen, more problematic for some in certain situations.
3. Creating/Updating blog content:
   * For a new blog post, create a new file in the [posts](./posts) directory with the name in the format `YYYY-MM-DD-post-title.adoc` where the date represents the expected publication date (e.g. `2021-11-21-open-liberty-is-awesome.adoc`) and write your post.
     * Update the [blogs_tags.json](./blog_tags.json) by adding your blog post to the start of the `posts` array (1-2 entries per line) for each appropriate tag.
   * For an existing, published blog post, simply make the change to the existing blog post file in the [posts](./posts) directory.
     * If necessary, update the [blogs_tags.json](./blog_tags.json) by adding/removing the blog from the `posts` arrays (add to beginning, 1-2 entries per line) of the tags.
   * For an existing blog post that has not been published, work off of the branch/fork that was used to deliver those commits, or you'll need to either cherry pick the post's commits from the `draft` branch.
     * If necessary, update the [blogs_tags.json](./blog_tags.json) by adding/removing the blog from the `posts` arrays (add to beginning, 1-2 entries per line) of the tags.
   * Any images that you want to reference in your blog post must be placed in [img/blog](./img/blog/) directory.
   * For more information regarding creating/editing blog post content (like multiple authors, third-party posts, etc), refer to documentation that follows this section.
4. Once finished and verified locally (adoc editor or blog docker image) create a pull request into the `draft` branch (linked to the issue you created in Step 1) with @lauracowen or anyone else as reviewer, and merge upon approval.
5. Request a build of the [draft site](https://draft-openlibertyio.mybluemix.net/blog/):
    1. Go to [Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io)
    2. More Options > Trigger Build > Make sure the `master` branch is selected (default) > Trigger custom build
6. Once the build completes, check to make sure the blog renders correctly on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/) and resolve any problems (like formatting/styling).  Resolve the issue first in the feature/personal branch and create another PR into `draft` branch and repeat steps 4, 5, & 6 until all issues are resolved.
7. Create a PR from your `feature/personal branch` into `staging` branch verifying that the publication date in the post's file name is still correct, provide a link to your post on the [draft site](https://draft-openlibertyio.mybluemix.net/blog/) and add @lauracowen, SMEs, and/or other reviewers to get their final approval for both content and format.  To make any changes, update the PR with new commit and repeat step 5 & 6 until all issues are resolved.  Once approved, @lauracowen (or another admin) will merge the PR into `staging` and shepherd the post through the remaining steps.
8. Request a build of the [staging site](https://staging-openlibertyio.mybluemix.net/blog/) (same as step 5)
    1. Go to [Travis CI](https://travis-ci.com/github/OpenLiberty/openliberty.io)
    2. More Options > Trigger Build > Make sure the `master` branch is selected (default) > Trigger custom build
9. Once the build completes, check to make sure the blog renders correctly on the [staging site](https://staging-openlibertyio.mybluemix.net/blog/).  This is the final check before the post goes into the [production site](https://openliberty.io/blog/).
10. If there are issues found on the [staging site](https://staging-openlibertyio.mybluemix.net/blog/), they must be resolved quickly, either by merging a new PR with a fix, or reverting it.  If you pushed a new PR with the fix, make sure it also gets pushed to the `draft` branch.
11. Create a PR from `staging` branch into `prod` branch (with an admin approver, though this check is currently purposefully disabled).  Once approved, merge into `prod`.
12. Rebuild the [production site](https://openliberty.io/blog/) on IBM Cloud and verify the post looks as expected on openliberty.io.  If the post used a future date, it will not render on the production site until that day or later (and will need the site to be rebuild to publish).
13. Now that the contents of the feature branch has been successfully delivered to & tested on `draft`, `staging`, and `prod`, delete the feature branch.

Summary of commit flow through branches:  
`prod` <-PR- `staging` <-PR- `draft` <-PR- `feature/personal branch from fork`  
In other words, `prod` should always be a commit subset of `staging` which should be a commit subset of `draft`.  Note, however, that you're not actually, normally, doing a PR from `draft` to `staging` but instead from your `feature/personal branch from fork` into `staging`, but only after it already has been in `draft`.
  
  
### Blog structure (AsciiDoc & front matter)
Blogs are written in [AsciiDoc](https://asciidoctor.org/docs/asciidoc-writers-guide/) format with a file extension of `.adoc`.

In the blog post file the following front matter variables must be set:
- layout: post
- title: `title of the blog post`
- categories: blog
- author_picture: `secure url to author picture`
     - If a picture cannot be found, the openliberty.io logo can be used instead https://avatars3.githubusercontent.com/u/28316667
- author_github: `secure url to author github`
- blog_description: `Description of blog post used in the preview card on openliberty.io/blog`
     - Please keep your `blog_description` to around 60 words
- seo-title: `Blog Title used in search results and on social media - OpenLiberty.io`
     - Please ensure that your `seo-title` ends with ` - OpenLiberty.io`
- seo-description: `Blog Description used in search results and on social media`
     - Please keep your `seo-description` between 50-300 characters


### Blog posts with multiple authors

If you would like to publish a blog post with more than 1 author, you can add the ```additional_authors``` attribute to the liquid front matter. Any number of additional authors can be specified using the following format:
```
additional_authors: 
 - name: author 2 first and last name
   github: secure url to author 2 github
   image: secure url to author 2 picture
 - name:  author 3 first and last name
   github: secure url to author 3 github
   image: secure url to author 3 picture
```

### Contributing a third party blog post

If you would like to add a blog post that is actually a link to an existing third party blog post, you can follow the normal steps described above for creating a blog post. You simply need to add the following attributes to the liquid front matter: 
- redirect_link: secure_url_to_3rd_party_post
- permalink: /blog/redirected.html

Also provide a level 1 heading eg:

`= Creating a cool app with MicroProfile`

### Troubleshooting

Certain characters (eg apostrophe ' ) in the main heading are displayed incorrectly. To fix, escape with a backslash (`\`).
eg `= Minimise turnaround times with Open Liberty\'s dev mode`

# Docker container for development

Github.com does a pretty good job of rendering asciidoc so you can preview your file there, but to see exactly what it will
look like you'll need to install the website software and run it. 

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



