---
name: Open Liberty GA and beta release blog posts
about: Checklist that must be completed to create and publish Open Liberty release notes.
title: Open Liberty release blog post for VERSION_NUMBER
labels: release
assignees: ryan-storey

---

This issue is to track the tasks involved in creating and publishing the GA and beta release notes for an Open Liberty release.

The Open Liberty release notes are published as a post on the [Open Liberty blog](https://openliberty.io/blog/):
- [GA blog post example](https://openliberty.io/blog/2022/06/07/microprofile-graphql-2-22006.html)
- [beta blog post example](https://openliberty.io/blog/2022/06/09/time-based-log-rollover-22007-beta.html)

## Creating the blog posts

The Open Liberty release blog posts are written in asciidoc and pushed to the [OpenLiberty/blogs](https://github.com/openliberty/blogs) repo. The repo README contains [instructions on how to create, build, and review](https://github.com/OpenLiberty/blogs/blob/prod/README.md) the posts, including template files to help you.

You need to create **two** separate posts:

- a GA release blog post
- a beta release blog post

Follow the instructions in the README and the template file to complete the following tasks _for each post_:

- [ ] Create a draft blog post using either the [GA release blog post template](https://github.com/OpenLiberty/blogs/blob/prod/templates/ga-release-post.adoc) or the [beta release blog post template](https://github.com/OpenLiberty/blogs/blob/prod/templates/beta-release-post.adoc). Build the draft blog post on the draft website according to the [blog post instructions](https://github.com/OpenLiberty/blogs/blob/prod/README.md).
- [ ] When you've compiled the whole blog and checked that it makes sense to the best of your knowledge, create a PR from your feature branch to the `staging` branch (as described in the [blog post instructions](https://github.com/OpenLiberty/blogs/blob/prod/README.md)).
- [ ] Get the draft post reviewed by all the people who contributed the content to the blog post.
- [ ] Then, when they're all happy, ask @mbroz2 to review it.
- [ ] Agree with @mbroz2 which feature will lead this blog post, then write a title, slug, summary first paragraph, and SEO front matter appropriately.
- [ ] Get the post approved by @mbroz2.
- [ ] On release day (usually Tuesday for the GA release post and Thursday for the beta release post), @mbroz2 will publish the post.

## All done?

Check that you've completed every task above. Select each check box to confirm that you have before closing this issue.
