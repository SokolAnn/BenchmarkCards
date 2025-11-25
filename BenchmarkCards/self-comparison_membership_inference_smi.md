# Self-Comparison Membership Inference (SMI)

## 📊 Benchmark Details

**Name**: Self-Comparison Membership Inference (SMI)

**Overview**: This paper proposes a novel dataset-level membership inference method based on Self-Comparison, aiming to detect unauthorized usage of copyrighted materials in large language models (LLMs) and vision-language models (VLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a method for dataset-level membership inference without requiring access to ground-truth member or non-member data in identical distribution.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Membership Inference

**Limitations**: N/A

## 💾 Data

**Source**: Generated or processed text data derived from various public and proprietary datasets used in LLMs and VLMs.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics were calculated based on changes in average negative log-likelihood (A-NLL) before and after paraphrasing, and hypothesis testing was used to infer membership.

**Interpretation**: An increase in A-NLL indicates that the data is more likely to be part of the training set.

**Baseline Results**: SMI outperformed traditional membership inference methods on various models and datasets, achieving an average F1 score of 0.984 across assessed scenarios.

**Validation**: The benchmark was validated through extensive experiments across various datasets and models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark does not require access to ground-truth data, thereby improving privacy by avoiding the need to handle sensitive training material directly.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
