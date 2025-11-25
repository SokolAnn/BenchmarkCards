# USB: A Unified Summarization Benchmark Across Tasks and Domains

## 📊 Benchmark Details

**Name**: USB: A Unified Summarization Benchmark Across Tasks and Domains

**Overview**: We introduce USB, a Wikipedia-derived benchmark complemented by a rich set of crowd-sourced annotations that supports eight interrelated tasks (extractive summarization; abstractive summarization; topic-based summarization; compressing selected sentences into a one-line summary; surfacing evidence for a summary sentence; predicting the factual accuracy of a summary sentence; identifying unsubstantiated spans in a summary sentence; correcting factual errors in summaries). The benchmark includes labeled datasets with high-quality human annotations collected from diverse documents across six domains.

**Data Type**: text (document-summary pairs with sentence-level evidence annotations and unsupported-span annotations)

**Domains**:
- Biographies
- Companies
- Schools
- Newspapers
- Landmarks
- Disasters

**Languages**:
- English

**Similar Benchmarks**:
- SuperPAL
- FactEdit
- FactCC
- Samsum

**Resources**:
- [GitHub Repository](https://github.com/kukrishna/usb)
- [Resource](https://arxiv.org/abs/2305.14296)
- [GitHub Repository](https://github.com/attardi/wikiextractor)
- [Resource](https://spacy.io)
- [Resource](https://www.dbpedia-spotlight.org)

## 🎯 Purpose and Intended Users

**Goal**: Provide a multi-domain benchmark with human-labeled datasets to train and evaluate models on eight tasks that assess control, reliability, and factuality-related aspects of text summarization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Extractive Summarization
- Abstractive Summarization
- Topic-based Summarization
- Multi-sentence Compression
- Evidence Extraction
- Factuality Classification
- Unsupported Span Prediction
- Fixing Factuality

**Limitations**: The benchmark may exhibit biases due to sampling and the selection of Wikipedia articles as the primary data source; conversations are not represented; possible annotation errors or inconsistencies in human annotations.

## 💾 Data

**Source**: Wikipedia English articles dump (downloaded 1 July 2022) processed with Wikiextractor; overview (leading) section used as candidate summary and remaining article as source document; articles filtered into six domains.

**Size**: 1,988 document-summary pairs (total annotated documents across all domains)

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with a qualification task and worker selection; primary annotators performed main annotations; model-assisted verification (Flan-T5-XL) used to flag likely unsupported spans for a verification round; final annotations include sentence-level evidence links, edited summaries, and span-level unsupported annotations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- Fine-tuning of models
- Few-shot prompting of large language models
- Multi-task training

**Metrics**:
- ROUGE (ROUGE-1, ROUGE-2, ROUGE-L; geometric mean of variants used for generation tasks)
- Exact Match (used for Fixing Factuality)
- F1 Score (BIO tagging format for Unsupported Span Prediction)
- Area Under Curve (AUC) (used for classification tasks)
- Accuracy (used where applicable)
- Precision
- Recall

**Calculation**: For generation tasks, geometric mean of ROUGE-1/2/L reported. Fixing Factuality uses Exact Match. Unsupported Span Prediction evaluated with F1 based on BIO token tagging. Classification/span tasks use standard binary classification metrics and AUC where noted.

**Interpretation**: Higher ROUGE indicates closeness to the ground-truth edited summaries; Exact Match indicates identical corrected summary for FIX; F1 (BIO) measures span-prediction quality for UNSUP. The paper notes that ROUGE does not always mirror human preference and human evaluations may prefer different outputs. Fine-tuned smaller models outperform few-shot prompted LLMs on factuality-related tasks.

**Baseline Results**: Key results (Table 2) — Flan-T5-XL (fine-tuned): COMP ROUGE 44.87; EVEXT F1 79.23; EXT 87.81; FAC AUC 95.30; FIX ExactMatch 35.10; ABS ROUGE 32.69; TOPIC ROUGE 24.26; UNSUP F1 64.94. GPT-3.5-turbo (few-shot): COMP ROUGE 33.21; EVEXT F1 26.78; EXT 61.63; FAC AUC 60.81; FIX ExactMatch 3.29; ABS ROUGE 29.77; TOPIC ROUGE 14.59; UNSUP F1 7.80.

**Validation**: Data splits generally use 40:20:40 train:validation:test per domain (except landmarks and newspapers held out as challenging test sets). Verification included a model-assisted verification pass to flag likely unsupported spans for human re-check. Human evaluation conducted for generation tasks on 50 randomly selected test documents with multiple annotators; FIX human evaluation used screened annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Reproducibility
- Annotation quality

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of model transparency

**Demographic Analysis**: Annotator pool restricted to the United States (explicitly stated), which may bias what is considered common knowledge and affect annotations.

**Potential Harm**: Detecting and reducing factual errors and hallucinations in summaries; improving evaluation of factuality and controllability in summarization systems.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
