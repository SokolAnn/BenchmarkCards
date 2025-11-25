# BATCH SAFEBENCH

## 📊 Benchmark Details

**Name**: BATCH SAFEBENCH

**Overview**: BATCH SAFEBENCH is a benchmark dataset designed to evaluate the vulnerability of large language models (LLMs) to batch prompting attacks, comprising 150 attack instructions and 8,000 batch instances. It systematically examines how malicious inputs can influence LLM outputs across various scenarios.

**Data Type**: batch prompting instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/MurongYue/BatchSafeBench)
- [GitHub Repository](https://github.com/MurongYue/BatchSafeBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary goal of BATCH SAFEBENCH is to systematically assess the security vulnerabilities in batch prompting techniques used with large language models and to encourage the development of defenses against these vulnerabilities.

**Target Audience**:
- ML Researchers
- Security Researchers
- Model Developers

**Tasks**:
- Security Evaluation
- Adversarial Testing

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from the GSM8k and HotpotQA datasets where batch instances are generated based on predefined attack instructions.

**Size**: 8,000 batch instances

**Format**: JSON

**Annotation**: Manual generation of attack instructions using a meta prompt followed by selection of examples from existing datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Attack Success Rate (ASR)

**Calculation**: Accuracy is calculated based on correct answers excluding appended malicious content. Attack Success Rate is determined through customized ground truth for various attack scenarios.

**Interpretation**: A higher accuracy indicates better performance against prompts, while a higher ASR indicates greater vulnerability to attacks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Accuracy

**Atlas Risks**:
- **Accuracy**
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: ['The benchmark identifies how batch prompting can lead to the spread of harmful or misleading information through improper model responses.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
