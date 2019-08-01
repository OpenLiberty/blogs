# Contributing to the blog
Fork this repository and write your blog post. Create a pull request with the content of the blog post placed in the `drafts` folder using the following file naming scheme: `YYYY-MM-DD-post-title.extension`.  Blogs are written in [AsciiDoc](https://asciidoctor.org/docs/asciidoc-writers-guide/) format with a file extension of `.adoc`. In the blog post file the following front matter variables must be set:
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

`drafts` folder contains blog posts that are still in draft and are not ready to be published

`publish` folder contains blog posts that are ready to be published

`img/blog` folder contains images used in the blog `adoc` files

Once approved (ask `lauracowen`, or `NottyCode` as backup, to review/approve your PR), the blog post will be moved from `drafts` to `publish`.

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
- redirect_link: 'link'
- permalink: /blog/redirected.html

# Docker container for development

### Running the website on your local machine
```
git clone https://github.com/OpenLiberty/blogs.git
git clone https://github.com/OpenLiberty/openliberty.io.git
docker pull kinueng/openliberty.io
```
Replace "currentFolder" in the following command with the full path to the folder you are in. 
```
docker run --name website -it -p 4000:4000 -v currentFolder/openliberty.io:/home/jekyll kinueng/openliberty.io

# example when current directory is /Users/bruce/projects/blog/website:
# docker run --name website -it -p 4000:4000 -v /Users/bruce/projects/blog/website/openliberty.io:/home/jekyll kinueng/openliberty.io
```

### Update the running container with your edits
Before your new or updated blog entry will appear on the website, you will need to run the commands below to update the container with your latest changes, then wait for the container to finish processing them.  Then you can see your changes at http://localhost:4000/blog/

Note that blogs named with dates in the future, e.g. 2099-01-05, will not be shown, so don't do that. 

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
If you try to run the `docker run....` command above when the container already exists or has been stopped, you'll get an error like this:

```
docker: Error response from daemon: Conflict. The container name "/website" is already in use by container "ddc88f127404e8df53ad149245f636a54f6d5b501ac93477985c27a12b061a94". You have to remove (or rename) that container to be able to reuse that name.
```

Instead, run `docker start website`. 

If the container's been stopped (you pressed control-c, didn't you?) you can run ```docker ps -a`` to get it's container id, then run ``docker rm [containerid]``` to remove it. Then issue that docker run command again. 

There's no feedback about what it's doing. If you run `docker ps`, you can see that the `website` container is now running. However, it takes a few mins for the whole site to come back up so that you can access it from `0.0.0.0:4000` in your browser. So be patient.

When you can access `0.0.0.0:4000`, run the four commands above to update the running container with your new edits (starting with the `docker exec....` command).
