# ReMUD (Reasoning Multimodal Ultrasound Dataset)

## 📊 Benchmark Details

**Name**: ReMUD (Reasoning Multimodal Ultrasound Dataset)

**Overview**: ReMUD is established as the first open-source medical reasoning QA supervised fine-tuning dataset specifically tailored for ultrasound, containing over 45,000 reasoning and non-reasoning Question Answering (QA) and Visual Question Answering (VQA) data.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese
- English

**Resources**:
- [GitHub Repository](https://github.com/ShiDaizi/ReMUD)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in the specific domain of medical ultrasound through a large-scale, multimodal dataset for reasoning models.

**Target Audience**:
- ML Researchers
- Domain Experts
- Medical Professionals

**Tasks**:
- Question Answering
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available ultrasound materials, including textbooks, clinical guidelines, and datasets sourced from the internet.

**Size**: 45,000+ examples

**Format**: JSON

**Annotation**: Automatically generated VQA triplets using multimodal language models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- pass@1

**Calculation**: pass@1 is calculated as the average proportion of correct responses among generated answers.

**Interpretation**: Higher pass@1 values indicate better model performance in selecting correct answers.

**Validation**: The validation procedures include quality checks using scoring systems to assess the accuracy of generated data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
