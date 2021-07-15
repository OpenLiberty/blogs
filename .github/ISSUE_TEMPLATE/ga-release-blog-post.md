---
name: Open Liberty GA release blog post
about: Checklist that must be completed to create and publish Open Liberty release notes.
title: Open Liberty GA release blog post for VERSION_NUMBER
labels: release
assignees: jakub-pomykala, austin0

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
  - [ ] At least one of the following people: @mbroz2
- [ ] Agree with @mbroz2 which feature will lead this blog post, then write a title, slug, summary first paragraph, and SEO front matter appropriately.
- [ ] Get the post approved by @mbroz2.
- [ ] On release day (usually a Friday) @mbroz2 will publish the post.

## All done?

Check that you've completed every task above. Select each check box to confirm that you have before closing this issue.
