# Contract Intelligence Pipeline

## Overview

A production-style document intelligence system that extracts structured information from commercial contracts using Google Gemini.

The project uses the Contract Understanding Atticus Dataset (CUAD) for evaluation against expert-annotated reference answers.

## Technology Stack

- Python 3.12
- Google Gemini SDK
- Pydantic
- Pandas
- Docling (later stage)
- FastAPI (later stage)
- DuckDB (later stage)
- pytest
- Docker (later stage)

## Initial Extraction Fields

1. Contracting parties
2. Agreement date
3. Governing law

## Initial Workflow

Contract TXT → Gemini → Pydantic Validation → JSON → CUAD Evaluation

## Run a Single Extraction

Create `.env` from `.env.example` and set `GEMINI_API_KEY` and `GEMINI_MODEL`.
Then run:

```sh
uv run python main.py "data/raw/contracts/CybergyHoldingsInc_20140520_10-Q_EX-10.27_8605784_EX-10.27_Affiliate Agreement.txt"
```

The command prints validated extraction JSON and field-level CUAD evaluation.
Comparisons normalize party order, aliases in parentheses, punctuation, case,
whitespace, and date formats. Mismatches remain visible for manual review;
unsupported reference date formats receive a null match rather than a score.
Each run saves a timestamped JSON report in `data/processed/`, containing the
source filename, model, UTC start time, extraction, evaluation, processing time,
and input/output/thinking/total token counts reported by Gemini. Unavailable
token counts are null. Processing time covers reading through evaluation,
excluding report saving. Repeated runs keep separate reports.

Run evaluation tests with `uv run python -m pytest`.

## Development Milestones

This is the agreed project roadmap. Milestone 1 is complete; milestones 2–7
are planned in the order below. Keep implementation minimal and simple, using
a modular monolith. CUAD sample contracts will support learning and evaluation;
personal contracts are not required.

| Milestone | What we'll build | Completion criteria |
| --- | --- | --- |
| **1. Contract extraction MVP — complete** | Read a TXT contract, extract and validate three fields using Gemini, compare against CUAD, and save results with time and token usage. | A single-contract run produces a validated JSON report with evaluation and usage. |
| **2. Batch processing and evaluation** | Process multiple TXT contracts, handle individual failures, and summarize accuracy, time, and tokens. | A batch completes despite individual failures, with results and a useful summary. |
| **3. PDF parsing** | Use Docling to convert PDFs into text and feed our existing pipeline. | PDF extraction works on representative contracts, with parsing failures reported clearly. |
| **4. FastAPI service** | Add a contract-upload endpoint that runs parsing and extraction. | Uploading a PDF returns structured results or a clear error. |
| **5. Storage** | Use DuckDB to retain processing records, extracted fields, evaluation where available, and usage. | Previous results can be listed and retrieved after restarting the application. |
| **6. Upload and review interface** | Add a simple screen to upload contracts, inspect values and evidence, view history, and download JSON. | A user can complete the workflow without running commands. |
| **7. Reliability and packaging** | Complete meaningful tests, improve error handling and logging, add Docker, and document setup. | The application runs reproducibly and handles common failure cases. |

Tests will be added throughout development. Extraction remains focused on
contracting parties, agreement date, and governing law. CUAD contracts can be
evaluated against reference answers; new contracts without reference answers
will provide extracted values and evidence for review, without an accuracy score.

## Project Goal

Learn to design, implement, evaluate and maintain a reliable, production-style AI document processing system.

## Milestone 1 — Contract Extraction MVP

Completed requirements:

- [x] Read a CUAD contract from a local TXT file
- [x] Extract parties, agreement date and governing law using Gemini
- [x] Return a structured JSON response
- [x] Validate the JSON using Pydantic
- [x] Compare extracted values against master_clauses.csv
- [x] Record processing time and token usage
- [x] Save the extraction result locally
