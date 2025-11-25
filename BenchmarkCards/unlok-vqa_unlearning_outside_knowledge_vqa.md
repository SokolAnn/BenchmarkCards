# UnLOK-VQA (Unlearning Outside Knowledge VQA)

## 📊 Benchmark Details

**Name**: UnLOK-VQA (Unlearning Outside Knowledge VQA)

**Overview**: UnLOK-VQA is a benchmark specifically designed for evaluating the targeted erasure of pretrained multimodal information from Multimodal Large Language Models (MLLMs). It involves high-quality, well-annotated image-text pairs to assess the effectiveness of unlearning methods against adversarial attacks.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Vaidehi99/UnLOK-VQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate a comprehensive evaluation of unlearning in Multimodal Large Language Models (MLLMs) and serve as a challenging benchmark for future research in unlearning.

**Target Audience**:
- ML Researchers
- AI Safety Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Information Deletion

**Limitations**: N/A

## 💾 Data

**Source**: Automated generation and manual filtering using the OK-VQA dataset.

**Size**: 500 samples

**Format**: JSON

**Annotation**: Manual filtering by human evaluators to retain high-quality samples.

## 🔬 Methodology

**Methods**:
- Experimental evaluation against whitebox and blackbox attacks
- Manual evaluation of dataset quality

**Metrics**:
- Attack Success Rates
- Rewrite Score
- Neighborhood ∆-Accuracy

**Calculation**: Attack success rates represent the percentage of successful extractions by the adversarial attacks during evaluation.

**Interpretation**: Lower attack success rates and higher rewrite scores indicate better performance of the unlearning methods.

**Validation**: Manual filtering to ensure dataset quality through human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Our work aims to mitigate risks related to sensitive information leakage from MLLMs.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
