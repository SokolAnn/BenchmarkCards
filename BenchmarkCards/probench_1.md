# ProBench

## 📊 Benchmark Details

**Name**: ProBench

**Overview**: ProBench is a benchmark of open-ended user queries that require professional expertise and advanced reasoning, consisting of 4,000 samples across 10 fields and 56 sub-fields, evaluated utilizing MLLM-as-a-Judge.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://yan98.github.io/ProBench/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multimodal large language models (MLLMs) through professional queries that necessitate expert-level knowledge.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced queries from professionals in various fields

**Size**: 4,000 samples

**Format**: N/A

**Annotation**: Manually curated by professionals in their respective domains

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Average Precision (mAP)
- Precision
- Recall

**Calculation**: Calculated based on the output of MLLM-as-a-Judge compared against human evaluations for each task and query.

**Interpretation**: Higher scores indicate better model performance in classifying and generating responses to queries.

**Baseline Results**: N/A

**Validation**: Pairwise comparisons against multiple leading models to ensure robustness and accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential bias in the benchmark tasks affecting model evaluation.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected with explicit user consent.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
