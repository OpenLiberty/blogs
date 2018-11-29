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

### Restarting the container
If you try to run the `docker run....` command above when the container already exists, you'll get an error like this:

```
docker: Error response from daemon: Conflict. The container name "/website" is already in use by container "ddc88f127404e8df53ad149245f636a54f6d5b501ac93477985c27a12b061a94". You have to remove (or rename) that container to be able to reuse that name.
```

Instead, run `docker start website`.

There's no feedback about what it's doing. If you run `docker ps`, you can see that the `website` container is now running. However, it takes a few mins for the whole site to come back up so that you can access it from `0.0.0.0:4000` in your browser. So be patient.

When you can access `0.0.0.0:4000`, run the four commands above to update the running container with your new edits (starting with the `docker exec....` command).
