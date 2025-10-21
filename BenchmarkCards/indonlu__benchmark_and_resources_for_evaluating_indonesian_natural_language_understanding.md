# IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding

## 📊 Benchmark Details

**Name**: IndoNLU: Benchmark and Resources for Evaluating Indonesian Natural Language Understanding

**Overview**: IndoNLU is a comprehensive benchmark for training, evaluation, and benchmarking on Indonesian natural language understanding tasks, consisting of twelve diverse tasks ranging from single sentence classification to pair-sentences sequence labeling.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Indonesian

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- CLUE

**Resources**:
- [Resource](https://indobenchmark.com/)

## 🎯 Purpose and Intended Users

**Goal**: To establish a standardized benchmark for Indonesian natural language understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Emotion Classification
- Sentiment Analysis
- Aspect-Based Sentiment Analysis
- Named Entity Recognition
- Part-of-Speech Tagging
- Textual Entailment
- Span Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Collection from various existing datasets covering tasks in Indonesian NLP.

**Size**: 23 GB

**Format**: text

**Annotation**: Annotated by experts and linguists.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Calculated using macro-averaged F1 score for classification tasks and word-level sequence labeling F1 score for sequence labeling tasks.

**Interpretation**: A higher F1 score indicates better model performance on the benchmark tasks.

**Baseline Results**: Baseline models provided for each task, including IndoBERT and IndoBERT-lite variants.

**Validation**: Standardized evaluation set for reproducibility.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures for data handling are incorporated based on data sources.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
