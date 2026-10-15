# Contract Intelligence Pipeline

A Python learning project that extracts contracting parties, agreement dates,
and governing law from commercial contracts using Gemini, validates the output
with Pydantic, and evaluates it against CUAD reference answers.

The project uses a modular monolith. Milestones 1 and 2 are complete; PDF
parsing and the application interface are planned.

## Setup

Requires Python 3.12 or newer and [uv](https://docs.astral.sh/uv/).

```sh
uv sync --locked
cp .env.example .env
```

Set `GEMINI_API_KEY` and `GEMINI_MODEL` in `.env`. The key stays local and is
excluded from Git. Live extraction sends contract text to Gemini and uses API
quota; automated tests use mocked responses.

## Usage

Run one contract:

```sh
uv run python main.py "data/raw/contracts/CybergyHoldingsInc_20140520_10-Q_EX-10.27_8605784_EX-10.27_Affiliate Agreement.txt"
```

Run the seven-contract sample:

```sh
uv run python main.py data/raw/contracts/batch_sample
```

The batch processes direct TXT files sequentially in filename order; it does
not recurse into subfolders. One failed contract does not stop the batch.
Inputs currently need a matching filename in `data/raw/master_clauses.csv`.
Processing new contracts without reference answers is future work.

## Workflow and results

```text
Contract TXT → Gemini → Pydantic validation → CUAD comparison → JSON report
```

Each run prints and saves a timestamped report in `data/processed/`, including
extracted values, supporting quotes, reference comparisons, evidence checks,
review reasons, processing time and token usage. A batch summary includes
individual results and aggregate counts. Generated runs remain local and are
excluded from Git; repeated runs retain separate reports.

Extraction and evaluation conventions:

- Preserve named contracting parties and stated trading names. Do not invent
  missing template identities or unnamed affiliates.
- For combined numbered amendments, target the highest numbered amendment.
- Select dates in order: explicit agreement date, explicitly linked date
  definition, then execution-supported latest signature date as a fallback.
  Record the selection `basis`; incomplete dates stay null.
- Evidence can contain one quote or separate quotes. Check source presence
  after whitespace normalization; presence alone does not prove correctness.
- Normalize explicit aliases, collective descriptions, jurisdiction prefixes
  and supported date formats conservatively. Preserve meaningful legal-name
  and jurisdiction scope differences. Unsupported references remain unscored.

Reference match rates are not guaranteed extraction accuracy. Missing-reference
matches are counted separately from populated fields; failed or unavailable
usage is not assumed to be zero tokens. Processing time covers reading through
evaluation and evidence checking, excluding report saving.

## Validation

```sh
uv run python -m pytest -q
uv run ruff check app main.py tests
```

Milestone 2 closed on 15 October 2026. The
[consolidated results](MILESTONE_2_RESULTS.md) cover 63 unique tested contracts,
with extracted/reference answers, evidence and review findings separated by
prompt version. The final 20 unseen contracts completed successfully; old cases
were not rerun for that report. All 33 automated tests passed at closeout.

Known limitations include stated-date versus signature-date conventions,
collective-party cleanup, unknown/affiliate scope, and multi-jurisdiction
representations. These remain review cases, not forced matches.

## Repository layout

```text
app/
  core/config.py          Environment settings and data paths
  extraction/             Prompt, Pydantic schemas and Gemini client
  evaluation/cuad.py      Reference lookup and comparison rules
  pipeline.py             Single-contract and batch processing
main.py                   Command-line entry point
tests/                    Mocked pipeline and evaluation tests
data/raw/                 CUAD reference CSV and tested contract samples
data/validation_manifest.json  Sample provenance and source hashes
MILESTONE_2_RESULTS.md     Consolidated evaluation findings
```

## Dataset

The included reference CSV and contract samples come from CUAD v1, curated by
[The Atticus Project](https://github.com/TheAtticusProject/cuad).
See the [dataset paper](https://arxiv.org/abs/2103.06268) for background.
The [validation manifest](data/validation_manifest.json) identifies the 63 tested
TXT files, their source hashes and result cohorts. The original sample PDF is
retained for the upcoming parsing milestone. The samples are a development set,
not a representative accuracy benchmark.

## Roadmap

Keep implementation minimal and modular. Extraction remains focused on the
three initial fields; testing continues throughout development.

| Milestone | What we'll build | Completion criteria |
| --- | --- | --- |
| **1. Contract extraction MVP — complete** | Read a TXT contract, extract and validate three fields using Gemini, compare against CUAD, and save results with time and token usage. | A single-contract run produces a validated JSON report with evaluation and usage. |
| **2. Batch processing and evaluation — complete** | Process multiple TXT contracts, handle individual failures, and summarize accuracy, time, and tokens. | A batch completes despite individual failures, with results and a useful summary. |
| **3. PDF parsing** | Use Docling to convert PDFs into text and feed our existing pipeline. | PDF extraction works on representative contracts, with parsing failures reported clearly. |
| **4. FastAPI service** | Add a contract-upload endpoint that runs parsing and extraction. | Uploading a PDF returns structured results or a clear error. |
| **5. Storage** | Use DuckDB to retain processing records, extracted fields, evaluation where available, and usage. | Previous results can be listed and retrieved after restarting the application. |
| **6. Upload and review interface** | Add a simple screen to upload contracts, inspect values and evidence, view history, and download JSON. | A user can complete the workflow without running commands. |
| **7. Reliability and packaging** | Complete meaningful tests, improve error handling and logging, add Docker, and document setup. | The application runs reproducibly and handles common failure cases. |
