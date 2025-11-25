# TituLLMs Benchmarking Datasets

## 📊 Benchmark Details

**Name**: TituLLMs Benchmarking Datasets

**Overview**: We developed five benchmarking datasets to evaluate LLMs, particularly focusing on assessing world knowledge, commonsense reasoning, and reading comprehension specific to the Bangla language.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Bangla

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/hishab-nlp/titulm)

## 🎯 Purpose and Intended Users

**Goal**: To establish comprehensive benchmarking datasets for evaluating LLMs in their capacity to understand and generate Bangla.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering
- Commonsense Reasoning
- Reading Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from various educational websites, textbooks, and synthesized data generation.

**Size**: 132k entries

**Format**: N/A

**Annotation**: Manual and automated methods including novel translation techniques.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Normalized accuracy

**Calculation**: Metrics were calculated using the lm-evaluation-harness.

**Interpretation**: Higher accuracy indicates better understanding of Bangla language tasks.

**Baseline Results**: N/A

**Validation**: Validation set sampled proportionally to maintain data heterogeneity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
