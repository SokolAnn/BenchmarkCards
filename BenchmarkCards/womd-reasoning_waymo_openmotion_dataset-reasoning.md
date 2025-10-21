# WOMD-Reasoning (Waymo OpenMotion Dataset-Reasoning)

## 📊 Benchmark Details

**Name**: WOMD-Reasoning (Waymo OpenMotion Dataset-Reasoning)

**Overview**: WOMD-Reasoning is a comprehensive large-scale Q&As dataset built on WOMD focusing on describing and reasoning traffic rule-induced interactions in driving scenarios. It presents the largest multi-modal Q&A dataset, with 3 million Q&As on real-world driving scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- BDD-X
- DriveLM
- nuScenes-QA

**Resources**:
- [Resource](https://waymo.com/open/download/)
- [GitHub Repository](https://github.com/yhli123/WOMD-Reasoning)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of WOMD-Reasoning is to provide a detailed dataset for interaction reasoning in driving, focusing on traffic rule-induced interactions and human intentions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Interaction Reasoning
- Scene Description
- Motion Prediction
- Traffic Rule Compliance Planning

**Limitations**: N/A

## 💾 Data

**Source**: WOMD (Waymo Open Motion Dataset)

**Size**: 3,000,000 Q&As

**Format**: JSON

**Annotation**: Automated data curation using GPT-4 and rule-based translations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE
- BLEU
- METEOR
- CIDEr
- SPICE
- GPT Score

**Calculation**: Metrics are calculated based on the generated answers to the questions in the WOMD-Reasoning dataset.

**Interpretation**: High scores in metrics indicate good performance in answering driving-related questions accurately.

**Baseline Results**: Fine-tuned Multi-modal models showed improvement over baseline models in performance across various metrics.

**Validation**: Human evaluation confirmed an accuracy of approximately 91.99% across interaction analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
