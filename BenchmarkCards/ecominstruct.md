# EcomInstruct

## 📊 Benchmark Details

**Name**: EcomInstruct

**Overview**: EcomInstruct is the first E-commerce instruction dataset, comprising 2.5 million instruction data and 134 tasks, designed to enhance generalization capabilities for E-commerce specific tasks.

**Data Type**: instruction data and atomic tasks

**Domains**:
- Natural Language Processing
- E-commerce

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/Alibaba-NLP/EcomGPT)

## 🎯 Purpose and Intended Users

**Goal**: To provide an instruction-tuning dataset tailored for E-commerce tasks and improve the generalization ability of models in the E-commerce domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Question Answering
- Text Generation
- Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various academic websites and data competition platforms, as well as atomic tasks constructed using E-commerce data.

**Size**: 2.5 million instruction examples

**Format**: N/A

**Annotation**: Manually curated and automatically generated using ChatGPT

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Micro F1
- Macro F1
- ROUGE-L

**Calculation**: Metrics are calculated based on model output compared to ground truth.

**Interpretation**: Higher scores indicate better performance in the tasks undertaken by the model.

**Baseline Results**: ChatGPT, BLOOM, and BLOOMZ serve as baseline comparisons.

**Validation**: Cross-dataset evaluation on various unseen tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
