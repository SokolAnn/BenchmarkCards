# NorBench – A Benchmark for Norwegian Language Models

## 📊 Benchmark Details

**Name**: NorBench – A Benchmark for Norwegian Language Models

**Overview**: We present NorBench: a streamlined suite of NLP tasks and probes for evaluating Norwegian language models (LMs) on standardized data splits and evaluation metrics. NorBench collects a broad range of annotated datasets, provides precise task definitions, pre-defined data splits and evaluation metrics, and evaluation scripts to streamline benchmarking of Norwegian LMs.

**Data Type**: text (token-level annotations, named-entity labels, document- and sentence-level sentiment annotations, targeted sentiment spans, grammaticality sentences, extractive question-answering pairs, parallel Bokmål–Nynorsk sentence pairs, diagnostic masked-completion templates for bias and harmfulness)

**Domains**:
- Natural Language Processing

**Languages**:
- Norwegian (Bokmål)
- Norwegian (Nynorsk)

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- ScandEval

**Resources**:
- [GitHub Repository](https://github.com/ltgoslo/norbench)
- [GitHub Repository](https://github.com/ltgoslo/norne)
- [GitHub Repository](https://github.com/ltgoslo/norec_sentence)
- [GitHub Repository](https://github.com/ltgoslo/norec_tsa)
- [GitHub Repository](https://github.com/ltgoslo/NorQuAD)
- [Resource](https://huggingface.co/datasets/NbAiLab/NCC)
- [GitHub Repository](https://github.com/huggingface/tokenizers)

## 🎯 Purpose and Intended Users

**Goal**: Provide a suite of standardized benchmark tasks, pre-defined data splits, evaluation metrics, and scripts to enable simple, fair and standardized comparison between Norwegian language models.

**Target Audience**:
- NLP Practitioners
- Model Developers
- ML Researchers
- Domain Experts interested in Norwegian NLP

**Tasks**:
- Part-of-Speech Tagging (UPOS)
- Morphological Feature Tagging (UFeats)
- Lemmatization
- Dependency Parsing
- Named Entity Recognition
- Sentiment Analysis (Document-level)
- Sentiment Analysis (Sentence-level)
- Targeted Sentiment Analysis
- Grammaticality Judgment / Linguistic Acceptability (binary classification)
- Extractive Question Answering
- Machine Translation (Bokmål to Nynorsk)
- Bias and Toxicity Probing / Diagnostic Probes (gender-bias and harmfulness)

**Limitations**: Currently does not include some additional annotated tasks the authors plan to add in future work (explicitly mentioned: coreference resolution based on NARC, negation resolution based on NoReC neg, and sequence-generation tasks such as summarization and prompt-based few-shot evaluation).

## 💾 Data

**Source**: Collection of annotated Norwegian datasets used in NorBench, including: Norwegian Universal Dependencies Treebank (UD/NDT), NorNE (NER annotations on UD/NDT), Norwegian Review Corpus (NoReC) and derived sentence and targeted sentiment subsets (NoReC sentence, NoReC tsa), NoCoLA (linguistic acceptability), NorQuAD (extractive QA), Bokmål–Nynorsk parallel bitexts for machine translation, and diagnostic templates for gender-bias and harmfulness probing.

**Size**: Various per dataset. Explicit counts reported in the paper: UD tokens — 489,217 (train), 67,619 (dev), 54,739 (test); Named Entities — 23,071 (train), 2,942 (dev), 2,393 (test); Sentiment analysis documents — 34,903 (train), 4,360 (dev), 4,351 (test); Sentiment sentences — 7,973 (train), 1,411 (dev), 1,181 (test); Sentiment targets — 5,044 (train), 877 (dev), 735 (test); NoCoLA sentences — 116,195 (train), 14,289 (dev), 14,383 (test); NorQuAD questions — 3,808 (train), 472 (dev), 472 (test); Bokmål–Nynorsk parallel sentences — 10,000 (train), 10,000 (dev), 10,000 (test).

**Format**: N/A

**Annotation**: Combination of manual/human annotation and derived annotations as described in the paper: NorQuAD question-answer pairs are manually created; NorNE provides NER annotations on UD/NDT; NoReC reviews originate from professional reviews with numeric ratings (mapped to ternary sentiment classes); other datasets are described as human-annotated or derived as explained in the paper.

## 🔬 Methodology

**Methods**:
- Automated metrics-based evaluation
- Standard fine-tuning evaluation pipelines (encoder-only and encoder-decoder fine-tuning)
- Multi-task fine-tuning for UD tasks (UDify-style)
- Sequence labeling with BIO for NER and TSA
- SQuAD-style fine-tuning for extractive QA
- Generative evaluation for machine translation with greedy decoding
- Probing via masked-language templates for gender-bias and harmfulness (HONEST/HurtLex-based scoring)

**Metrics**:
- Accuracy (token-wise)
- Micro F1 (strict entity-level for NER)
- Macro F1 (sentiment tasks)
- Matthews Correlation Coefficient (MCC) for linguistic acceptability
- Token-level F1 for extractive QA
- Labeled Attachment Score (LAS) for dependency parsing
- SacreBLEU (BLEU) for machine translation
- HONEST score for harmfulness (hurtful completions)
- Normative and Descriptive occupational bias scores (Touileb et al., 2023)

**Calculation**: NER: strict micro F1 requiring correct entity type and exact boundary match computed using SemEval'13 Task 9 code. Dependency parsing: Labeled Attachment Score (LAS). Lemmatization: aggregated token-wise exact match accuracy. Sentiment metrics: macro F1. NoQuAD: token-level F1. Machine translation: SacreBLEU with BLEU no smoothing, 13a tokenization, no lowercasing (torchmetrics defaults as used). Harmfulness: HONEST computed over top-k completions per template. Normative and descriptive bias scores computed as defined in Touileb et al. (2023). Reported results are means with standard deviations over 5 runs for many experiments.

**Interpretation**: The authors advise against aggregating across tasks; instead, interpretation focuses on per-task performance. Higher metric values per task indicate better performance on that specific ability. The benchmark reports mean and standard deviation over multiple runs to assess stability.

**Baseline Results**: Baseline and comparative results are provided in the paper (Tables 3 and 4). Summary: NorBERT 3 (large, 353M) attains highest scores across most encoder-only tasks; NorT5-large performs best among encoder-decoder models. The paper reports per-model, per-task metrics (means and standard deviations over 5 runs).

**Validation**: Datasets come with pre-defined training, development, and test splits. Reported experimental results use mean and standard deviation across 5 runs for stability. Evaluation scripts and standardized splits are provided in the NorBench repository to ensure reproducible evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Output bias
- **Value Alignment**: Toxic output, Harmful output

**Demographic Analysis**: The paper reports descriptive and normative occupational bias scores and provides breakdowns for gender-dominated and gender-neutral occupations (per-gender descriptive scores: Neutral, Female, Male).

**Potential Harm**: ['Detection of gender bias in occupational associations (normative and descriptive occupational bias scores)', 'Detection/measurement of harmful or toxic sentence completions via HONEST scoring (HurtLex-based)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
