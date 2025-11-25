# MoZIP (Multilingual Benchmark to Evaluate Large Language Models in Intellectual Property)

## 📊 Benchmark Details

**Name**: MoZIP (Multilingual Benchmark to Evaluate Large Language Models in Intellectual Property)

**Overview**: MoZIP is the first multilingual benchmark for the evaluation of large language models in the intellectual property (IP) domain. It includes three distinct tasks: IP multiple-choice quiz (IPQuiz), IP question answering (IPQA), and patent matching (PatentMatch).

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- German
- French
- Russian
- Japanese
- Spanish
- Korean
- Portuguese

**Resources**:
- [GitHub Repository](https://github.com/AI-for-Science/MoZi)
- [Resource](https://huggingface.co/datasets/BNNT/IPQuizDataset)
- [Resource](https://huggingface.co/datasets/BNNT/IPQA)
- [Resource](https://huggingface.co/datasets/BNNT/PatentMatch)

## 🎯 Purpose and Intended Users

**Goal**: To serve as a standardized benchmark for evaluating large language models in the intellectual property (IP) domain.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Multiple Choice Question Answering
- Question Answering
- Patent Matching

**Limitations**: N/A

## 💾 Data

**Source**: Datasets were constructed from various sources, including patents, IP acts, and frequently asked questions related to IP.

**Size**: 2,000 multiple-choice questions, 100 IPQA questions, 1,000 PatentMatch questions

**Format**: JSON

**Annotation**: The data was manually verified and curated from reliable sources.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance of models on the MoZIP benchmark tasks.

**Interpretation**: Higher accuracy indicates better understanding and completion of IP-related tasks.

**Baseline Results**: ChatGPT performs best overall, followed by MoZi-7b, BLOOMZ-7b, BELLE-7b, and ChatGLM-6b.

**Validation**: Models were evaluated and compared on performance metrics against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data used is publicly available and does not involve personal privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collection complies with relevant regulations.
