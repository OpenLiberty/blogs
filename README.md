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
