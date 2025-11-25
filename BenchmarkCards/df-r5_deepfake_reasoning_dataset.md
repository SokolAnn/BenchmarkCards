# DF-R5 (Deepfake Reasoning Dataset)

## 📊 Benchmark Details

**Name**: DF-R5 (Deepfake Reasoning Dataset)

**Overview**: DF-R5 is a reasoning-annotated dataset for deepfake detection containing approximately 115,000 images paired with high-quality explanations, designed to enhance the reasoning capabilities of multimodal large language models.

**Data Type**: image-reasoning pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/tuanrpt/PRPO)

## 🎯 Purpose and Intended Users

**Goal**: To improve deepfake detection and explanation quality through a reasoning-annotated dataset and a novel reinforcement learning approach.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Deepfake Detection
- Explainability

**Limitations**: N/A

## 💾 Data

**Source**: Images sourced from DF40 dataset, covering multiple generative domains.

**Size**: 115,000 images

**Format**: N/A

**Annotation**: High-quality explanations generated through a three-step process using multimodal large language models.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Reasoning Score

**Calculation**: Metrics such as accuracy and F1 score are calculated based on the performance of trained models on the DF-R5 dataset.

**Interpretation**: Higher scores indicate better detection accuracy and reasoning quality.

**Baseline Results**: PRPO achieves an accuracy of 89.91% and a reasoning score of 4.55/5.0.

**Validation**: Extensive experiments showing significant gains in both detection accuracy and explanation faithfulness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential misinformation and misuse in deepfake generation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
