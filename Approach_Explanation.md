

# Approach Explanation: Persona-Driven Document Intelligence (Challenge 1B)

## Problem Statement
Traditional semantic search is effective at finding text with similar meaning, but it often fails to respect strict persona or user constraints. For example, a naive search for "vegetarian buffet" might still return recipes with "bacon" or "sausage" because these terms are semantically related to food, not because they are relevant to the persona's needs. This is a critical failure in real-world, persona-driven applications.

## Solution Overview
Our solution is a robust, multi-stage pipeline that combines fast keyword filtering, global semantic search, and local generative AI to deliver highly relevant, persona-driven insights from document collections. The pipeline is fully offline-capable and designed for scalability and extensibility.

## Pipeline Details

### 1. Pre-retrieval Keyword Filtering
- **Goal:** Strictly enforce persona constraints before any AI processing.
- **How:** The system scans and removes any text chunk containing forbidden keywords (e.g., non-vegetarian terms for a vegetarian persona). This guarantees that only content matching the persona's requirements is considered in the next stage.
- **Benefit:** Ensures that negative constraints are respected, eliminating irrelevant or inappropriate content early in the process.

### 2. Global Semantic Ranking
- **Goal:** Find the most relevant content for the user's task, across all documents.
- **How:** All remaining ("safe") chunks from all documents are pooled together. We use the `all-MiniLM-L6-v2` sentence transformer to rank these chunks by semantic similarity to the user’s task description. This ensures the best content is selected globally, not just per document.
- **Benefit:** Delivers the most contextually relevant results, regardless of their original document source.

### 3. AI-Powered Title Generation
- **Goal:** Make the output clear, concise, and professional.
- **How:** For each top-ranked section, we use a local generative model (`flan-t5-small`) to create a concise, human-readable title. This is far superior to simple heuristics like using the first line as a title.
- **Benefit:** Transforms raw extracted text into a polished, actionable summary that is easy to consume and use.

## Why This Approach Works
- **Precision:** Persona constraints are strictly enforced before any AI ranking, eliminating false positives.
- **Relevance:** Global semantic ranking ensures the best content is surfaced for the user’s specific task.
- **Clarity:** AI-generated titles make the output easy to understand and act on.
- **Offline-First:** All models are loaded from local disk, making the solution robust and deployable in restricted environments.
- **Scalability:** The pipeline is easily extensible for new personas, document types, or additional processing stages.

## Example Use Cases
- **Travel Planning:** Extracting the best travel tips, recommendations, and itineraries for a group with specific needs.
- **Learning Guides:** Summarizing and ranking the most relevant sections from technical manuals or learning resources.
- **Recipe Collections:** Delivering only vegetarian (or other dietary) recipes, with clear titles and context.

## Summary
By combining fast keyword filtering, global semantic search, and local generative AI, our pipeline delivers robust, accurate, and user-centric document intelligence—fully offline and ready for real-world use cases. This approach goes beyond traditional search to deliver true persona-driven insights, making it ideal for enterprise, educational, and consumer applications alike.
