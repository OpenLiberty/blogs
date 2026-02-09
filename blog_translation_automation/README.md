# Blog Translation Automation

This folder contains all documentation, guidelines, and example blog posts for the blog translation automation system. It helps IBM BOB understand the translation style, tone, and patterns used for Open Liberty blog translations.

## Folder Structure

```
blog_translation_automation/
├── translation_examples/         # Example blog translations
│   ├── eng/                      # English source blogs (examples)
│   │   ├── 2026-01-27-26.0.0.1.adoc
│   │   ├── 2025-12-02-25.0.0.12.adoc
│   │   └── 2025-11-04-25.0.0.11.adoc
│   └── ja/                       # Japanese translated blogs (examples)
│       ├── 2026-01-27-26.0.0.1.adoc
│       ├── 2025-12-02-25.0.0.12.adoc
│       └── 2025-11-04-25.0.0.11.adoc
├── BOB_START_HERE.md             # Start here - main guide for IBM BOB
├── IBM_BOB_INTEGRATION_SUMMARY.md # Comprehensive translation guidelines
├── TRANSLATION_EXAMPLES.md       # Specific translation examples
└── README.md                     # This file
```

## Purpose

These example files serve as reference material for IBM BOB to learn:

1. **Translation Style and Tone**: Formal technical Japanese (です・ます体)
2. **Technical Term Handling**: Which terms to keep in English, translate to katakana, or translate to Japanese
3. **Formatting Preservation**: How to maintain AsciiDoc markup, code blocks, and links
4. **Common Patterns**: Standard phrases and section header translations

## Example Blog Posts

### 1. 2026-01-27-26.0.0.1.adoc
**Topic**: Log throttling feature and bug fixes
**Key Learning Points**:
- Feature introduction translation
- Configuration examples (XML, properties, environment variables)
- Technical explanation of throttling behavior
- Bug fix descriptions

### 2. 2025-12-02-25.0.0.12.adoc
**Topic**: AES-256 key support and FIPS 140-3 compliance
**Key Learning Points**:
- Complex technical feature descriptions
- Security-related terminology
- Command-line examples with multiple options
- Detailed configuration instructions
- CVE table formatting

### 3. 2025-11-04-25.0.0.11.adoc
**Topic**: Bug fixes only release
**Key Learning Points**:
- Bug description translations
- Error message handling
- Issue link formatting
- Simpler structure for bug-fix-only releases

## How to Use These Examples

### For IBM BOB Integration

1. **Read BOB_START_HERE.md first** - This provides the roadmap and overview
2. **Read IBM_BOB_INTEGRATION_SUMMARY.md** - This provides comprehensive rules and patterns
3. **Study TRANSLATION_EXAMPLES.md** - This shows specific before/after examples
4. **Compare translation_examples/eng/ and translation_examples/ja/ files side-by-side** - See real translations in context
5. **Identify patterns**:
   - How technical terms are handled
   - How sentence structure changes
   - How formatting is preserved
   - How cultural adaptation is applied

### Key Observations

#### Translation Style
- **Formal and professional**: Uses です・ます form throughout
- **Technical precision**: Maintains exact technical meanings
- **Natural Japanese**: Not literal word-for-word translation
- **Consistent terminology**: Same terms translated the same way

#### What Gets Preserved Exactly
- All code blocks (XML, bash, properties, etc.)
- All AsciiDoc markup syntax
- All URLs and file paths
- All comments (including GHA-BLOG-TOPIC blocks)
- Version numbers and technical identifiers

#### What Gets Translated
- Titles and descriptions
- Explanatory text and paragraphs
- Section headers
- Link display text (but not URLs)
- Image alt text
- List items and bullet points

#### What Gets Adapted
- Image references (e.g., `blog_btn_stack.svg` → `blog_btn_stack_ja.svg`)
- Language links (swap `en` ↔ `ja`)
- Add translator credit in `additional_authors`

## Translation Quality Standards

Based on these examples, translations should:

1. ✅ Use formal technical Japanese consistently
2. ✅ Preserve all code and markup exactly
3. ✅ Maintain technical accuracy
4. ✅ Read naturally in Japanese
5. ✅ Follow established terminology patterns
6. ✅ Keep proper formatting and structure
7. ✅ Include translator attribution

## Common Translation Patterns

### Version Context
- "in X.X.X" → "X.X.X での" or "X.X.X における"

### Conditional Statements
- "If you're using..." → "もし...を使用しているなら"
- "Or for..." → "...を使用している場合は"

### Instructions
- "include the following" → "以下を含めます"
- "run the command" → "コマンドを実行します"

### References
- "Check out" → "チェックして下さい" or "ご覧ください"
- "For more information" → "詳細については"
- "See the documentation" → "ドキュメントを参照してください"

## Notes for Developers

When adding new example files:
1. Always include both English and Japanese versions
2. Ensure files have the same name in both folders
3. Choose examples that demonstrate different translation challenges
4. Update this README with new examples and their key learning points

## Integration with Translation Pipeline

These examples should be used by IBM BOB to:
1. Learn translation patterns before processing new blogs
2. Validate translation quality against established patterns
3. Ensure consistency across all translated content
4. Maintain the professional tone and technical accuracy expected

## Questions or Issues?

If you notice inconsistencies or have questions about translation patterns:
1. Review BOB_START_HERE.md for the main guide
2. Review IBM_BOB_INTEGRATION_SUMMARY.md for comprehensive rules
3. Compare with existing examples in translation_examples/eng/ and translation_examples/ja/ folders
4. Check TRANSLATION_EXAMPLES.md for specific patterns
5. Consult with the translation team for clarification