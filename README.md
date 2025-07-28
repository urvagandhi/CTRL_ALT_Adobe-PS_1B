# Persona-Driven Document Intelligence (Adobe Hackathon - Challenge 1B)

## Overview

This project is an advanced, offline-capable solution for extracting persona-driven insights from document collections. Designed for Challenge 1B of the Adobe India Hackathon, it leverages a multi-stage Retrieval-Augmented Generation (RAG) pipeline to deliver highly relevant, context-aware, and user-centric results.

## Features

- **Two-Stage Retrieval Pipeline:**
  - **Stage 1: Keyword Filtering** — Removes content that violates persona constraints (e.g., non-vegetarian items for a vegetarian persona).
  - **Stage 2: Semantic Ranking** — Uses the `all-MiniLM-L6-v2` sentence transformer to globally rank the remaining content for maximum relevance.
- **AI-Powered Title Generation:**
  - Utilizes a local generative model (`flan-t5-small`) to create concise, human-readable titles for each extracted section.
- **Global Ranking:**
  - Pools and ranks content from all documents in a collection, ensuring only the best results are included in the output.
- **Unified, Configurable Script:**
  - A single Python script (`run_analysis.py`) processes any collection, with easy command-line configuration.
- **Offline-First:**
  - All models are loaded from local folders, ensuring the solution works without internet access.

## Setup & Usage

### 1. Install Dependencies

Install all required libraries using:

```sh
pip install -r requirements.txt
```


### 2. Download and Place Models Locally

Use the provided `download_model.py` script to automatically download and save the required models locally:

```sh
python download_model.py
```

This will create a `models/` directory with the following structure:

```
models/
  all_MiniLM_L6_v2/
  flan_t5_small/
```

**Important:**
- The `models/` directory is NOT tracked in git (see `.gitignore`).
- You must have the `models/` directory present locally before running the script or building the Docker image.
- If you are building a Docker image, ensure `models/` is present in your build context.

### 3. Run the Analysis Script

Run the script for any collection:

```sh
python run_analysis.py ./Collection_1/
# or
python run_analysis.py ./Collection_2/
# or
python run_analysis.py ./Collection_3/
```

The script will generate a `challenge1b_output.json` file in the respective collection directory.

## Project Structure

```
├── Collection_1/
│   ├── PDFs/
│   └── challenge1b_input.json
├── Collection_2/
│   ├── PDFs/
│   └── challenge1b_input.json
├── Collection_3/
│   ├── PDFs/
│   └── challenge1b_input.json
├── Dockerfile
├── README.md
├── approach_explanation.md
├── requirements.txt
├── run_analysis.py
├── download_model.py
└── models/
    ├── all_MiniLM_L6_v2/
    └── flan_t5_small/
```

## How It Works

1. **Keyword Filtering:**
   - The pipeline first removes any text chunk containing forbidden keywords (e.g., non-vegetarian terms for a vegetarian persona).
2. **Semantic Ranking:**
   - The remaining content is ranked globally using the `all-MiniLM-L6-v2` model for semantic similarity to the user's task.
3. **Title Generation:**
   - For each top-ranked section, a concise, human-readable title is generated using the local `flan-t5-small` model.
4. **Output:**
   - The best results are saved in a structured JSON file, ready for further use or presentation.

## Why This Approach?

- **Accuracy:** Strict persona constraints are enforced before any AI ranking.
- **Relevance:** Global semantic ranking finds the best content for the user’s task.
- **Clarity:** AI-generated titles make the output easy to understand and act on.
- **Scalability:** The unified script and offline model loading make it easy to deploy and extend.

## Troubleshooting

- **Model Not Found:**
  - Ensure you have run `download_model.py` and the `models/` directory contains both `all_MiniLM_L6_v2/` and `flan_t5_small/` before running the script or building the Docker image. The models are not tracked in git and must be present locally.
- **Missing Dependencies:**
  - Run `pip install -r requirements.txt` to install all required packages.
- **PDF Extraction Issues:**
  - Make sure your PDFs are not encrypted or corrupted. The script uses `pdfplumber` for extraction.

## References

- [Sentence Transformers - all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
- [HuggingFace Transformers - flan-t5-small](https://huggingface.co/google/flan-t5-small)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

## Team Details

**Team Name:** Clt+Alt+Adobe

| Name         | Email                     | Phone Number |
| :----------- | :------------------------ | :----------- |
| Urva Gandhi  | urvagandhi24@gmail.com    | 8866241204   |
| Harsh khanna | harsh2004khanna@gmail.com | 9033175024   |
| Diya Patel   | gdiya2646@gmail.com       | 9879472806   |

---

This solution demonstrates a practical, scalable, and user-centric approach to document intelligence, going beyond traditional search to deliver true persona-driven insights.
