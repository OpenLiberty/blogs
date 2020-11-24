---
name: Open Liberty GA release blog post
about: Checklist that must be completed to create and publish Open Liberty release notes.
title: Open Liberty GA release blog post for VERSION_NUMBER
labels: release
assignees: lauracowen

---

This issue is to track the tasks involved in creating and publishing the releases notes for an Open Liberty 4-weekly release.

The Open Liberty release notes are presented in three places:
- [Open Liberty blog](https://openliberty.io/blog/) (GA and beta features; [example](https://openliberty.io/blog/2020/05/07/EJB-persistent-timers-20005.html))
- [Red Hat Runtimes release notes for Open LIberty](https://access.redhat.com/documentation/en-us/open_liberty/2020/) (GA features only; [example](https://access.redhat.com/documentation/en-us/open_liberty/2020/html/release_notes_for_open_liberty_20.0.0.5_on_red_hat_openshift_container_platform/features))
- [Red Hat Developer blog](https://developers.redhat.com/blog/) (GA features only; [example](https://developers.redhat.com/blog/2020/05/13/open-liberty-20-0-0-5-brings-updates-to-ejb-persistent-timers-coordination-and-failover-across-members/))


## 1. Open Liberty release blog post

The Open Liberty release blog post is written in asciidoc and pushed to the [OpenLiberty/blogs](https://github.com/openliberty/blogs) repo. The repo README contains [instructions on how to create, build, and review](https://github.com/OpenLiberty/blogs/blob/prod/README.md) the post, including a template file to help you.

Follow the instructions in the README and the template file to complete the following tasks:

- [ ] Create a draft release blog post in asciidoc, build to [the draft site](https://draft-openlibertyio.mybluemix.net/blog/), and create a PR to the `staging` branch with a link to the post on [the draft site](https://draft-openlibertyio.mybluemix.net/blog/). Add all the reviewers (see below) to the PR so that they can add all their review feedback and approvals in the PR.
- [ ] Get the draft post reviewed by:
  - [ ] All the people who contributed the content to the blog post.
  - [ ] At least one of the following people: @lauracowen, @mbroz2, @NottyCode
- [ ] Agree with @lauracowen, @mbroz2, or @NottyCode which feature will lead this blog post, then write a title, slug, summary first paragraph, and SEO front matter appropriately.
- [ ] Get the post approved by @lauracowen, @mbroz2, or @NottyCode.
- [ ] On release day (usually a Friday), @lauracowen, @mbroz2, or @NottyCode will publish the post.

## 2. Red Hat Runtimes release notes for Open Liberty

The release notes are automatically built from the asciidoc release blog post. This is done by using the appropriate tags in the asciidoc source and then the Red Hat documentation build includes the tagged sections in the release notes. The tags ensure that information in the blog post that is not relevant to the Red Hat Runtimes release are omitted from the Red Hat Runtimes release notes.

- [ ] In the asciidoc source of the draft release blog post, check that the include tags are in the correct places in the asciidoc source file:
  - [ ] `// tag::intro[]` (before the first paragraph)
  - [ ] `// end::intro[]` (after the link to the list of fixed bugs)
  - [ ] `// tag::run[]` (before the Maven coordinates)
  - [ ] `//end::run[]` (after the Dockerfile entry)
  - [ ] `//tag::features[]` (before the first GA feature section)
  - [ ] `//end::features[]` (after the last GA feature section)
- [ ] In [the release notes file](https://raw.githubusercontent.com/PurpleLiberty/docs/master/releasenotes/master-remote.adoc) (in a separate repo on GitHub), find the include statement in the **Features** section of the release notes. Edit the file name part of the include statement so that it targets the new Open Liberty release blog post .adoc file. Don't change anything else. Work with the ID team if they contact you to resolve any problems when the Red Hat build is run.

## 3. Red Hat Developer blog post

Red Hat Developer blog is authored in Wordpress so you must convert the asciidoc blog post to Wordpress HTML markup. We have a tool that does most of the conversion for you and removes the sections that are not needed (eg the beta content).

- [ ] Use [Tom's conversion tool](https://github.ibm.com/was-WASdev/asciidoc-to-wordpresshtml) to convert the asciidoc (.adoc) file to a text file of HTML source (it also removes irrelevant content such as the beta sections, and adds a final paragraph).
- [ ] Log in to [Red Hat Developer blog's Wordpress Admin dashboard](https://developers.redhat.com/blog/wp-login.php). And make sure you have a profile on the site. See the [instructions in the Dashboard](https://developers.redhat.com/blog/wp-admin/index.php) if this is your first post.
- [ ] [Create a new post](https://developers.redhat.com/blog/wp-admin/post-new.php).
- [ ] Paste the content from the text file into the editor.
- [ ] Provide a title and edit the slug so that it's succinct.
- [ ] Select the relevant categories. Always select `Java` and `Open source`, plus any other categories _relevant_  to this post.
- [ ] Upload and insert any images using the Wordpress editor.
- [ ] Preview the post and check that it displays correctly and makes sense (e.g. doesn't contain any beta content).
- [ ] Save the post, then email a link to `contributors@redhat.com` to let them know that it's ready for review.
- [ ] Work with the Red Hat Developer blog editors to finalise the post. They might ask for additional clarfications or minor changes. They will also make edits directly in the post. When they are happy, they'll check with you then schedule the post to publish on the Tuesday morning after the Open Liberty release.

## All done?

Check that you've completed every task above. Select each check box to confirm that you have before closing this issue.
