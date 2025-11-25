# SEGSUB

## 📊 Benchmark Details

**Name**: SEGSUB

**Overview**: SEGSUB is a framework for applying targeted image perturbations to investigate vision-language model resilience against knowledge conflicts, generating a benchmark dataset with over 35,000 systematically perturbed samples to measure susceptibility to hallucination.

**Data Type**: image-question-answer pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/CASOS-IDeaS-CMU/SebSub)
- [Resource](https://www.doi.org/10.1184/R1/28297076)

## 🎯 Purpose and Intended Users

**Goal**: To improve robustness in vision-language models against knowledge conflicts and hallucinations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Augmented from WebQA, VQAv2, and OK-VQA datasets with knowledge conflicts.

**Size**: 35,225 samples

**Format**: N/A

**Annotation**: Quality-checked through visual inspection.

## 🔬 Methodology

**Methods**:
- Model fine-tuning
- Image perturbation

**Metrics**:
- Accuracy

**Calculation**: Accuracy measured as the percentage of correct responses acknowledging knowledge conflicts.

**Interpretation**: Lower accuracy indicates higher susceptibility to hallucinations.

**Validation**: Models validated on both original and perturbed datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: plagiarism
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
