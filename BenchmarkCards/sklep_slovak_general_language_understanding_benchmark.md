# skLEP (Slovak General Language Understanding Benchmark)

## 📊 Benchmark Details

**Name**: skLEP (Slovak General Language Understanding Benchmark)

**Overview**: skLEP is the first comprehensive benchmark specifically designed for evaluating Slovak natural language understanding (NLU) models, encompassing nine diverse tasks for thorough assessment of model capabilities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Slovak

**Resources**:
- [GitHub Repository](https://github.com/slovak-nlp/sklep)

## 🎯 Purpose and Intended Users

**Goal**: To foster the evaluation and development of language models specifically for the Slovak language through a standardized benchmark.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Token Classification
- Named Entity Recognition
- Textual Entailment
- Natural Language Inference
- Semantic Textual Similarity
- Hate Speech Classification
- Sentiment Analysis
- Question Answering

**Limitations**: Some tasks within each category are relatively similar, and additional NLP tasks for Slovak are constrained by dataset availability.

## 💾 Data

**Source**: Curated from original datasets and established English resources translated and annotated for Slovak with native speaker post-editing.

**Size**: 9 tasks

**Format**: Various (Task-specific)

**Annotation**: Manual annotation with native speaker post-editing for translated datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Macro F1
- Accuracy
- Pearson Correlation

**Calculation**: Relative Error Reduction (RER) comparisons against a baseline model for scoring across tasks.

**Interpretation**: Performance is interpreted in relation to task-specific metrics, emphasizing a rigorous hyperparameter grid search for each model.

**Baseline Results**: SlovakBERT serves as a baseline for comparison, with detailed performance metrics across tasks.

**Validation**: Extensive hyperparameter search from training across models to validate robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes Slovak-specific considerations but does not provide extensive demographic breakdowns.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All benchmark datasets are sourced from public repositories and are licensed for academic research.

**Data Licensing**: Predominantly released under Creative Commons licenses and managed for public access upon acceptance.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
