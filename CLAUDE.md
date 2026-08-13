# NOMAD - Nextgen Optimized Mobile Application Development

## Project Overview

NOMAD is a knowledge base and framework containing best practices, components, and solutions for modern mobile application development. It provides end-to-end guidance from concept to release and maintenance.

This is a **documentation/knowledge project**, not a code project. Content lives primarily in Markdown files.

## Project Structure

```
NOMAD/
├── README.md                  # Project overview and index
├── KnowledgeBase/             # All knowledge base content
│   ├── Requirements/          # Requirements engineering practices
│   └── ...                    # Additional topic directories
└── CLAUDE.md                  # This file
```

## Content Guidelines

- **Platform agnostic**: Content should apply broadly to mobile development, not be tied to a specific framework. Platform-specific implementations belong in separate repos (e.g., NOMAD.Maui).
- **Practical over theoretical**: Favor actionable guidance, concrete examples, and real-world patterns.
- **Opinionated**: The framework provides clear recommendations rather than exhaustive comparisons of every option.
- **AI-assisted development**: Content should consider AI tooling as a first-class concern in the development process.
- **Cross-platform focus**: Prefer solutions that minimize effort across platforms.

## Core Principles (from README)

1. Do NOT reinvent the wheel
2. Find good and easy-to-integrate solutions to common mobile app problems
3. Minimize effort for setup, implementation, and maintenance
4. AI-assisted development at every stage
5. Cross-platform first to minimize time and effort

## Knowledge Base Topics

- Process best practices (requirements, planning, workflow)
- Common mobile feature implementations (error logging, version management, etc.)
- Tool selection and evaluation
- Testing strategies for mobile apps

## Two Kinds of Prose

NOMAD publishes guides and articles, and they have different jobs:

- **Knowledge base guide** — the *what* and *how*. Numbered sections, tables, rules. Read by lookup, repeatedly.
- **Article** — the *why*. The reasoning behind a decision, what was rejected, what it cost. Read once, start to finish.

They cross-reference rather than repeat, preserving one canonical source per topic: the rule lives in the guide, the argument for it lives in the article. See the `nomad-technical-writer` skill.

## Writing Style

- Use clear, structured Markdown
- Feature-based organization (features over screens, as defined in requirements best practices)
- One canonical source of truth per topic — avoid duplicating information across files
- Keep documents well-structured with headers, tables, and lists for scannability
- Structure prevents bloat; duplication causes it

## When Editing Content

- Read existing files before proposing changes to understand current structure and conventions
- Follow the existing naming patterns and directory structure
- Cross-reference related topics rather than duplicating content
- Update the README index when adding new sections or documents
