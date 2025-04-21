# GLUE-X

## 📊 Benchmark Details

**Name**: GLUE-X

**Overview**: GLUE-X is a benchmark for evaluating out-of-distribution (OOD) robustness in NLP models, incorporating 15 publicly available datasets across 8 NLP tasks to assess model generalization to unseen data distributions.

**Data Type**: Text

**Domains**:
- Sentiment Analysis
- Natural Language Inference
- Textual Entailment
- Paraphrase Recognition
- Textual Similarity
- Linguistic Acceptability
- Question Answering

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SuperGLUE

**Resources**:
- [Resource](https://gluexbenchmark.com/)
- [GitHub Repository](https://github.com/YangLinyi/GLUE-X)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research on OOD generalization in NLP models by providing a consistent evaluation framework.

**Target Audience**:
- NLP researchers
- AI developers
- Academics

**Tasks**:
- Evaluate OOD performance of NLP models
- Analyze model generalization capabilities
- Compare performance across different NLP tasks

**Limitations**: Focus primarily on text classification tasks; other NLP tasks like generation are out of scope.

**Out of Scope Uses**:
- Machine translation
- Dialogue systems

## 💾 Data

**Source**: Publicly available datasets across various domains.

**Size**: Varies by dataset, with some datasets containing millions of examples.

**Format**: Structured text for classification tasks.

**Annotation**: Datasets are curated to ensure consistency in task definitions and output labels.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Linear Probing
- Linear Probing then Fine-tuning (LP-FT)

**Metrics**:
- Average accuracy for OOD performance on various tasks
- Friedman rank for model comparisons

**Calculation**: Average scores across multiple tasks to assess overall performance.

**Interpretation**: Performance decay is measured by the difference between in-distribution and out-of-distribution accuracy.

**Baseline Results**: Average human performance observed at 80.14% compared to model scores.

**Validation**: Results validated through comparisons against human performance and standard benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Datasets are derived from publicly available sources; no private data used.

**Data Licensing**: Open-sourced under CC-BY-NC-SA license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
