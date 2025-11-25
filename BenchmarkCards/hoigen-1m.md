# HOIGen-1M

## 📊 Benchmark Details

**Name**: HOIGen-1M

**Overview**: HOIGen-1M is the first large-scale dataset for human-object interaction (HOI) video generation, consisting of over one million high-quality videos collected from diverse sources with accurate captions.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://liuqi-creat.github.io/HOIGen.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality dataset for improving the accuracy of human-object interaction video generation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Generation

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was curated from 80 million raw videos sourced from various online platforms and refined through human verification.

**Size**: 1,000,000 videos

**Format**: video

**Annotation**: Videos are manually checked for human-object interactions to ensure quality and accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CoarseHOIScore
- FineHOIScore

**Calculation**: The CoarseHOIScore measures basic interaction accuracy by detecting HOI triplets in generated videos. The FineHOIScore assesses the details of interactions at the pixel level for more precise evaluation.

**Interpretation**: Higher scores indicate better generation of accurate human-object interactions in videos.

**Validation**: Extensive experiments were conducted comparing current T2V models applied to the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
