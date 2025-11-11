# Flow-Aware PDF-to-Markdown Benchmark

This repository provides a benchmark for evaluating the accuracy of PDF-to-Markdown extraction tools. The main goal is to measure how well a tool can convert a complex, 2D PDF document into a 1D (text/markdown) format that **preserves the logical reading flow** of the content.

---

## The Core Problem

Large Language Models (LLMs) operate on a 1D sequence of tokens. They cannot natively understand the 2D spatial layout of a PDF. This "2D-to-1D" gap is a major bottleneck.

Existing benchmarks are often inadequate:
1.  **They focus on layout detection:** Datasets like DocLayNet are excellent for identifying *bounding boxes* (e.g., "this is a paragraph"), but not for connecting text blocks that form a single, logical flow (e.g., "this paragraph continues in the next column").
2.  **They assume a "total order":** Some benchmarks incorrectly assume a single, linear reading path for an entire document. In reality, complex documents have a **partial order**. For example, a main article and a sidebar can be read independently; neither logically precedes the other.

This benchmark is designed to measure a tool's ability to extract and correctly sequence these logically coherent "threads" of text.

---

## Benchmark Methodology

### 1. Dataset
The benchmark uses **127 PDF documents** sampled from the [DocLayNet dataset](https://github.com/DS4SD/DocLayNet), ensuring a diverse mix of challenging, real-world layouts. The documents are sourced from six distinct categories:
* Financial Reports
* Scientific Articles
* Laws & Regulations
* Government Tenders
* Manuals
* Patents

### 2. Ground Truth
To create a "ground truth" for evaluating text flow, for each document, we **manually copied multiple, random pieces of text in their correct logical reading order** to create "ground truth snippets" for each PDF. An evaluation metric can then check if a tool's output contains these snippets, in order, without being jumbled with text from other columns or sections. This method effectively tests the preservation of reading flow.

### 3. Evaluation Metric: FATA Score
We evaluate tools using a **Flow-Aware Text Accuracy (FATA) Score**. 

1.  For each ground truth text snippet (`truth_i`), we search the tool's entire markdown output to find the substring that is its "best match" (`best_match_i`).
2.  This "best match" is determined using the **Normalized Levenshtein distance** (a measure of character-level similarity).
3.  The final FATA score is a weighted average of the similarity scores for all snippets.
4.  A high FATA score (max 1.0) indicates the tool successfully extracted the text snippets with their internal order intact. A low score indicates the text was "mangled" (e.g., columns interleaved, text garbled), making it impossible to find a clean match for the ground truth snippets. These are converted to percentages, 100% being perfect.

---

## Initial Tools Evaluated

This benchmark was used to generate a comparative analysis of modern PDF extraction tools that produce markdown directly. The initial set of tools evaluated includes:

* LlamaParse
* Docling
* Marker
* Reducto
* PyMuPDF4LLM
* Pymupdf-Layout
* Google Gemini (multimodal)
---


# How to run this benchmark

```bash
uv sync
uv run prod_benchmark.py
```
