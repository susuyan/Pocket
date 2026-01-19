# QWEN.md - Pocket SKILL Workspace

## Project Overview

**pocket** is a SKILL development workspace focused on creating and managing AI-powered content processing skills, particularly for link extraction, content summarization, and technical writing workflows. The repository serves as a centralized environment for developing, documenting, and deploying SKILL definitions that integrate with AI agents.

**Primary Purpose:** Develop and maintain "SKILL" definitions for content processing pipelines, with a current focus on the `link-extractor` skill for extracting and processing links from social media, technical news, and blog posts.

**Key Technologies & Tools:**
- **SKILL Framework:** Custom skill definitions with structured metadata
- **AI Agents:** Writing agents pipeline for content creation and review
- **Bash Scripting:** Automation for formatting and processing
- **Markdown:** Primary documentation format with specific conventions
- **AWK:** Text processing in automation scripts

## Directory Structure

```
pocket/
├── .claude/                  # Claude workspace configuration
│   └── agents/              # Agent configurations for Claude Code
├── .trae/                    # Trae workspace configuration
│   └── documents/
├── agents/                   # AI agent definitions and templates
│   └── writer.md            # Technical blog writing agent definition
├── docs/                     # Project documentation
│   ├── articles/            # Technical articles and summaries
│   └── daily-links/         # Daily link collections
├── examples/                 # Best practices and examples
├── scripts/                  # Automation scripts
│   └── format-daily-links.sh # Daily links formatter
├── skills/                   # SKILL implementations
│   └── link-extractor/       # Link extraction skill
└── *.md files               # Key project documentation
```

## Key Files & Documentation

### Core Documentation
1. **README.md** - Brief project overview: "专门来开发 SKILL 的"
2. **CLAUDE.md** - Guidance for Claude Code when working with this repository
3. **AGENTS.md** - Comprehensive documentation of writing agents pipeline
4. **mcp-practice-guide.md** - MCP practice guide (未读取)
5. **风格技术写作 agent 流水线 v1.0.md** - Technical writing agent pipeline (Chinese)
6. **examples/markdown-best-practices.md** - Detailed Markdown formatting guidelines

### Key Articles & Agent Definitions
- **docs/articles/agentic-workflow-summary.md** - Summary of agentic workflows and design patterns
- **agents/writer.md** - Technical blog writing agent focused on creating concise, practice-oriented technical content
- **AGENTS.md** - Architecture documentation of the full writing agents pipeline (reference only, actual files may be archived)

### Central Skills
- **skills/link-extractor/SKILL.md** - Primary link extraction skill definition
- **skills/link-extractor/references/** - Reference materials for link extraction workflows:
  - `categories.md` - Content classification and sections
  - `workflow.md` - Processing workflows
  - `decision-trees.md` - Extraction decision logic
  - `guide.md` - FAQ, best practices, validation checklist
  - `language-rules.md` - Language-specific guidelines
  - `edge-cases.md` - Boundary case handling
  - `examples.md` - Usage examples
  - `create-daily-links.md` - Daily links creation process
  - `daily-links-styles/` - Various output styling formats

## SKILL Development Framework

### Link Extractor Skill
**Purpose:** Extract and process links from social media (Weibo, X/Twitter, Reddit), technical news (Hacker News), and blog posts into structured Markdown entries for Daily Links documentation.

**Key Features:**
- **Smart Link Extraction:** Identifies platform → extracts content → expands short links → filters irrelevant resources
- **Output Styles:** Concept-style, Bullet-point summary, Official blog, GitHub repo, Icon single-line
- **Categories:** Six main content categories (Read This, Tools, Watch, Listen To, Play, Try)

**Usage:**
```bash
# Extract single link
link https://weibo.com/1648815335/Qn8iCfNyt

# Specify category
link https://cursor.com/cn/blog/agent-best-practices "Read This"

# Specify category and style
link https://github.com/pointfreeco/swift-composable-architecture "Tools" "GitHub Repo"
```

### Writing Agents Pipeline
**Three-Stage Workflow:**
```
Outline Designer → Writer → PO-Writer
     ↓              ↓          ↓
   Outline      Draft     Review/Approval
```

**Agent Responsibilities:**
1. **Outline Designer:** Research topics and create structured outlines with NFRs and constraints
2. **Writer:** Expand outlines into complete technical content focusing on "why" rather than "how"
3. **PO-Writer:** Quality gate reviewing style compliance, structure adherence, and content quality
4. **Analyst-Writer:** Research-heavy content synthesis from multiple sources

## Development Commands & Scripts

### Key Automation Scripts
**`scripts/format-daily-links.sh` - Daily Links Formatter**
```bash
# Format today's daily links file
scripts/format-daily-links.sh

# Format specific file
scripts/format-daily-links.sh docs/daily-links/2026-01-16.md
```

**Script Functionality:**
- Removes empty sections (only whitespace or horizontal rules)
- Normalizes blank lines (single blank lines between sections)
- Maintains header line if present
- Preserves section structure with separators
- Trims trailing whitespace

### No Build/Run Commands
This is not a traditional code project - no `package.json`, `requirements.txt`, or build configuration files exist. The workspace is focused on SKILL definitions, agent prompts, and documentation.

## Development Conventions & Guidelines

### Markdown Best Practices
Based on `examples/markdown-best-practices.md`, follow these conventions:

1. **Structure Over Decoration:**
   - Use `#` only for document titles
   - Use `##` for "problem-level" chapters
   - Use `###` for "solution/detail-level" sections
   - Limit lists to two levels

2. **Format for Diff and Tools:**
   - Keep semantically complete sentences on one line
   - Control empty lines intentionally (paragraphs, titles, lists)
   - Use stable, task-oriented headings

3. **New Markdown Paradigms:**
   - `Agent.md`: Describe Agent behavior and boundaries
   - `Claude.md`: Model-specific usage guidelines
   - `AGENTS.md`: System role and tool directory
   - `SKILL.md`: Markdown as "soft DSL" with YAML front matter

### Git Guidelines (from CLAUDE.md)
- **No commits** unless explicitly requested
- All changes must be thoroughly reviewed before committing
- Ensure clean git state (no uncommitted changes) when working

### File Organization Conventions
- **Daily links:** `docs/daily-links/YYYY-MM-DD.md` format
- **Markdown structure:** Level-2 headings (##) for link categories
- **Section separators:** Horizontal rules (---) between sections
- **Empty section handling:** Automatically removed by formatting script

## Project-Specific Patterns

### SKILL Definition Format
SKILL files use YAML front matter with structured metadata:
```yaml
---
name: skill-name
description: Skill description
license: Apache-2.0
metadata:
  author: pocket
  version: "2.0"
  updated: "2026-01-16"
---
```

### References System
Each SKILL includes a `references/` directory with:
- `categories.md` - Content classification and sections
- `workflow.md` - Processing workflows
- `decision-trees.md` - Extraction decision logic
- `guide.md` - FAQ, best practices, validation checklist
- `language-rules.md` - Language-specific guidelines
- `edge-cases.md` - Boundary case handling
- `examples.md` - Usage examples
- `create-daily-links.md` - Daily links creation process
- `daily-links-styles/` - Various output styling formats

### Writing Agent Templates
Located in `agents/writing-agents/templates/`:
- **onev-style-outline.md** - Template for OneV-style technical writing outlines

## Workflow Patterns

### Link Processing Workflow
1. **Daily collection** of links from various sources
2. **Batch extraction** using link-extractor skill
3. **Archiving to Daily Links** with appropriate categorization
4. **Regular review and optimization** of processing rules

### Content Creation Workflow
1. **Always start with Outline Designer** for structured thinking and clear constraints
2. **Use Writer** to expand outline into complete content
3. **Apply PO-Writer** as quality gate before publication
4. **Iterate if needed** with specific feedback to Writer if rejected
5. **Maintain conversation flow** - keep original outline and previous outputs in context

## Project Philosophy

This workspace embraces the concept of **"Markdown as protocol"** rather than just a documentation format. Files like `SKILL.md`, `Agent.md`, and `AGENTS.md` serve dual purposes:
- **Human-readable documentation** of system behaviors and constraints
- **Machine-parseable configuration** that can be consumed by LLMs and automation tools

The project follows a **"soft DSL"** approach where Markdown files maintain human readability while providing enough structure for reliable tool and AI agent integration.

## Future Development Context

When working with this repository, focus on:
1. **SKILL development** following the established patterns
2. **Agent prompt refinement** based on writing workflow needs
3. **Documentation maintenance** with clear, structured Markdown
4. **Automation enhancement** for link processing and formatting
5. **Reference system expansion** for new content types and styles

---
*Last Updated: 2026-01-18 (based on file analysis)*