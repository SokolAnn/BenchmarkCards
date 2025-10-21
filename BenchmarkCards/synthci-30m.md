# SynthCI-30M

## 📊 Benchmark Details

**Name**: SynthCI-30M

**Overview**: SynthCI-30M is a purely synthetic dataset comprising 30 million captioned images generated for training the SynthCLIP model, designed to study the performance of CLIP models trained on synthetic data.

**Data Type**: captioned images

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/hammoudhasan/SynthCLIP)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the performances of CLIP models trained on fully synthetic data and evaluate the feasibility of using synthetic data for scaling training datasets without human intervention.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Image Retrieval
- Text Retrieval
- Zero-shot Classification

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using text-to-image models and large language models.

**Size**: 30,000,000 captioned images

**Format**: N/A

**Annotation**: Automatically generated with no human intervention.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy
- Linear Probing
- Few-shot Performance
- Image Retrieval Performance
- Text Retrieval Performance

**Calculation**: Evaluation metrics are calculated based on downstream task performances of the SynthCLIP model.

**Interpretation**: Higher performance in retrieval and classification tasks indicates better alignment between text and image representations.

**Validation**: Models were validated through performance comparison with baselines trained on real datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
