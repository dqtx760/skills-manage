# newtype CLI — Multi-Agent Content Team

Binary: `nt` | Package: `npm i -g @newtype-os/cli`

8 specialized AI agents (researcher, writer, editor, fact-checker, extractor, analyst, archivist, chief) accessible as non-interactive CLI commands. Designed for programmatic invocation by other AI agents.

## When to Use

- Deep research on a topic with source verification
- Generate newsletters, essays, reports, technical docs
- Polish existing content (structure → paragraph → sentence → word)
- Fact-check claims or articles
- Extract structured content from PDF, images, web pages
- Framework-based analysis (SWOT, first-principles, PESTEL, etc.)
- Full research-to-publish pipeline orchestration
- Store/retrieve knowledge across sessions

## Installation

```bash
npm i -g @newtype-os/cli
# or
bun i -g @newtype-os/cli
```

Verify: `nt --version`

## Output Modes

| Flag        | Behavior                | Use When                               |
| ----------- | ----------------------- | -------------------------------------- |
| (none)      | Plain text to stdout    | Human reading, simple piping           |
| `--json`    | JSON envelope to stdout | Agent parsing results programmatically |
| `--stream`  | NDJSON event stream     | Real-time progress monitoring          |
| `-o <file>` | Write result to file    | Saving output, pipeline steps          |

### JSON Envelope Schema

```json
{
  "success": true,
  "result": "... the text output ...",
  "metadata": {
    "agent": "researcher",
    "sessionID": "...",
    "duration_ms": 45000,
    "tools": [{ "name": "web_search", "title": "..." }]
  }
}
```

On error:

```json
{
  "success": false,
  "error": { "code": 2, "message": "..." },
  "metadata": {
    "agent": "researcher",
    "sessionID": "...",
    "duration_ms": 12000,
    "tools": []
  }
}
```

## Exit Codes

| Code | Meaning              |
| ---- | -------------------- |
| 0    | Success              |
| 1    | Input/argument error |
| 2    | Model call failed    |
| 3    | Timeout              |
| 4    | Config/auth error    |

## Input Methods (priority high → low)

1. Positional text: `nt research AI Agent architectures`
2. `--input <file>` — read from file
3. `--topic <text>` — explicit topic string
4. stdin pipe: `cat notes.md | nt write`

## Global Flags

| Flag              | Short | Description                               |
| ----------------- | ----- | ----------------------------------------- |
| `--output <path>` | `-o`  | Output file (default: stdout)             |
| `--json`          |       | JSON envelope output                      |
| `--stream`        |       | NDJSON event stream                       |
| `--verbose`       |       | Show tool execution progress              |
| `--quiet`         | `-q`  | Suppress non-result output                |
| `--model <p/m>`   | `-m`  | Override model (format: `provider/model`) |
| `--lang <code>`   |       | Output language: `zh`, `en`, `ja`, etc.   |
| `--timeout <sec>` | `-t`  | Timeout in seconds (default: 300)         |
| `--input <file>`  |       | Input file path                           |
| `--topic <text>`  |       | Topic text                                |

---

## Commands

### `nt research [topic..]` — Topic Research

Agent: researcher (+ fact-checker by default)

```bash
# Basic
nt research "AI Agent architectures 2026" -o research.md

# Deep research with focus
nt research "MCP vs CLI" --depth deep --focus "developer experience,adoption" -o deep.md

# JSON output for programmatic consumption
nt research "Kubernetes security" --json

# Skip fact-checking for speed
nt research "quick overview of RAG" --no-fact-check -o quick.md

# Pipe research into writing
nt research "AI trends" -o /tmp/r.md && nt write --input /tmp/r.md -o draft.md
```

| Flag                 | Default  | Description                     |
| -------------------- | -------- | ------------------------------- |
| `--depth <level>`    | `normal` | `shallow` / `normal` / `deep`   |
| `--sources <n>`      | `5`      | Expected number of sources      |
| `--focus <keywords>` |          | Focus keywords, comma-separated |
| `--no-fact-check`    |          | Skip fact-checking step         |

### `nt write [topic..]` — Content Generation

Agent: writer

```bash
# From research material
nt write --input research.md --style newsletter -o draft.md

# From scratch with topic
nt write "Why CLI is the native language of AI Agents" --style essay --words 2000 -o article.md

# Specify methodology and tone
nt write --input notes.md --method AIDA --tone professional --audience "CTOs and VPs of Engineering" -o post.md
```

| Flag                | Default | Description                                                                 |
| ------------------- | ------- | --------------------------------------------------------------------------- |
| `--style <s>`       |         | `newsletter` / `essay` / `report` / `tweet-thread` / `technical` / `story`  |
| `--method <m>`      |         | `WRITE` / `AIDA` / `PAS` / `STORYTELLING` / `ANALYTICAL` / `CONVERSATIONAL` |
| `--words <n>`       | `1500`  | Target word count                                                           |
| `--tone <t>`        |         | `professional` / `casual` / `academic` / `provocative`                      |
| `--audience <desc>` |         | Target audience description                                                 |

### `nt edit [file]` — Content Editing

Agent: editor. Four-layer refinement: structure → paragraph → sentence → word.

```bash
# Full edit
nt edit --input draft.md -o final.md

# Structure-only pass
nt edit --input draft.md --layer structure -o restructured.md

# Preserve voice, only fix grammar
nt edit --input draft.md --preserve-voice -o polished.md

# Pipe from stdin
cat draft.md | nt edit -o final.md

# Edit with diff output
nt edit --input draft.md --diff -o final.md
```

| Flag                       | Default | Description                                             |
| -------------------------- | ------- | ------------------------------------------------------- |
| `--layer <l>`              | `all`   | `structure` / `paragraph` / `sentence` / `word` / `all` |
| `--tone <t>`               |         | Target tone                                             |
| `--target-audience <desc>` |         | Target audience                                         |
| `--preserve-voice`         |         | Keep original voice, fix grammar/logic only             |
| `--diff`                   |         | Include diff showing changes                            |

### `nt fact-check [topic..]` — Fact Verification

Agent: fact-checker

```bash
# Check an article
nt fact-check --input article.md -o report.md

# Check a single claim
nt fact-check --claim "GPT-4 has 1.8 trillion parameters" --json

# Strict mode with extra cross-verification
nt fact-check --input report.md --strict -o verified.md
```

| Flag             | Description                          |
| ---------------- | ------------------------------------ |
| `--claim <text>` | Verify a single claim                |
| `--strict`       | Strict mode — more cross-referencing |

### `nt analyze [topic..]` — Framework Analysis

Agent: chief + researcher. Supports 12 analysis frameworks.

```bash
# SWOT analysis
nt analyze --input research.md --framework swot -o analysis.md

# First principles
nt analyze "Why are all tools moving to CLI" --framework first-principles -o analysis.md

# Multiple frameworks combined
nt analyze --input data.md --framework "swot,pestel" -o combo.md

# JSON output
nt analyze "React vs Vue market position" --framework porter --json
```

Available frameworks: `swot`, `pestel`, `porter`, `first-principles`, `5why`, `jobs-to-be-done`, `blue-ocean`, `value-chain`, `bcg-matrix`, `ansoff`, `okr`, `systems-thinking`

| Flag                 | Description                   |
| -------------------- | ----------------------------- |
| `--framework <name>` | Framework(s), comma-separated |

### `nt extract [topic..]` — Content Extraction

Agent: extractor. Extract structured content from documents, images, or web pages.

```bash
# Extract from file
nt extract --input paper.pdf -o extracted.md

# Extract from URL
nt extract --url "https://example.com/article" -o page.md

# Prioritize tables
nt extract --input report.pdf --extract-tables --json
```

| Flag               | Description                        |
| ------------------ | ---------------------------------- |
| `--url <url>`      | Web page URL to extract from       |
| `--extract-tables` | Prioritize table extraction        |
| `--extract-images` | Extract and describe image content |

### `nt archive <action>` — Knowledge Base

Agent: archivist. Subcommands: `store`, `search`, `list`, `delete`.

```bash
# Store content with tags
nt archive store --input research.md --tags "AI,Agent,2026"

# Semantic search
nt archive search --query "difference between MCP and CLI" --top 5 -o results.md

# List all entries (filtered by tag)
nt archive list --tags "AI" --json

# Delete entry
nt archive delete --id "entry-123"
```

| Flag             | Description                           |
| ---------------- | ------------------------------------- |
| `--tags <csv>`   | Tags, comma-separated (store/list)    |
| `--query <text>` | Search query (search, required)       |
| `--top <n>`      | Number of search results (default: 5) |
| `--id <id>`      | Entry ID (delete, required)           |

### `nt pipeline [topic..]` — Full Workflow

Agent: chief orchestrating all agents. Default steps: research → analyze → write → fact-check → edit.

```bash
# Full pipeline from topic
nt pipeline "AI Agent trends 2026" --style newsletter --output-dir ./output/

# Custom steps
nt pipeline "MCP future" --steps "research,write,edit" -o result.md

# From existing material (skip research)
nt pipeline --input notes.md --steps "analyze,write,edit" -o final.md

# JSON output
nt pipeline "topic" --json
```

| Flag                 | Default                                  | Description                                   |
| -------------------- | ---------------------------------------- | --------------------------------------------- |
| `--steps <csv>`      | `research,analyze,write,fact-check,edit` | Workflow steps                                |
| `--style <s>`        |                                          | Final output writing style                    |
| `--output-dir <dir>` |                                          | Output directory (one file per step)          |
| `--parallel`         |                                          | Allow parallel execution of independent steps |

Default timeout: 600s (vs 300s for other commands).

---

## Pipeline Composition Patterns

Chain commands with `&&` for multi-step workflows:

```bash
# Research → Write → Edit
nt research "AI Agents" -o /tmp/r.md \
  && nt write --input /tmp/r.md --style newsletter -o /tmp/d.md \
  && nt edit --input /tmp/d.md -o final.md

# Extract → Fact-check → Archive
nt extract --input paper.pdf -o /tmp/e.md \
  && nt fact-check --input /tmp/e.md -o /tmp/fc.md \
  && nt archive store --input /tmp/fc.md --tags "paper,verified"

# Research with JSON for downstream parsing
nt research "topic" --json | jq '.result' > research.txt
```

## Agent Integration Examples

For AI agents (Claude Code, Cursor, etc.) calling `nt` programmatically:

```bash
# Get structured output
result=$(nt research "Kubernetes best practices" --json)
echo "$result" | jq -r '.result'    # extract text
echo "$result" | jq '.success'      # check success
echo "$result" | jq '.metadata'     # get metadata

# Check exit code
nt research "topic" --json -o out.json
if [ $? -eq 0 ]; then
  echo "Success"
elif [ $? -eq 2 ]; then
  echo "Model call failed, retry"
elif [ $? -eq 3 ]; then
  echo "Timeout, increase with --timeout"
fi

# Write to file and verify
nt write "topic" -o draft.md && test -f draft.md && echo "File created"
```

## Command → Agent Mapping

| Command         | Agent(s)                    | Description                            |
| --------------- | --------------------------- | -------------------------------------- |
| `nt research`   | researcher (+ fact-checker) | Deep research with source verification |
| `nt write`      | writer                      | Multi-style content generation         |
| `nt edit`       | editor                      | Four-layer content refinement          |
| `nt fact-check` | fact-checker                | Claim and source verification          |
| `nt analyze`    | chief + researcher          | 12 analysis frameworks                 |
| `nt extract`    | extractor                   | Document/image/web extraction          |
| `nt archive`    | archivist                   | Knowledge base CRUD                    |
| `nt pipeline`   | chief → all                 | Full orchestration pipeline            |
