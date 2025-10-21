# DomainVerse (A Benchmark Towards Real-World Distribution Shifts For Tuning-Free Adaptive Domain Generalization)

## 📊 Benchmark Details

**Name**: DomainVerse (A Benchmark Towards Real-World Distribution Shifts For Tuning-Free Adaptive Domain Generalization)

**Overview**: DomainVerse is a novel large-scale dataset designed to evaluate the capability of vision-language models (VLMs) in Adaptive Domain Generalization (ADG) across realistic domain shifts, consisting of approximately 0.5 million images from 390 fine-grained domains.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- Digits-five
- Office-Home
- PACS
- DomainNet
- NICO++
- OOD-CV

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate vision-language models to achieve adaptive domain generalization on realistic scenarios.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Domain Generalization

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic images generated using a game-engine-based simulator (Unity).

**Size**: 457,570 images

**Format**: N/A

**Annotation**: Automatically generated labels based on defined domain shifts.

## 🔬 Methodology

**Methods**:
- Domain CLIP
- Domain++ CLIP

**Metrics**:
- Accuracy

**Calculation**: The accuracy is computed based on prediction outcomes from the model against the ground truth.

**Interpretation**: Higher accuracy indicates better performance of the model in adapting to new domains.

**Validation**: Extensive experiments conducted to benchmark performance against existing models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
