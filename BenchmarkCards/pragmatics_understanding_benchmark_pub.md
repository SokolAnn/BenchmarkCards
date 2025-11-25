# Pragmatics Understanding Benchmark (PUB)

## 📊 Benchmark Details

**Name**: Pragmatics Understanding Benchmark (PUB)

**Overview**: PUB is designed to assess the pragmatic capabilities of large language models (LLMs) through 14 tasks covering four pragmatics phenomena: Implicature, Presupposition, Reference, and Deixis, consisting of 28,000 data points.

**Data Type**: multiple choice question answers

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/cfilt/PUB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLM's ability to handle real-world language tasks that require pragmatic reasoning.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Implicature understanding
- Presupposition detection
- Reference resolution
- Deixis analysis

**Limitations**: While the benchmark is carefully constructed, there might be biases present that could affect evaluations. Models are sensitive to prompt variations, which can lead to inconsistent performance.

## 💾 Data

**Source**: The dataset consists of curated tasks focusing on Implicature, Presupposition, Reference, and Deixis, with both newly annotated and adapted examples.

**Size**: 28,000 examples

**Format**: MCQA

**Annotation**: 6,100 examples are newly annotated, while the rest are adapted from existing datasets.

## 🔬 Methodology

**Methods**:
- Multiple Choice Prompting
- Cloze prompting

**Metrics**:
- Accuracy

**Calculation**: Models are evaluated using length normalized Cloze prompting and Multiple Choice Prompting, measuring their performance on tasks.

**Interpretation**: Models' performance is compared against human evaluators to assess understanding of pragmatic tasks.

**Validation**: Results are validated through human evaluation with a total of 4,200 samples assessed by three independent evaluators for each task.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
