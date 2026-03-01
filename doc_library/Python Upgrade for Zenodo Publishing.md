# Review → Plan → Agreement → Code

## Updated Review with File Structure

Perfect! This file listing clarifies everything. I can see:

**Directory Structure:**
```
repo_root/
├── README.md (repo-level, to be generated)
├── papers/
│   ├── {SUBJECT}/              # e.g., AI, BIO, ADHM, etc.
│   │   └── CKS-{SUBJECT}-{N}-2026/
│   │       ├── manuscript.md
│   │       ├── manuscript.json
│   │       ├── zenodo.json
│   │       ├── README.md
│   │       ├── description.txt
│   │       ├── !manuscript.pdf
│   │       ├── {PAPER}.zip (some have it)
│   │       ├── code/ (some papers)
│   │       ├── data/ (some papers)
│   │       ├── figures/
│   │       ├── supplementary/
│   │       ├── references.bib
│   │       └── LICENSE
└── _template/
    ├── zenodo_gen.py (existing manual tool)
    ├── readme_gen.py (existing manual tool)
    ├── gen_pdf.sh, gen_readme.sh, gen_zenodo.sh, gen_zip.sh
    └── ...
```

**Key Observations:**
1. You have **existing tools** in `_template/`: `zenodo_gen.py`, `readme_gen.py`, `scan.py`, etc.
2. Papers are organized by **subject** (AI, BIO, ADHM, etc.) then numbered within subject
3. Each paper has **structured JSON**: `manuscript.json` and `zenodo.json`
4. Some papers have `.zip` files already created, some don't
5. DOI stub pattern: I need to see a manuscript.md to confirm the `.zzz` pattern

**Before I create the plan, I need to see ONE example file to understand the metadata structure:**

Can you share the content of one `manuscript.md` file (preferably a small one like `CKS-AI-1-2026/manuscript.md`) so I can see:
1. What the frontmatter/metadata sections look like
2. Where the DOI field is and what `.zzz` looks like
3. What fields are available for extraction (title, subject, key findings, etc.)

Once I see that, I'll create a complete plan that integrates with your existing `_template/` tools.

---

# Review → Plan → Agreement → Code

## Review: Understanding Your Current Process

After examining all your template tools, here's what I see:

### Current Manual Workflow (Inferred from Scripts)

**For each paper directory (`papers/{SUBJECT}/CKS-{SUBJECT}-{N}-2026/`):**

1. **Create manuscript.md** (manually or with LLM assistance)
   - Contains: title, registry ID, series path, DOI, abstract, full content
   - References other papers with `[@CKS-SUBJECT-N-2026]` syntax
   - DOI uses `.zzz` stub until published: likely `10.5281/zenodo.zzz`

2. **Run `scan.py`**
   - Extracts metadata from manuscript.md → manuscript.json
   - Fields: title, registry_id, series_path, doi, abstract, dependencies (all `[@CKS-...]` refs)

3. **Run `readme_gen.py`** (via `gen_readme.sh`)
   - Uses manuscript.json + template/README.md
   - Generates paper's README.md with metadata

4. **Run `zenodo_gen.py`** (via `gen_zenodo.sh`)
   - Uses manuscript.json + template/zenodo.json
   - Generates paper's zenodo.json for upload

5. **Run `gen_pdf.sh`**
   - Pandoc converts manuscript.md → !manuscript.pdf
   - Heavy Unicode→LaTeX symbol substitution
   - Uses diagram-generator.lua, columns.lua filters
   - Cites from references.bib

6. **Run `gen_zip.sh`**
   - Zips entire paper directory → `{PAPER}.zip`

7. **Run `create_bibs.py`** (globally)
   - Scans ALL manuscript.json files
   - Generates master references.bib
   - Distributes to all paper directories

8. **Manual Zenodo Upload**
   - Upload .zip file
   - Paste zenodo.json metadata
   - Get DOI (e.g., `10.5281/zenodo.12345678`)
   - Replace `.zzz` in manuscript.md with actual DOI
   - Regenerate everything

### The Pain Points You Want to Solve

1. **Too many manual steps** - The "run 6 scripts in sequence" dance
2. **Inconsistent metadata** - Same data duplicated across manuscript.md, manifest.json, zenodo.json, README.md
3. **No central index** - No `papers.json` or repo-level README.md
4. **DOI management** - Manual find/replace of `.zzz` stubs
5. **Zenodo API** - Not using the API, just generating metadata files

### Paper Format Variations

You mentioned:
- **Standard format**: Well-formed papers (most of them)
- **CKS-0-2026 template**: The foundational paper (different structure)
- **Poorly formatted papers**: Same pattern of malformation across several papers

---

## Plan for the Rewrite

We're going to build **robust Python libraries** that replace this fragile shell-script workflow with **confidence-inspiring tools**. We'll do this in mechanical stages.

### Architecture: Three Library Modules

```
cks_tools/
├── __init__.py
├── metadata.py      # Extract/normalize metadata from markdown
├── zenodo.py        # Zenodo API interactions (create/update/publish)
├── documents.py     # PDF generation, ZIP creation, file handling
└── audit.py         # Scan all papers → papers.json
```

### Tools Built on Libraries

```
tools/
├── audit_papers.py      # Scan all papers → papers.json
├── build_readme.py      # Generate repo README.md from papers.json
├── sync_paper.py        # Sync one paper to Zenodo
├── sync_batch.py        # Sync multiple papers from input file
└── fix_legacy.py        # Reformat poorly-formed papers (future)
```

---

## Staged Development Plan

### **Stage 1: Metadata Extraction Library** (`cks_tools/metadata.py`)

**Goal:** Parse manuscript.md reliably, extract all metadata fields, normalize duplicates.

**Features:**
- Parse frontmatter-style metadata (Registry, DOI, Series Path)
- Extract title (H1), abstract (after `## ABSTRACT`)
- Find all `[@CKS-...]` references → dependencies
- Return normalized dict with priority rules for overlapping fields
- Handle both standard format and CKS-0-2026 variations

**Priority Rules for Overlaps:**
```python
# If same field appears multiple places, use first match:
FIELD_PRIORITY = {
    'title': ['frontmatter', 'h1', 'json'],
    'doi': ['frontmatter', 'json'],
    'abstract': ['frontmatter', 'section'],
    # etc.
}
```

**Output:** Python dict ready for JSON serialization

---

### **Stage 2: Audit Tool** (`tools/audit_papers.py`)

**Goal:** Scan all papers, generate `papers.json` at repo root.

**Features:**
- Walk `papers/` directory tree
- For each `manuscript.md`, use `metadata.py` to extract data
- Collect into master list
- Write `papers.json` with schema:

```json
{
  "papers": [
    {
      "registry_id": "CKS-AI-1-2026",
      "path": "papers/AI/CKS-AI-1-2026",
      "title": "Clean Title",
      "subject": "AI",
      "doi": "10.5281/zenodo.12345678",
      "zenodo_id": "12345678",
      "abstract": "...",
      "dependencies": ["CKS-0-2026", "CKS-TEST-1-2026"],
      "has_code": true,
      "has_data": true,
      "has_figures": true,
      "status": "published"  // or "draft" if DOI has .zzz
    },
    // ... all papers
  ],
  "generated_at": "2026-03-01T12:34:56Z"
}
```

---

### **Stage 3: README Generator** (`tools/build_readme.py`)

**Goal:** Generate repo-level README.md and per-paper README.md/description.txt

**Features:**
- Load `papers.json`
- Generate repo README.md with:
  - Paper index by subject
  - Links to Zenodo DOIs
  - Dependency graph visualization (optional)
- For each paper, populate:
  - `README.md` (from template)
  - `description.txt` (from template)

**Template Variables Resolved:**
```python
TEMPLATE_VARS = {
    '<<TITLE>>': 'from papers.json',
    '<<REGISTRY_ID>>': 'from papers.json',
    '<<DOI_LINK>>': 'from papers.json',
    '<<PREREQUISITES>>': 'joined dependencies',
    # etc.
}
```

---

### **Stage 4: Document Handling Library** (`cks_tools/documents.py`)

**Goal:** Wrap PDF generation, ZIP creation, file operations.

**Features:**
- `create_pdf(paper_path)` - Wraps your Pandoc pipeline (or calls `gen_pdf.sh` as subprocess)
- `create_zip(paper_path)` - Creates .zip file
- `extract_repo_contents(paper_path)` - Generates repo_contents.md listing
- Error handling, progress reporting

---

### **Stage 5: Zenodo API Library** (`cks_tools/zenodo.py`)

**Goal:** Interact with Zenodo API programmatically.

**Features:**
- `create_deposition(metadata)` - Create new Zenodo record (draft)
- `upload_file(deposition_id, file_path)` - Upload .zip
- `update_metadata(deposition_id, metadata)` - Update record
- `get_doi(deposition_id)` - Retrieve assigned DOI (even for drafts)
- `publish(deposition_id)` - Publish record (optional, default off)

**API Credentials:** Read from env var or config file:
```python
ZENODO_TOKEN = os.getenv('ZENODO_TOKEN')
ZENODO_BASE_URL = 'https://zenodo.org/api/'  # or sandbox
```

---

### **Stage 6: Sync Tools** (`tools/sync_paper.py`, `tools/sync_batch.py`)

**Goal:** Automate Zenodo upload and DOI replacement.

**`sync_paper.py` workflow:**
1. Load paper metadata from manifest.json
2. Create Zenodo deposition (if new) or find existing
3. Upload .zip file
4. Get DOI (draft DOI returned immediately)
5. Replace `.zzz` in manuscript.md with actual DOI
6. Regenerate manifest.json, README.md
7. Optionally publish (default: no)

**`sync_batch.py` workflow:**
1. Read input file (list of paper directories)
2. For each paper, run `sync_paper.py`
3. Collect results, report errors at end

**Input file format:**
```
papers/AI/CKS-AI-1-2026
papers/BIO/CKS-BIO-1-2026
papers/QM/CKS-QM-1-2026
```

---

### **Stage 7: Legacy Reformatter** (`tools/fix_legacy.py`)

**Goal:** Fix poorly-formatted papers (future stage).

**Approach:**
- Identify common malformation patterns
- Apply regex transformations
- Validate result with `metadata.py`
- Dry-run mode to preview changes

---

## Staged Implementation Order

We'll build **one stage at a time**, review → plan → agreement → code for each:

1. **Stage 1:** `metadata.py` - Get extraction working solidly
2. **Stage 2:** `audit_papers.py` - Generate `papers.json`
3. **Stage 3:** `build_readme.py` - Generate all READMEs
4. **Stage 4:** `documents.py` - Wrap document generation
5. **Stage 5:** `zenodo.py` - API integration
6. **Stage 6:** `sync_paper.py` + `sync_batch.py` - End-to-end automation
7. **Stage 7:** `fix_legacy.py` - Handle edge cases

---

## Questions Before We Begin Stage 1

To start building `metadata.py`, I need to see an **actual manuscript.md file** to understand:

1. What does the frontmatter look like? (Registry:, DOI:, Series Path: fields)
2. Where exactly is the `.zzz` stub in the DOI field?
3. Are there any other metadata sections I'm missing?

Can you upload **one well-formatted manuscript.md** (e.g., from `papers/AI/CKS-AI-1-2026/manuscript.md`) so I can see the exact structure?

Once I see that, I'll write a detailed plan for Stage 1 and await your approval before coding.

---

