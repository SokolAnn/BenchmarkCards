# CBVS (Chinese Video Search Benchmark)

## 📊 Benchmark Details

**Name**: CBVS (Chinese Video Search Benchmark)

**Overview**: CBVS is a large-scale benchmark designed for Chinese short video search scenarios, providing a manual fine-labeling dataset and two large-scale datasets to support cover-based video retrieval tasks.

**Data Type**: video cover-image pairs and user query-video cover pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- V ATEX
- Wukong
- Product1M

**Resources**:
- [GitHub Repository](https://github.com/QQBrowserVideoSearch/CBVS-UniCLIP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating vision-language models in the context of Chinese short video search.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image-Text Matching
- Video Search

**Limitations**: N/A

## 💾 Data

**Source**: User query logs from the QQ Browser and videos from Chinese video platforms such as BiliBili and Tencent Video.

**Size**: 20,001 image-text pairs for CBVS-20K; 5M and 10M video cover-title pairs for CBVS-5M/10M.

**Format**: N/A

**Annotation**: Manually annotated by trained human experts with cross-validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Recall
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain (NDCG)

**Calculation**: Based on similarity scores of matched image and text embeddings using ITC loss.

**Interpretation**: Higher recall and MAP indicate better performance of the model in retrieving relevant video images for user queries.

**Baseline Results**: UniCLIP achieves state-of-the-art performance compared to other models evaluated on CBVS-20K.

**Validation**: Cross-validation for relevance scoring of user queries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
