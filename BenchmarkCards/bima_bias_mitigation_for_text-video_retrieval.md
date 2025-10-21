# BiMa (Bias Mitigation for Text-Video Retrieval)

## 📊 Benchmark Details

**Name**: BiMa (Bias Mitigation for Text-Video Retrieval)

**Overview**: BiMa is a novel framework designed to mitigate biases in both visual and textual representations within text-video retrieval (TVR) systems. It integrates scene elements into video embeddings and introduces a mechanism for disentangling text features into content and bias components, enhancing model performance and robustness against biases.

**Data Type**: text-video pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MSR-VTT
- MSVD
- LSMDC
- ActivityNet
- DiDeMo

**Resources**:
- [Resource](https://arxiv.org/abs/2506.03589)

## 🎯 Purpose and Intended Users

**Goal**: To advance generalization and robustness in text-video retrieval by mitigating dataset-specific biases through innovative techniques.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text-Video Retrieval

**Limitations**: Despite efforts, some inherent biases may remain unmitigated.

## 💾 Data

**Source**: Five major TVR benchmarks: MSR-VTT, MSVD, LSMDC, ActivityNet, and DiDeMo

**Size**: 118,081 video clips

**Format**: Various (specific formats not detailed)

**Annotation**: A comprehensive taxonomy dictionary of scene elements was constructed from multiple datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Recall at Rank 1
- Recall at Rank 5
- Recall at Rank 10

**Calculation**: Accuracy is calculated based on the rank of retrieved videos in relation to textual queries.

**Interpretation**: Higher Recall at Rank metrics indicate better performance in retrieving relevant videos to the provided textual queries.

**Baseline Results**: Comparison with existing benchmarks demonstrates BiMa achieving state-of-the-art results across multiple datasets.

**Validation**: Validated through extensive experiments and ablation studies measuring performance improvements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Does not include analysis related to demographics; the focus is on bias mitigation in a general sense.

**Potential Harm**: ['Model overfitting to specific biases in datasets.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
