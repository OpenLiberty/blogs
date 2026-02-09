# Translation Examples - English to Japanese

This document provides concrete examples of translation patterns extracted from the blog_translation_automation folder.

## Front Matter Examples

### Example 1: Version Release Blog

**English:**
```yaml
---
layout: post
title: "Log throttling and notable bug fixes in 26.0.0.1"
categories: blog
author_picture: https://avatars3.githubusercontent.com/navaneethsnair1
author_github: https://github.com/navaneethsnair1
seo-title: Log throttling and notable bug fixes in 26.0.0.1- OpenLiberty.io
seo-description: In this release, Open Liberty introduces log throttling to automatically suppress excessive, repeated log messages, helping developers reduce noise and manage high-volume logging more effectively.
blog_description: In this release, Open Liberty introduces log throttling to automatically suppress excessive, repeated log messages, helping developers reduce noise and manage high-volume logging more effectively.
open-graph-image: https://openliberty.io/img/twitter_card.jpg
open-graph-image-alt: Open Liberty Logo
blog-available-in-languages:
- lang: ja
  path: /ja/blog/2026/01/27/26.0.0.1.html
---
```

**Japanese:**
```yaml
---
layout: post
title: "26.0.0.1 でのログ抑制と注目すべきバグ修正"
categories: blog
author_picture: https://avatars3.githubusercontent.com/navaneethsnair1
author_github: https://github.com/navaneethsnair1
seo-title: 26.0.0.1 でのログ抑制と注目すべきバグ修正 - OpenLiberty.io
seo-description: このリリースでは、Open Liberty にログ抑制機能が導入され、過度に繰り返されるログメッセージを自動的に抑制することで、開発者がノイズを削減し、大量のログをより効果的に管理できるようになりました。
blog_description: このリリースでは、Open Liberty にログ抑制機能が導入され、過度に繰り返されるログメッセージを自動的に抑制することで、開発者がノイズを削減し、大量のログをより効果的に管理できるようになりました。
open-graph-image: https://openliberty.io/img/twitter_card.jpg
open-graph-image-alt: Open Liberty Logo
blog-available-in-languages:
- lang: en
  path: /blog/2026/01/27/26.0.0.1.html
additional_authors:
- name: 馬場 剛 (校正)
  github: https://github.com/babatch
  image: https://avatars.githubusercontent.com/u/29302643
---
```

## Introduction Paragraphs

### Example 1: Feature Introduction
**English:**
"In this release, Open Liberty introduces log throttling to automatically suppress excessive, repeated log messages, helping developers reduce noise and manage high-volume logging more effectively."

**Japanese:**
"このリリースでは、Open Liberty にログ抑制機能が導入され、過度に繰り返されるログメッセージを自動的に抑制することで、開発者がノイズを削減し、大量のログをより効果的に管理できるようになりました。"

### Example 2: Multiple Features
**English:**
"This release introduces support for supplying your own Base64-encoded AES-256 key, removing the need for Liberty to derive a key during startup and resulting in faster and more efficient password encryption. It also adds FIPS 140-3 compliance when Liberty running with supported IBM Semeru Runtime versions (11.0.29, 17.0.17, 21.0.9, 25.0.1 or later)."

**Japanese:**
"このリリースでは、独自の Base64 エンコードされた AES-256 キーを提供するサポートが導入され、起動時に Liberty がキーを導出する必要がなくなり、より高速で効率的なパスワード暗号化が実現されます。また、サポートされている IBM Semeru Runtime バージョン（11.0.29、17.0.17、21.0.9、25.0.1 以降）で Liberty を実行する際の FIPS 140-3 準拠が追加されます。"

## Section Headers

### Example 1: Development Section
**English:**
"== Develop and run your apps using 25.0.0.12"

**Japanese:**
"== 25.0.0.12 でアプリを開発して実行する"

### Example 2: Feature Section
**English:**
"== Log Throttling"

**Japanese:**
"== ログ抑制"

### Example 3: Bug Fixes Section
**English:**
"== Notable bugs fixed in this release"

**Japanese:**
"== このリリースで修正された注目すべきバグ"

## Installation Instructions

### Maven Example
**English:**
```asciidoc
If you're using link:{url-prefix}/guides/maven-intro.html[Maven], include the following in your `pom.xml` file:

[source,xml]
----
<plugin>
    <groupId>io.openliberty.tools</groupId>
    <artifactId>liberty-maven-plugin</artifactId>
    <version>3.11.5</version>
</plugin>
----
```

**Japanese:**
```asciidoc
もし link:{url-prefix}/guides/maven-intro.html[Maven] を使用しているなら、`pom.xml` に以下を含めます。

[source,xml]
----
<plugin>
    <groupId>io.openliberty.tools</groupId>
    <artifactId>liberty-maven-plugin</artifactId>
    <version>3.11.5</version>
</plugin>
----
```

### Gradle Example
**English:**
"Or for link:{url-prefix}/guides/gradle-intro.html[Gradle], include the following in your `build.gradle` file:"

**Japanese:**
"link:{url-prefix}/guides/gradle-intro.html[Gradle] を使用している場合は、`build.gradle` ファイルに以下を含めます。"

### Container Images
**English:**
"Or if you're using link:{url-prefix}/docs/latest/container-images.html[container images]:"

**Japanese:**
"link:{url-prefix}/docs/latest/container-images.html[コンテナ・イメージ] を使用する場合は以下です。"

## Technical Feature Descriptions

### Example 1: Log Throttling
**English:**
"Open Liberty Logging is introducing log throttling. Developers previously had no way to throttle or suppress high-volume messages. This new feature helps to prevent excessive log output when the same log events occur repeatedly within a short span of time."

**Japanese:**
"Open Liberty のロギング機能にログ抑制が導入されました。これまで開発者には、大量のメッセージを抑制する方法がありませんでした。この新機能は、同じログイベントが短時間に繰り返し発生した場合に、過度なログ出力を防ぐのに役立ちます。"

### Example 2: Default Behavior
**English:**
"Throttling is enabled by default. While enabled, Liberty tracks each messageID using a sliding window. By default, any messageID that is repeated more than 1,000 times within a five-minute interval is suppressed. A throttle warning is logged when throttling begins."

**Japanese:**
"抑制機能はデフォルトで有効になっています。有効にすると、Liberty はスライディングウィンドウを使用して各 messageID を追跡します。デフォルトでは、5 分間に 1,000 回以上繰り返される messageID は抑制されます。抑制が開始されると、抑制警告がログに記録されます。"

## Configuration Examples

### Example 1: XML Configuration
**English:**
```asciidoc
* In `server.xml`:
+
[source,xml]
----
<logging throttleMaxMessagesPerWindow="5000" throttleType="messageID" />
----
```

**Japanese:**
```asciidoc
* `server.xml` の場合:
+
[source,xml]
----
<logging throttleMaxMessagesPerWindow="5000" throttleType="messageID" />
----
```

### Example 2: Properties Configuration
**English:**
```asciidoc
* In `bootstrap.properties`:
+
[source,properties]
----
com.ibm.ws.logging.throttle.max.messages.per.window=5000
com.ibm.ws.logging.throttle.type=messageID
----
```

**Japanese:**
```asciidoc
* `bootstrap.properties` の場合:
+
[source,properties]
----
com.ibm.ws.logging.throttle.max.messages.per.window=5000
com.ibm.ws.logging.throttle.type=messageID
----
```

## Bug Descriptions

### Example 1: Simple Bug
**English:**
"* link:https://github.com/OpenLiberty/open-liberty/issues/33098[`appsWriteJSON` not working correctly when JSON record ends with new line.]"

**Japanese:**
"* link:https://github.com/OpenLiberty/open-liberty/issues/33098[JSON レコードが改行で終わる場合に `appsWriteJSON` が正しく動作しない]"

### Example 2: Bug with Detailed Description
**English:**
```asciidoc
* link:https://github.com/OpenLiberty/open-liberty/issues/32999[Fix the exception in multipart data asynchronous call]
+
Sending multipart/form-data with MicorProfileRestClient asynchronous results in below exception.
+
`java.util.concurrent.CompletionException: jakarta.ws.rs.ProcessingException: RESTEASY004655: Unable to invoke request: jakarta.ws.rs.WebApplicationException: Unexpected entity instance: org.jboss.resteasy.plugins.providers.multipart.ResteasyEntityPartBuilder$EntityPartImpl`
```

**Japanese:**
```asciidoc
* link:https://github.com/OpenLiberty/open-liberty/issues/32999[マルチパート・データの非同期呼び出しにおける例外を修正]
+
MicroProfileRestClient の非同期で multipart/form-data を送信すると、以下の例外が発生します。
+
`java.util.concurrent.CompletionException: jakarta.ws.rs.ProcessingException: RESTEASY004655: Unable to invoke request: jakarta.ws.rs.WebApplicationException: Unexpected entity instance: org.jboss.resteasy.plugins.providers.multipart.ResteasyEntityPartBuilder$EntityPartImpl`
```

## Command Examples

### Example 1: Basic Command
**English:**
"To enable across all servers, clients and tools, you can enable FIPS 140-3 at the Install level by running:"
```
securityUtility configureFIPS
```

**Japanese:**
"すべてのサーバー、クライアント、およびツール全体で有効にするには、以下を実行して Install レベルで FIPS 140-3 を有効にできます："
```
securityUtility configureFIPS
```

### Example 2: Command with Options
**English:**
"To generate a 256-bit AES key using `securityUtility`, run the new `securityUtility generateAESKey` task to:"
"* Generate a random AES key:"
```bash
./securityUtility generateAESKey
```

**Japanese:**
"`securityUtility` を使用して 256 ビット AES キーを生成するには、新しい `securityUtility generateAESKey` タスクを実行します："
"* ランダムな AES キーを生成する："
```bash
./securityUtility generateAESKey
```

## Closing Sections

### Example 1: Get Liberty Now
**English:**
"== Get Open Liberty 26.0.0.1 now"
"Available through <<run,Maven, Gradle, Docker, and as a downloadable archive>>."

**Japanese:**
"== Open Liberty 26.0.0.1 を今すぐ入手"
"<<run,Maven、Gradle、Docker、およびダウンロード可能なアーカイブ>> から入手できます。"

### Example 2: Alternative Format
**English:**
"== Get Open Liberty 25.0.0.11 now"
"Available through <<run,Maven, Gradle, Docker, and as a downloadable archive>>."

**Japanese:**
"== 今すぐ Open Liberty 25.0.0.11 を入手する"
"<<run,Maven, Gradle, Docker, そしてダウンロード可能なアーカイブ>> から可能です。"

## Link Translations

### Example 1: Previous Releases
**English:**
"Check out link:{url-prefix}/blog/?search=release&search!=beta[previous Open Liberty GA release blog posts]."

**Japanese:**
"link:{url-prefix}/blog/?search=release&search!=beta[以前の Open Liberty GA リリースのブログ投稿] もチェックして下さい。"

### Example 2: Bug List
**English:**
"View the list of fixed bugs in link:https://github.com/OpenLiberty/open-liberty/issues?q=label%3Arelease%3A26001+label%3A%22release+bug%22[26.0.0.1]."

**Japanese:**
"26.0.0.1 で修正されたバグのリストは link:https://github.com/OpenLiberty/open-liberty/issues?q=label%3Arelease%3A26001+label%3A%22release+bug%22[こちら] です。"

## Image References

### Stack Overflow Button
**English:**
```asciidoc
[link=https://stackoverflow.com/tags/open-liberty]
image::img/blog/blog_btn_stack.svg[Ask a question on Stack Overflow, align="center"]
```

**Japanese:**
```asciidoc
[link=https://stackoverflow.com/tags/open-liberty]
image::img/blog/blog_btn_stack_ja.svg[Stack Overflow で質問する, align="center"]
```

Note: The image file changes from `blog_btn_stack.svg` to `blog_btn_stack_ja.svg`.