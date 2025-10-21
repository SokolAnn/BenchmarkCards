# Assertion Messages with Large Language Models (LLMs) for Code

## 📊 Benchmark Details

**Name**: Assertion Messages with Large Language Models (LLMs) for Code

**Overview**: This paper evaluates the ability of four large language models to generate informative assertion messages in unit tests, highlighting the effectiveness of context in improving message quality.

**Data Type**: Java test methods with assertion messages

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://doi.org/10.5281/zenodo.15293133)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate large language models for generating assertion messages in unit tests and examine the impact of contextual information.

**Target Audience**:
- Software Engineers
- Researchers
- Developers

**Tasks**:
- Assertion Message Generation
- Test Code Evaluation

**Limitations**: The evaluation focuses on Java test methods containing a single assertion, limiting generalizability to more complex scenarios.

## 💾 Data

**Source**: Publicly available dataset from 20 Java projects with high-quality assertion messages.

**Size**: 216 test methods

**Format**: N/A

**Annotation**: Extracted assertion messages were manually annotated for clarity and relevance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation

**Metrics**:
- BLEU
- ROUGE-L
- METEOR
- BERTScore

**Calculation**: Metrics measure n-gram overlap and semantic similarity between generated and manual assertion messages.

**Interpretation**: Higher scores indicate better alignment with human-written assertion messages.

**Baseline Results**: Human-written assertion messages scored an average of 3.24 out of 5.

**Validation**: Systematic evaluation of multiple models against a dataset of Java test methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
