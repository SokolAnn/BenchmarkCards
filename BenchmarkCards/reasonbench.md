# ReasonBench

## 📊 Benchmark Details

**Name**: ReasonBench

**Overview**: ReasonBench is the first evaluation benchmark focused on structured graphic reasoning tasks, which includes 1,613 questions from real-world intelligence tests. It evaluates VLMs' performance in complex graphic reasoning, covering dimensions related to location, attribute, quantity, and multi-element tasks.

**Data Type**: question-answering pairs

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- CLEVR
- Raven
- Mensa

**Resources**:
- [Resource](https://huggingface.co/datasets/cistine/ReasonBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ReasonBench is to evaluate visual language models' (VLMs) capabilities in structured graphic reasoning tasks, identifying limitations and improving their performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Complex Graphic Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of 1,613 standardized test problems gathered from various human intelligence tests such as Chinese Civil Service Aptitude Tests, Mensa Tests, and Raven’s Progressive Matrices.

**Size**: 1,613 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluation based on a triple-controlled evaluation protocol ensuring measurement reliability and cross-model comparability.

**Interpretation**: Results are interpreted based on comparison to human-level performance and existing models.

**Baseline Results**: Human participants achieve an average accuracy of 68.7% on the test set.

**Validation**: Standardized evaluation protocol based on Pass@1 single-attempt scoring.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
