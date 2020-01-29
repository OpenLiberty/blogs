docker exec -it website rm -rf /home/jekyll/src/main/content/_drafts /home/jekyll/src/main/content/_posts /home/jekyll/src/main/content/img/blog
docker cp blogs/drafts website:/home/jekyll/src/main/content/_drafts
docker cp blogs/publish website:/home/jekyll/src/main/content/_posts
docker cp blogs/img/blog website:/home/jekyll/src/main/content/img
docker cp blogs/blog_tags.json website:/home/jekyll/src/main/content
