# AMBENCH

## 📊 Benchmark Details

**Name**: AMBENCH

**Overview**: A benchmark dataset of seemingly ambiguous human names, leveraging the name regularity bias phenomenon, embedded within concise text snippets and benign prompt injections. AMBENCH systematically evaluates various LLMs on their ability to detect and classify ambiguous human names.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/dzungvpham/llm-name-detection)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models on the identification and classification of ambiguous human names in text.

**Target Audience**:
- ML Researchers
- Privacy Researchers
- Model Developers

**Tasks**:
- Named Entity Recognition
- Privacy Leakage Detection

**Limitations**: N/A

## 💾 Data

**Source**: Generated via a prompt-based pipeline using real human names that resemble non-human entities, from publicly available name datasets.

**Size**: 60,000 test points

**Format**: N/A

**Annotation**: Generated using an LLM and validated for ambiguity and soundness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- False Discovery Rate (FDR)
- Privacy audit score

**Calculation**: Metrics calculated based on the percentage of ambiguous human names detected as a person’s name and measuring the accuracy of names categorized correctly.

**Interpretation**: Higher recall and lower FDR indicate better performance in detecting ambiguous names.

**Validation**: Involves systematic testing across various LLMs and human evaluation against a set of templates.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misclassification of named entities leading to privacy risks.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
