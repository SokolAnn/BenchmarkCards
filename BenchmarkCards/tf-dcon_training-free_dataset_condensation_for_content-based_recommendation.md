# TF-DCon (Training-Free Dataset Condensation for Content-based Recommendation)

## 📊 Benchmark Details

**Name**: TF-DCon (Training-Free Dataset Condensation for Content-based Recommendation)

**Overview**: TF-DCon is a novel training-free dataset condensation method designed for content-based recommendation (CBR). It synthesizes a compact dataset that maintains the performance of models comparable to those trained on large datasets, notably reducing dataset size while preserving user preference information.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2310.09874)

## 🎯 Purpose and Intended Users

**Goal**: To create a compact dataset for content-based recommendation that retains performance while being significantly smaller than the original datasets.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Content-based Recommendation

**Limitations**: The performance can be unstable when utilizing ChatGPT for the pre-process due to network latency.

## 💾 Data

**Source**: Real-world datasets including MIND, Goodreads, and MovieLens.

**Size**: Condensed the size of original datasets by up to 95%.

**Format**: N/A

**Annotation**: Utilizes ChatGPT for interest extraction and item content condensation.

## 🔬 Methodology

**Methods**:
- ChatGPT for content condensation
- Clustering-based synthesis for user interactions

**Metrics**:
- NDCG@K
- Recall@K

**Calculation**: The metrics are calculated based on model performance on original datasets relative to those on condensed datasets.

**Interpretation**: Higher NDCG and Recall indicate better performance of the recommendation models.

**Baseline Results**: Achieved up to 97% of original performance while reducing dataset size by 95%.

**Validation**: Extensive experiments conducted on multiple datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Efficiency
- Data Quality

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
