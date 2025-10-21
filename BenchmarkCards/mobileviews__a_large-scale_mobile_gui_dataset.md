# MobileViews: A Large-Scale Mobile GUI Dataset

## 📊 Benchmark Details

**Name**: MobileViews: A Large-Scale Mobile GUI Dataset

**Overview**: MobileViews is the largest mobile screen dataset, including over 600K screenshot-view hierarchy pairs from more than 20K modern Android apps. It aims to help enhance mobile screen assistants by providing a comprehensive and diverse dataset for training.

**Data Type**: screenshot-view hierarchy pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Rico

**Resources**:
- [Resource](https://huggingface.co/datasets/mllmTeam/MobileViews)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality mobile screen dataset to enhance the capabilities of mobile screen assistants by training multimodal LLMs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Screen Question Answering
- Tappability Prediction
- Element Relationship Prediction
- UI Component Identification

**Limitations**: N/A

## 💾 Data

**Source**: Mobile screen data collected using a highly parallelized, LLM-enhanced automatic app interaction approach.

**Size**: 1,103,481 screenshots and view hierarchies

**Format**: N/A

**Annotation**: LLM-enhanced automatic annotation with minimal human intervention.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation
- LoRA fine-tuning

**Metrics**:
- Binary F1 Score
- Multi-class F1 Score
- SQuAD F1 Score

**Calculation**: Metrics calculated based on model performance across various tasks, including element-level assessments.

**Interpretation**: Higher scores indicate better performance in tasks such as tappability prediction and screen question answering.

**Validation**: Models validated using standard train/test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset does not contain subjective individual personal data.

**Data Licensing**: Open-sourced dataset under appropriate usage policies.

**Consent Procedures**: Manual accounts created to ensure compliance with app usage policies.

**Compliance With Regulations**: Not Applicable
