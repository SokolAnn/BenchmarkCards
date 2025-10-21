# MuLD: The Multitask Long Document Benchmark

## 📊 Benchmark Details

**Name**: MuLD: The Multitask Long Document Benchmark

**Overview**: We present MuLD: a new long document benchmark consisting of only documents over 10,000 tokens. By modifying existing NLP tasks, we create a diverse benchmark which requires models to successfully model long-term dependencies in the text. We evaluate how existing models perform, and find that our benchmark is much more challenging than their 'short document' equivalents.

**Data Type**: long-form text documents (>=10,000 tokens); question-answering pairs; summarization pairs; translation pairs; text classification labels; style-change annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- Long Range Arena
- QuALITY
- SCROLLS

**Resources**:
- [GitHub Repository](https://github.com/ghomasHudson/muld)
- [Resource](https://arxiv.org/abs/2202.07362)
- [Resource](https://www.imsdb.com)
- [Resource](https://opus.nlpl.eu/OpenSubtitles2016.php)

## 🎯 Purpose and Intended Users

**Goal**: To enable the evaluation of long document models by introducing a benchmark of varied NLP tasks where each document consists of more than 10,000 tokens; tasks are created by filtering, extending, or modifying existing NLP tasks to require long context modeling.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Summarization
- Machine Translation
- Style Change Detection
- Text Classification (Character Archetype Classification)

**Limitations**: N/A

## 💾 Data

**Source**: Datasets are formed by filtering, extending, or modifying existing NLP datasets: NarrativeQA (full novels/movie scripts), HotpotQA (expanded by concatenating full Wikipedia pages and distractor articles), AO3 (Archive of Our Own) stories for style change detection, movie scripts (primarily from www.imsdb.com) matched with Wikipedia plot summaries for Character Archetype classification, Very Long Scientific Papers extracted from arXiv.org (VLSP), and OpenSubtitles (full movie/TV subtitles, filtered to >=10,000 tokens).

**Size**: Per Table 1 in paper: NarrativeQA - Train 32,159 documents (avg. 91,938 tokens), Valid 3,461 (avg. 90,832 tokens), Test 10,261 (avg. 88,579 tokens). HotpotQA - Train 87,752 (avg. 23,775 tokens), Valid 7,405 (avg. 22,669 tokens). AO3 Style Change - Train 6,354 (avg. 29,657 tokens), Valid 705 (avg. 29,304 tokens), Test 2,352 (avg. 30,502 tokens). Movie Character Types - Train 167 (avg. 44,640 tokens), Test 86 (avg. 48,165 tokens). Very Long Scientific Papers (VLSP) - Test 482 (avg. 57,473 tokens). OpenSubtitles - Train 4,252 (avg. 12,330 tokens), Test 1,385 (avg. 18,932 tokens).

**Format**: N/A

**Annotation**: Character Archetype labels annotated via Amazon Mechanical Turk with multiple annotators and manual verification. AO3 style change documents constructed programmatically from fanfiction paragraphs with paragraph-level partitioning; ContraPro annotations used for contrastive pronoun evaluation in OpenSubtitles (explicitly referenced). Other datasets use existing annotations from their original sources (NarrativeQA, HotpotQA, VLSP/OpenArXiv, OpenSubtitles).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Baseline model evaluation (T5, Longformer)
- Chunking-based input splitting and retrieval (TF-IDF cosine similarity for chunk selection)

**Metrics**:
- BLEU-1
- BLEU-4
- ROUGE-L
- METEOR
- F1 Score

**Calculation**: Generation tasks (QA, Summarization, Translation) evaluated using BLEU-1, BLEU-4, METEOR, and ROUGE-L, using multiple references where available. Classification and style change detection tasks evaluated using F1 Score. For QA (NarrativeQA/HotpotQA) documents are chunked and top TF-IDF-similar chunks are selected and concatenated as model input; OpenSubtitles are chunked respecting line breaks and translated chunk-wise.

**Interpretation**: Higher BLEU/METEOR/ROUGE-L and F1 Score indicate better performance on respective tasks. The authors interpret that models with increased context length (Longformer) perform better on many tasks compared to a short-context model (T5), and that MuLD is more challenging than short-document equivalents.

**Baseline Results**: Table 2 results (selected): T5 - NarrativeQA BLEU-1 17.67, BLEU-4 0.55, ROUGE-L 19.03, METEOR 3.36; HotpotQA BLEU-1 28.11, BLEU-4 13.63, ROUGE-L 27.61, METEOR 4.46; Style Change F1 26.49; Character Type F1 54.01; VLSP BLEU-1 28.85, BLEU-4 0.84, ROUGE-L 16.55, METEOR 7.98; OpenSubtitles BLEU-1 34.07, BLEU-4 1.63, ROUGE-L 35.35, METEOR 38.53. Longformer - NarrativeQA BLEU-1 19.84, BLEU-4 0.62, ROUGE-L 22.09, METEOR 4.52; HotpotQA BLEU-1 30.38, BLEU-4 16.76, ROUGE-L 30.49, METEOR 4.98; Style Change F1 28.17; Character Type F1 82.58; VLSP BLEU-1 46.74, BLEU-4 3.05, ROUGE-L 19.52, METEOR 9.58; OpenSubtitles BLEU-1 22.74, BLEU-4 0.20, ROUGE-L 22.17, METEOR 22.95.

**Validation**: Uses existing train/validation/test splits from source datasets after filtering for documents >=10,000 tokens. VLSP: small test set of 482 documents is provided; models trained on original shorter-length scientific papers dataset due to time required to compile long documents.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
