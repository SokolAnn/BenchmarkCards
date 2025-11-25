# SVTA (Synthetic Video-Text Anomaly benchmark)

## 📊 Benchmark Details

**Name**: SVTA (Synthetic Video-Text Anomaly benchmark)

**Overview**: We introduce SVTA, the first large-scale dataset for cross-modal anomaly retrieval, leveraging generative models to produce a dataset with 41,315 video-text pairs, covering 68 anomaly types and 30 normal activities to address data scarcity and privacy concerns.

**Data Type**: video-text pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- UCF-Crime
- UCFCrime-AR
- UBnormal
- OOPS!

**Resources**:
- [Resource](https://svta-mm.github.io/SVTA.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale synthetic benchmark for video anomaly retrieval using natural language queries.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Anomaly Retrieval
- Cross-Modal Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic video generation from Large Language Models and video generative models.

**Size**: 41,315 videos (1.36M frames)

**Format**: N/A

**Annotation**: Generated cybernetically, with category labels assigned by LLMs and human validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall@K (R@1, R@5, R@10)
- Median Rank (MdR)
- Mean Rank (MnR)

**Calculation**: Metrics are calculated based on retrieval performance comparing text queries and video outputs.

**Interpretation**: Higher Recall@K indicates better retrieval performance while lower Median and Mean Rank indicates better relevance in ranking.

**Baseline Results**: CLIP4Clip achieved R@1 of 55.4% for T2V retrieval.

**Validation**: The dataset is divided into training, validation, and test sets with a ratio of 7:1:2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Videos are generated with age, gender, and environmental diversity considerations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Synthetic data generation bypasses privacy concerns associated with real-world data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
