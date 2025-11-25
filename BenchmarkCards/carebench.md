# CAREBENCH

## 📊 Benchmark Details

**Name**: CAREBENCH

**Overview**: CAREBENCH is a fine-grained benchmark designed for video captioning and retrieval, comprising 1,000 videos with high-quality human-annotated detailed captions, including spatial and temporal annotations.

**Data Type**: video-caption pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MSR-VTT
- DREAM-1K
- ActivityNet
- DiDeMo

**Resources**:
- [Resource](https://carebench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate fine-grained video understanding capabilities of video-language models through detailed annotations and novel metrics.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Captioning
- Video Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Videos collected from FineAction dataset.

**Size**: 1,000 videos

**Format**: N/A

**Annotation**: Detailed hierarchical annotations covering overall summary, spatial descriptions, dynamic actions, and miscellaneous aspects.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Novel metric evaluation

**Metrics**:
- ReBias
- CapST

**Calculation**: Metrics are calculated based on spatial and temporal retrieval performance evaluations.

**Interpretation**: Higher scores indicate better performance in spatial and temporal video understanding.

**Validation**: The benchmark has been validated through comparisons with existing models and benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
