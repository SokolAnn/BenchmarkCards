# GRAPE (Grouped Ranking-Aware Policy Optimization Enhancement)

## 📊 Benchmark Details

**Name**: GRAPE (Grouped Ranking-Aware Policy Optimization Enhancement)

**Overview**: GRAPE is a plug-and-play enhancement approach that incorporates ranking signals into retrieval-guided query rewriting with LLMs to improve retrieval performance under distributional shifts including multilingual, length, and modality differences.

**Data Type**: text

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- Flickr30k-CN
- CVLUE
- XM3600
- Wikipedia
- CIRR

**Resources**:
- [GitHub Repository](https://github.com/Chinese0123456/GRAPE.git)

## 🎯 Purpose and Intended Users

**Goal**: To enhance CLIP-based retrieval systems under distributional shifts without costly re-embedding or redeployment.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Five representative benchmarks including Flickr30k-CN, CVLUE, XM3600, Wikipedia, and CIRR.

**Size**: 148,915 training queries, 29,783 training images for Flickr30k-CN; similar sizes for others.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Ranking-based reward optimization
- Retrieval-guided query rewriting with LLMs

**Metrics**:
- Recall@1
- Recall@10

**Calculation**: Ranking rewards are computed based on the relative ranking of the target image against generated queries.

**Interpretation**: Higher Recall@1 and Recall@10 indicate better retrieval performance.

**Baseline Results**: Improvements of 4.9% in Recall@10 over CLIP with LLM rewriting.

**Validation**: Conducted on training and validation splits of each benchmark dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
