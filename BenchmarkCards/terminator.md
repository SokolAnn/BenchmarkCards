# TERMinator

## 📊 Benchmark Details

**Name**: TERMinator

**Overview**: This paper is devoted to the extraction of entities and semantic relations between them from scientific texts. We present a dataset that includes annotations for two tasks and develop a system called TERMinator for the study of the influence of language models on term recognition and comparison of different approaches for relation extraction.

**Data Type**: text (annotated scientific terms and relation labels)

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- Russian

**Similar Benchmarks**:
- SciERC

**Resources**:
- [GitHub Repository](https://github.com/iis-research-team/terminator)
- [GitHub Repository](https://github.com/iis-research-team/ruserrc-dataset)
- [Resource](https://arxiv.org/abs/2209.14854)

## 🎯 Purpose and Intended Users

**Goal**: Provide a new dataset for term recognition and relation extraction in Russian scientific texts and develop the TERMinator tool to study the influence of language models and compare approaches for relation extraction.

**Target Audience**:
- Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Relation Extraction

**Limitations**: Markup quality significantly affects performance; dataset size is limited (some relation classes have very few examples); some relations are implicit making them difficult to annotate and detect; as far as the authors know this is the first corpus for scientific texts in Russian, making direct comparison to prior work difficult.

## 💾 Data

**Source**: Abstracts of scientific papers on Information Technology (computer science) in Russian.

**Size**: 136 training texts and 80 test texts; 12,809 training tokens and 11,157 test tokens; 2,028 training terms and 2,027 test terms; 356 training relations and 620 test relations.

**Format**: N/A

**Annotation**: Entities annotated in BIO format with tags B-TERM, I-TERM, O. Relations annotated with six semantic relation types: CAUSE, ISA, PART_OF, SYNONYMS, TOOL, USAGE.

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained language models (mBERT, ruBERT, rubert-tiny2) for Named Entity Recognition
- Heuristics and dictionary-based matching combined with model predictions for term extraction
- Lexical pattern matching for relation extraction
- Classification with CLS-vector (R-BERT-like) for relation extraction
- Ensemble combining model-based classification and lexical patterns

**Metrics**:
- F1 Score
- Precision
- Recall
- Exact match (full match) and Partial match for term extraction

**Calculation**: Metrics are recorded after each training epoch. Term extraction is evaluated with both exact (full) match and partial match metrics. Relation extraction is treated as a 7-class classification (CAUSE, ISA, PART_OF, SYNONYMS, TOOL, USAGE, NO-RELATION) and evaluated using Precision, Recall, and F1.

**Interpretation**: Models achieve higher scores on partial match than on exact match, indicating difficulty with exact term boundary detection. Fine-tuning on manually annotated data yields better performance than on pseudo-labeled data despite the latter being larger. Combining language models with heuristics and dictionaries can improve exact-match performance.

**Baseline Results**: Term extraction: best exact-match F1 = 0.50 (ruBERT + dictionary + heuristics); ruBERT partial-match F1 reported as 0.88 on the manually labeled set. Relation extraction: combined approach macro-average F1 = 0.29; example model results for relation extraction: mBERT F1 = 0.26, ruBERT F1 = 0.27, rubert-tiny2 F1 = 0.22.

**Validation**: Dataset split into train (136 texts) and test (80 texts) used for evaluation. For relation extraction, authors trained on the corpus without a separate validation set and selected the number of epochs experimentally due to very few examples for some relations. They also used experimental selection of maximum context length for pattern matching.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
