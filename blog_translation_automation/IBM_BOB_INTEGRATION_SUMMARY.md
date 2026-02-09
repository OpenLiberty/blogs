# IBM BOB Integration Summary - Blog Translation Learning

## Quick Start for IBM BOB

This document provides a concise summary of what IBM BOB needs to learn from the blog_examples folder to translate English Open Liberty blogs to Japanese.

## 🎯 Filename-Specific Translation Task

### Input
You will receive a **filename** (e.g., `2026-01-27-26.0.0.1.adoc` or `2026-01-27-26.0.0.1`) as input.

### Process
1. **Find**: Locate exact file in `posts/` directory (add `.adoc` if not present)
2. **Translate**: Apply all translation guidelines
3. **Save**: Save to `posts/ja/` with the **SAME filename**

### Example
```
Input filename: 2026-01-27-26.0.0.1.adoc (or 2026-01-27-26.0.0.1)
  ↓
Find: posts/2026-01-27-26.0.0.1.adoc
  ↓
Translate: (apply all guidelines)
  ↓
Save: posts/ja/2026-01-27-26.0.0.1.adoc
```

**Critical**: The output filename MUST be exactly the same as the input filename!

## 📚 Learning Resources

1. **IBM_BOB_INTEGRATION_SUMMARY.md** (this file) - Comprehensive rules and patterns
2. **TRANSLATION_EXAMPLES.md** - Specific before/after examples
3. **eng/** folder - English source blogs
4. **ja/** folder - Japanese translated blogs
5. **README.md** - Overview and usage instructions

## 🎯 Core Translation Principles

### 1. Translation Style
- **Formal Technical Japanese** (です・ます体)
- Professional, clear, and precise
- Natural Japanese flow while maintaining technical accuracy

### 2. What to Translate (CRITICAL)

#### YAML Front Matter:
```
✅ Title (translate naturally)
✅ seo-title (translate + add " - OpenLiberty.io")
✅ seo-description (full translation)
✅ blog_description (same as seo-description)
```

#### Body Content:
```
✅ All body text and headings (formal Japanese です・ます体)
✅ Image alt text (e.g., "Ask a question" → "質問する")
✅ Link display text (NOT the URLs)
✅ Section headers
✅ List item descriptions
✅ Explanatory paragraphs
```

### 3. What NOT to Translate (CRITICAL)

#### YAML Front Matter:
```
❌ YAML keys (layout, categories, author_picture, etc.)
❌ URLs and links
❌ GitHub usernames
```

#### Body Content:
```
❌ Code blocks (XML, bash, properties, Java, etc.)
❌ Technical commands
❌ AsciiDoc markup ([source,xml], ----, +, *, etc.)
❌ Technical product names (Open Liberty, WebSphere, Jakarta EE, Maven, Gradle, Docker)
❌ Version numbers (26.0.0.1, 25.0.0.12, etc.)
❌ File paths (pom.xml, server.xml, build.gradle, etc.)
❌ Comments (especially GHA-BLOG-TOPIC blocks)
❌ Error messages and stack traces
```

### 4. Special Handling (REQUIRED)

#### A. Language Links (CRITICAL)
**English version has:**
```yaml
blog-available-in-languages:
- lang: ja
  path: /ja/blog/2026/01/27/26.0.0.1.html
```

**Japanese version MUST have:**
```yaml
blog-available-in-languages:
- lang: en
  path: /blog/2026/01/27/26.0.0.1.html
```

#### B. Translator Credit (REQUIRED)
Add `additional_authors` section with the translator information provided in the workflow:

**The workflow will provide these environment variables:**
- `TRANSLATOR_NAME` - GitHub username of the person who triggered the workflow
- `TRANSLATOR_GITHUB` - GitHub profile URL of the translator

**Use this format:**
```yaml
additional_authors:
- name: [TRANSLATOR_NAME] (翻訳)
  github: [TRANSLATOR_GITHUB]
  image: [TRANSLATOR_GITHUB]/avatar
```

**Example (if translator is "ismathbadsha"):**
```yaml
additional_authors:
- name: ismathbadsha (翻訳)
  github: https://github.com/ismathbadsha
  image: https://avatars.githubusercontent.com/ismathbadsha
```

**IMPORTANT:** Always use the `TRANSLATOR_NAME` and `TRANSLATOR_GITHUB` environment variables provided by the workflow. Do NOT hardcode "IBM BOB" or any other name.

#### C. Image References (REQUIRED)
Change Stack Overflow button:
- English: `blog_btn_stack.svg`
- Japanese: `blog_btn_stack_ja.svg`

Example:
```asciidoc
# English
image::img/blog/blog_btn_stack.svg[Ask a question on Stack Overflow, align="center"]

# Japanese
image::img/blog/blog_btn_stack_ja.svg[Stack Overflow で質問する, align="center"]
```

## 🔑 Key Translation Patterns

### Technical Terms

| Category | Action | Examples |
|----------|--------|----------|
| **Keep in English** | Product names, features, files, commands | Open Liberty, Maven, `pom.xml`, `securityUtility` |
| **Use Katakana** | Generic tech terms | サーバー (server), クライアント (client), キー (key) |
| **Translate to Japanese** | Common concepts | 機能 (feature), バグ修正 (bug fixes), 設定 (configuration) |

### Common Phrases

| English | Japanese |
|---------|----------|
| "In this release" | "このリリースでは" |
| "If you're using" | "もし...を使用しているなら" |
| "Check out" | "チェックして下さい" |
| "Get Open Liberty X.X.X now" | "今すぐ Open Liberty X.X.X を入手する" |
| "Available through" | "...から入手できます" |

### Version Context
```
"in 26.0.0.1" → "26.0.0.1 での"
"in 26.0.0.1" → "26.0.0.1 における"
```

## 📋 Front Matter Checklist

When translating front matter:

```yaml
# English → Japanese transformations:
✅ Translate title descriptively
✅ Translate seo-title + add " - OpenLiberty.io"
✅ Translate seo-description (full translation)
✅ Translate blog_description (same as seo-description)
✅ Swap blog-available-in-languages (ja → en, update path)
✅ Add additional_authors with translator credit
✅ Keep all other fields unchanged
```

## 🎨 Formatting Rules

### Code Blocks
```asciidoc
# NEVER change code content
[source,xml]
----
<logging throttleMaxMessagesPerWindow="5000" />
----
```

### Configuration Examples
```asciidoc
# English
* In `server.xml`:

# Japanese
* `server.xml` の場合:
```

### Links
```asciidoc
# Translate display text only
link:{url-prefix}/start/[Downloads page]
→ link:{url-prefix}/start/[ダウンロード・ページ]
```

### Images
```asciidoc
# Update to Japanese image variant
image::img/blog/blog_btn_stack.svg[Ask a question, align="center"]
→ image::img/blog/blog_btn_stack_ja.svg[質問する, align="center"]
```

## 🔍 Example Comparison

### Before (English)
```asciidoc
== Log Throttling

Open Liberty Logging is introducing log throttling. This new feature helps to prevent excessive log output.

* In `server.xml`:
+
[source,xml]
----
<logging throttleMaxMessagesPerWindow="5000" />
----
```

### After (Japanese)
```asciidoc
== ログ抑制

Open Liberty のロギング機能にログ抑制が導入されました。この新機能は、過度なログ出力を防ぐのに役立ちます。

* `server.xml` の場合:
+
[source,xml]
----
<logging throttleMaxMessagesPerWindow="5000" />
----
```

## ⚠️ Critical Rules

### DO NOT:
- ❌ Translate code blocks
- ❌ Modify AsciiDoc syntax
- ❌ Change URLs or file paths
- ❌ Translate comments
- ❌ Remove or alter markup

### ALWAYS:
- ✅ Use formal Japanese (です・ます)
- ✅ Preserve all formatting
- ✅ Maintain technical accuracy
- ✅ Keep natural Japanese flow
- ✅ Add translator credit

## 📊 Quality Validation

Before finalizing translation, verify:

```
□ Front matter correctly translated
□ All code blocks unchanged
□ All links functional
□ Technical terms consistent
□ AsciiDoc syntax intact
□ Comments preserved
□ Japanese reads naturally
□ Image references updated (_ja.svg)
□ Translator credit added
```

## 🚀 Integration Steps for IBM BOB

### 1. Pre-Translation Phase
```
□ Receive filename input (e.g., 2026-01-27-26.0.0.1.adoc or 2026-01-27-26.0.0.1)
□ Read IBM_BOB_INTEGRATION_SUMMARY.md (this file)
□ Study TRANSLATION_EXAMPLES.md
□ Compare eng/ and ja/ examples side-by-side
```

### 2. File Location Phase
```
□ Add .adoc extension if not present in input
□ Locate exact file in posts/ directory
□ Identify the correct source file
□ Note the exact filename for output
```

### 3. Translation Phase
```
□ Read the source file completely
□ Apply formal technical Japanese style
□ Preserve all code and markup exactly
□ Translate text naturally while maintaining accuracy
□ Follow established terminology patterns
□ Update front matter (language links, translator credit, images)
```

### 4. Post-Translation Phase
```
□ Validate against quality checklist
□ Ensure consistency with examples
□ Verify all formatting preserved
□ Save to posts/ja/ with EXACT SAME filename
```

### File Naming Examples
```
Source                                                    Output
posts/2026-01-27-26.0.0.1.adoc                        →  posts/ja/2026-01-27-26.0.0.1.adoc
posts/2025-12-02-25.0.0.12.adoc                       →  posts/ja/2025-12-02-25.0.0.12.adoc
posts/2025-11-04-25.0.0.11.adoc                       →  posts/ja/2025-11-04-25.0.0.11.adoc
posts/2024-12-16-jblog-two-year-celebration.adoc      →  posts/ja/2024-12-16-jblog-two-year-celebration.adoc
```

## 📖 Learning from Examples

### Example Files Available

1. **2026-01-27-26.0.0.1.adoc**
   - Feature introduction (log throttling)
   - Configuration examples
   - Bug fixes

2. **2025-12-02-25.0.0.12.adoc**
   - Complex technical features (AES-256, FIPS)
   - Security terminology
   - Command-line examples
   - CVE table

3. **2025-11-04-25.0.0.11.adoc**
   - Bug-fix-only release
   - Error descriptions
   - Simpler structure

### How to Learn

```
1. Open English file (translation_examples/eng/filename.adoc)
2. Open Japanese file (translation_examples/ja/filename.adoc)
3. Compare side-by-side
4. Identify patterns:
   - What changed?
   - What stayed the same?
   - How were technical terms handled?
   - How was sentence structure adapted?
```

## 🎓 Key Takeaways

1. **Style**: Formal technical Japanese throughout
2. **Preservation**: All code and markup stay exactly the same
3. **Translation**: Natural Japanese while maintaining technical precision
4. **Consistency**: Use established patterns for technical terms
5. **Quality**: Professional, accurate, and readable

## 📞 Support

For questions or clarifications:
- Review IBM_BOB_INTEGRATION_SUMMARY.md for detailed rules
- Check TRANSLATION_EXAMPLES.md for specific patterns
- Compare with existing translation_examples/eng/ and translation_examples/ja/ examples
- Consult translation team if needed

---

**Remember**: The goal is to produce Japanese translations that are technically accurate, professionally written, and maintain the exact formatting and code of the original English blogs.