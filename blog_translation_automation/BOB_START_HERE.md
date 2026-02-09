# 🤖 IBM BOB - START HERE

## Mission
Translate a specific English blog post from `posts/` directory to Japanese, placing the translation in `posts/ja/` directory with the SAME filename.

## 🎯 Filename-Specific Translation Task

### Input Parameter
You will receive a **filename** as input (e.g., `2026-01-27-26.0.0.1.adoc` or `2026-01-27-26.0.0.1`).

### Step-by-Step Process

#### Step 1: Find the Source File
1. Look in the `posts/` directory
2. Find the file with the **exact filename** provided (with or without `.adoc` extension)
3. This is your source file to translate

**Example:**
- Input filename: `2026-01-27-26.0.0.1.adoc` or `2026-01-27-26.0.0.1`
- Find file: `posts/2026-01-27-26.0.0.1.adoc` ✅

#### Step 2: Translate the File
1. Read the source file completely
2. Apply all translation guidelines from documentation
3. Translate English content to Japanese
4. Preserve all code, markup, and formatting exactly

#### Step 3: Save the Translation
1. Save the translated file to `posts/ja/` directory
2. Use the **EXACT SAME filename** as the source file
3. Example: `posts/2026-01-27-26.0.0.1.adoc` → `posts/ja/2026-01-27-26.0.0.1.adoc`

### File Location Pattern

```
Source:      posts/{FILENAME}.adoc
Translation: posts/ja/{FILENAME}.adoc
                     ↑
                     Same filename!
```

**Examples:**
```
posts/2026-01-27-26.0.0.1.adoc  →  posts/ja/2026-01-27-26.0.0.1.adoc
posts/2025-12-02-25.0.0.12.adoc →  posts/ja/2025-12-02-25.0.0.12.adoc
posts/2025-11-04-25.0.0.11.adoc →  posts/ja/2025-11-04-25.0.0.11.adoc
posts/2024-12-16-jblog-two-year-celebration.adoc → posts/ja/2024-12-16-jblog-two-year-celebration.adoc
```

## 📖 Required Reading Order

### 1. FIRST: Read This File Completely
You are here! This file provides the roadmap.

### 2. SECOND: Read IBM_BOB_INTEGRATION_SUMMARY.md
**Location**: `blog_translation_automation/IBM_BOB_INTEGRATION_SUMMARY.md`
- Quick-start guide with core principles
- Comprehensive translation rules
- Key translation patterns in tables
- Critical DO/DON'T rules
- Quality validation checklist

### 3. THIRD: Study TRANSLATION_EXAMPLES.md
**Location**: `blog_translation_automation/TRANSLATION_EXAMPLES.md`
- Concrete before/after examples
- Front matter transformations
- Section-by-section examples
- Common patterns demonstrated

### 4. FOURTH: Compare Example Files
**Locations**:
- English: `blog_translation_automation/translation_examples/eng/*.adoc`
- Japanese: `blog_translation_automation/translation_examples/ja/*.adoc`

Compare these side-by-side to see real translations in context.

## 📝 Translation Task Details

### Input
- **Filename** (provided as environment variable or parameter, with or without `.adoc` extension)
- English blog post in `posts/` directory with exact filename
- File format: `.adoc` (AsciiDoc)

### Output
- Japanese translation in `posts/ja/` directory
- **EXACT SAME filename** as the source file
- Maintain exact formatting and structure

### Finding the Correct File

**Search Pattern:**
1. Receive filename input (with or without `.adoc` extension)
2. Add `.adoc` extension if not present
3. Look for exact file in `posts/` directory
4. This is your source file

**Command Example (for reference):**
```bash
# If filename is 2026-01-27-26.0.0.1 or 2026-01-27-26.0.0.1.adoc
# Look for: posts/2026-01-27-26.0.0.1.adoc
```

### Translation Requirements

## 🚨 CRITICAL TRANSLATION GUIDELINES

### ✅ What to Translate

#### YAML Front Matter:
- **Title** and all descriptions (seo-title, seo-description, blog_description)
- Translate naturally while maintaining meaning

#### Body Content:
- **All body text and headings** - Use formal technical Japanese (です・ます体)
- **Image alt text** - Example: "Ask a question on Stack Overflow" → "Stack Overflow で質問する"
- **Link display text** - Translate the text shown, NOT the URL

### ❌ What NOT to Translate

#### YAML Front Matter:
- **YAML keys** - Keep as-is: layout, categories, author_picture, author_github, etc.
- **URLs and links** - All URLs remain in English
- **GitHub usernames** - Keep original usernames

#### Body Content:
- **Code blocks** - ALL code must remain exactly as-is
- **Technical commands** - bash, XML, properties commands unchanged
- **AsciiDoc markup syntax** - [source,xml], ----, +, *, etc.
- **Technical product names** - Open Liberty, WebSphere, Jakarta EE, Maven, Gradle, Docker
- **Version numbers** - 26.0.0.1, 25.0.0.12, etc.
- **File paths** - pom.xml, server.xml, build.gradle, etc.
- **Comments** - Especially GHA-BLOG-TOPIC blocks

### 🔧 Special Handling Requirements

#### 1. Language Links (CRITICAL)
Update `blog-available-in-languages` section to point to English version:

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

#### 2. Translator Credit (REQUIRED)
Add `additional_authors` section with translator information:

```yaml
additional_authors:
- name: 高宮 裕子 (翻訳)
  github: https://github.com/HirokoTakamiya
  image: https://avatars.githubusercontent.com/HirokoTakamiya
```

Or use IBM BOB as translator:
```yaml
additional_authors:
- name: IBM BOB (翻訳)
  github: https://github.com/IBM
  image: https://avatars.githubusercontent.com/IBM
```

#### 3. Image References (REQUIRED)
Change Stack Overflow button image reference:
- **English**: `blog_btn_stack.svg`
- **Japanese**: `blog_btn_stack_ja.svg`

Example:
```asciidoc
# English
image::img/blog/blog_btn_stack.svg[Ask a question on Stack Overflow, align="center"]

# Japanese
image::img/blog/blog_btn_stack_ja.svg[Stack Overflow で質問する, align="center"]
```

### ✅ Additional MUST DO Rules
1. Use **formal technical Japanese** (です・ます体) throughout
2. Preserve ALL code blocks exactly (no changes)
3. Preserve ALL AsciiDoc markup exactly
4. Preserve ALL comments (especially GHA-BLOG-TOPIC blocks)
5. Translate text naturally while maintaining technical accuracy
6. Follow established terminology patterns from examples

### ❌ Additional MUST NOT DO Rules
1. Do NOT translate code blocks
2. Do NOT modify AsciiDoc syntax
3. Do NOT change URLs or file paths
4. Do NOT translate comments
5. Do NOT remove or alter markup
6. Do NOT use casual Japanese
7. Do NOT translate YAML keys
8. Do NOT translate product names or version numbers

## 📋 Translation Workflow

### Step 1: Preparation
```
1. Read IBM_BOB_INTEGRATION_SUMMARY.md for comprehensive rules
2. Study TRANSLATION_EXAMPLES.md for concrete patterns
3. Review example translations in eng/ and ja/ folders
```

### Step 2: Find and Translate the Specific Blog Post
```
1. Receive filename input (e.g., 2026-01-27-26.0.0.1.adoc or 2026-01-27-26.0.0.1)
2. Add .adoc extension if not present
3. Find exact file in posts/ directory
4. Read the matching English blog file
5. Identify sections to translate vs preserve
6. Apply translation patterns from documentation
7. Preserve all code and markup exactly
8. Update front matter appropriately
9. Add translator credit
10. Save to posts/ja/ with EXACT SAME filename
```

**Example Workflow:**
```
Input: filename = "2026-01-27-26.0.0.1.adoc" (or "2026-01-27-26.0.0.1")
  ↓
Find: posts/2026-01-27-26.0.0.1.adoc
  ↓
Translate: Apply all guidelines
  ↓
Save: posts/ja/2026-01-27-26.0.0.1.adoc
```

### Step 3: Quality Check
```
□ Front matter correctly translated
□ All code blocks unchanged
□ All AsciiDoc syntax intact
□ All comments preserved
□ Technical terms consistent
□ Japanese reads naturally
□ Image references updated
□ Translator credit added
```

## 🔑 Quick Reference

### Technical Terms
- **Keep in English**: Open Liberty, Maven, Gradle, Docker, file names, commands
- **Use Katakana**: サーバー (server), クライアント (client), キー (key)
- **Translate**: 機能 (feature), バグ修正 (bug fixes), 設定 (configuration)

### Common Phrases
- "In this release" → "このリリースでは"
- "If you're using" → "もし...を使用しているなら"
- "Check out" → "チェックして下さい"
- "Get Open Liberty X.X.X now" → "今すぐ Open Liberty X.X.X を入手する"

### Front Matter Changes
```yaml
# English version has:
blog-available-in-languages:
- lang: ja
  path: /ja/blog/2026/01/27/26.0.0.1.html

# Japanese version should have:
blog-available-in-languages:
- lang: en
  path: /blog/2026/01/27/26.0.0.1.html
additional_authors:
- name: IBM BOB (翻訳)
  github: https://github.com/IBM
  image: https://avatars.githubusercontent.com/IBM
```

### Code Block Example
```asciidoc
# This NEVER changes - preserve exactly:
[source,xml]
----
<logging throttleMaxMessagesPerWindow="5000" />
----
```

## 🚨 Critical Reminders

1. **Formal Japanese Only**: Always use です・ます form
2. **Code is Sacred**: Never modify code blocks
3. **Markup is Sacred**: Never modify AsciiDoc syntax
4. **Comments are Sacred**: Never translate or modify comments
5. **Natural Translation**: Don't translate word-for-word, make it natural Japanese
6. **Consistency**: Use same translations for same terms throughout

## 📊 Success Criteria

Your translation is successful when:
- ✅ Japanese reads naturally and professionally
- ✅ Technical accuracy is maintained
- ✅ All code and markup preserved exactly
- ✅ Follows patterns from example translations
- ✅ Front matter correctly updated
- ✅ Passes quality checklist

## 🆘 If You're Unsure

1. Check IBM_BOB_INTEGRATION_SUMMARY.md for rules
2. Check TRANSLATION_EXAMPLES.md for patterns
3. Compare with example files in eng/ and ja/
4. When in doubt, preserve the original format

## 📁 File Structure Reference

```
Blog_Personal/
├── posts/                              # English blogs (source)
│   ├── 2026-01-27-26.0.0.1.adoc
│   ├── 2025-12-02-25.0.0.12.adoc
│   └── ...
├── posts/ja/                           # Japanese blogs (your output)
│   ├── 2026-01-27-26.0.0.1.adoc
│   ├── 2025-12-02-25.0.0.12.adoc
│   └── ...
└── blog_translation_automation/        # Translation automation system
    ├── BOB_START_HERE.md              # ← You are here
    ├── IBM_BOB_INTEGRATION_SUMMARY.md # Comprehensive guidelines
    ├── TRANSLATION_EXAMPLES.md        # Translation patterns
    ├── README.md                      # Documentation overview
    └── translation_examples/          # Example translations
        ├── eng/                       # Example English blogs
        └── ja/                        # Example Japanese translations
```

## 🎓 Learning Path Summary

```
1. Read BOB_START_HERE.md (this file)
   ↓
2. Read IBM_BOB_INTEGRATION_SUMMARY.md (comprehensive rules & quick reference)
   ↓
3. Study TRANSLATION_EXAMPLES.md (concrete examples)
   ↓
4. Compare eng/ and ja/ example files
   ↓
5. Start translating posts/ to posts/ja/
   ↓
6. Validate each translation with quality checklist
```

## ✨ You're Ready!

After reading all the documentation files, you'll understand:
- Translation style and tone
- Technical term handling
- Formatting preservation
- Common patterns and phrases
- Quality standards

Now proceed to read the documentation files in order and begin translating!

---

**Remember**: Quality over speed. Each translation should be professional, accurate, and maintain the exact formatting of the original.