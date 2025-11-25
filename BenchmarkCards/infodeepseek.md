# InfoDeepSeek

## 📊 Benchmark Details

**Name**: InfoDeepSeek

**Overview**: InfoDeepSeek is a benchmark for evaluating agentic information seeking in dynamic web environments, featuring challenging queries and fine-grained metrics for assessing the effectiveness of information seeking.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English
- Chinese
- Japanese
- Russian
- Korean
- Italian
- Arabic
- French
- Spanish
- German
- Portuguese
- Icelandic
- Slovene
- Malay
- Bengali
- Croatian
- Czech
- Dutch
- Hindi

**Resources**:
- [Resource](https://infodeepseek.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of agentic systems in their ability to seek information in dynamic web environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually curated high-quality questions from web sources.

**Size**: 245 validated questions

**Format**: N/A

**Annotation**: Each question was verified by multiple annotators for determinacy, difficulty, and other criteria.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated evaluation using LLMs

**Metrics**:
- Answer Accuracy (ACC)
- Information Accuracy (IA@k)
- Effective Evidence Utilization (EEU)
- Information Compactness (IC)

**Calculation**: Metrics calculated based on correctness of LLM-generated answers against ground-truth answers.

**Interpretation**: High metrics indicate better performance in agentic information seeking tasks.

**Baseline Results**: N/A

**Validation**: Questions were validated through multiple perspectives and confirmed by independent annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy
- Robustness
- Misinformation

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Exposing personal information
- **Robustness**: Data poisoning
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
