# Contributing to the blog
Create a pull request with the content of the blog post placed in the `drafts` folder using the following file naming scheme: `YYYY-MM-DD-post-title.extension`. HTML, markdown, and AsciiDoc formats can be used. The file extension would be .html, .md, or .adoc respectively. In the blog post file the following front matter variables must be set:
- layout: post
- categories: blog
- title: `title of the blog post`
- author_picture: `secure url to author picture`

`drafts` folder contains blog posts that are still in draft and are not ready to be published

`publish` folder contains blog posts that are ready to be published

`img` folder contains images used in the blog `adoc` files

Once approved, the blog post will be moved from `drafts` to `publish`.

# Docker container for development

### Running the website on your local machine
```
git clone https://github.com/OpenLiberty/blogs.git
git clone https://github.com/OpenLiberty/openliberty.io.git
docker pull kinueng/openliberty.io
docker run --name website -it -p 4000:4000 -v /Users/kueng/work/sandboxes/openliberty.io:/home/jekyll kinueng/openliberty.io
```

### Update the running container with edits
If you make changes to blog Asciidoc files and images, you can run the commands below to update the container with your latest changes.  Below are instructions on how to know when the container renders your new changes.

```
docker exec -it website rm -rf /home/jekyll/src/main/content/_drafts /home/jekyll/src/main/content/_posts /home/jekyll/src/main/content/img/blog
docker cp blogs/drafts website:/home/jekyll/src/main/content/_drafts
docker cp blogs/publish website:/home/jekyll/src/main/content/_posts
docker cp blogs/img/blog website:/home/jekyll/src/main/content/img
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
