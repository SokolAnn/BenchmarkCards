# G2A-VReID (Ground-to-Aerial Video Re-Identification)

## 📊 Benchmark Details

**Name**: G2A-VReID (Ground-to-Aerial Video Re-Identification)

**Overview**: The G2A-VReID dataset consists of 185,907 images and 5,576 tracklets capturing 2,788 distinct identities for the task of cross-platform video-based person re-identification.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- MARS
- iLIDS
- PRID-2011

**Resources**:
- [GitHub Repository](https://github.com/FHR-L/G2A-VReID)

## 🎯 Purpose and Intended Users

**Goal**: To construct a large-scale benchmark dataset for cross-platform video person ReID and propose methods for solving visual alignment problems.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Video-based Person Re-Identification

**Limitations**: N/A

## 💾 Data

**Source**: Captured using UAVs and ground surveillance cameras at different heights and modes.

**Size**: 185,907 images, 5,576 tracklets

**Format**: N/A

**Annotation**: Annotated with boundary boxes and unique IDs for each person.

## 🔬 Methodology

**Methods**:
- Evaluated using Cumulative Matching Characteristic (CMC) and mean Average Precision (mAP)

**Metrics**:
- mAP
- Rank-1

**Calculation**: Metrics calculated based on query and gallery video sequences.

**Interpretation**: Higher mAP and Rank-1 values indicate better performance in video person re-identification.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted on existing video ReID datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Privacy risks due to the visibility of individuals in captured videos.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Facial information is masked with mosaic to protect privacy.

**Data Licensing**: Licensed for non-profit academic research only.

**Consent Procedures**: Notification placed near data collection areas.

**Compliance With Regulations**: Not Applicable
