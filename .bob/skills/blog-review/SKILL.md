# Blog review skill

## Purpose

Review blogs being delivered to the https://github.com/OpenLiberty/blogs repository.

## Preliminary instructions

- Read [README.md](README.md) for instructions on creating/editing/reviewing posts.

## Blog types

- **General / Feature Post**: Technical deep dive, guide, tutorial, workshop announcement, or community update (single or multiple authors). Follows standard YAML frontmatter with author metadata, title, and descriptive sections with code samples. Follows the [post-multiple-authors.adoc](post-multiple-authors.adoc) or [post-single-author.adoc](post-single-author.adoc) template.
- **GA Release Post**: Open Liberty general availability release announcement (`YYYY-MM-DD-version.adoc`). Includes release summary, feature breakdown, `Develop and run your apps`, CVE fixes, bug fixes, and `Get Open Liberty [version] now` sections. Follows the [ga-release-post.adoc](ga-release-post.adoc) template.
- **Beta Release Post**: Open Liberty beta release announcement (`YYYY-MM-DD-version-beta.adoc`). Outlines upcoming beta features, trying features with Maven/Gradle/Docker, notable fixes, and a feedback link. Follows the [beta-release-post.adoc](beta-release-post.adoc) template.
- **Third-Party / Syndicated Post**: Short summary post linking to an externally hosted article via `redirect_link` and `permalink` frontmatter fields. Follows the [third-party-post.adoc](third-party-post.adoc) template.

## Instructions

- Ensure phrasing is grammatically correct. Flag anything with confusing wording.
- Ensure there are no syntax errors that could prevent the page from rendering correctly.
- Ensure the blog follows the expected structure/template.
- Verify all HTML anchors refer to existing anchors.
- Ensure code literals in backticks are consistent.
  - Flag when the following are in backticks:
    - Java version (e.g. `Java 27`)
- Sometimes PRs will have a link to a draft or staging site to preview the changes. Those links help show how the post actually renders on a website and are useful to follow and review for rendering purposes.
- Ensure the tags in [blog_tags.json](blog_tags.json) are updated correctly depending on the post type. Ensure formatting and syntax remain valid.
- Recommend that template comments and instructions be removed.

### DO NOT

- DO NOT attempt to change technical details.