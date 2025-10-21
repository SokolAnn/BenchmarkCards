# PV-VTT (Privacy Violation Video To Text)

## 📊 Benchmark Details

**Name**: PV-VTT (Privacy Violation Video To Text)

**Overview**: PV-VTT is a unique multimodal dataset aimed at identifying privacy violations, providing detailed annotations for both video and text in scenarios. It supports benchmarking tasks in both Video Anomaly Recognition (VAR) and video description.

**Data Type**: video feature vectors and text descriptions

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- XD-Violence
- UCF-Crime
- ShanghaiTech

**Resources**:
- [Resource](https://ryozomasukawa.github.io/PV-VTT.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To enable research across tasks such as Video Anomaly Recognition (VAR) and video description focusing on privacy violation detection.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Video Anomaly Recognition
- Video Description

**Limitations**: Some text descriptions derived from news manuscripts may contain context not always inferable from the videos.

## 💾 Data

**Source**: Videos collected from video sharing platforms such as YouTube, annotated for privacy violations.

**Size**: Approximately 2.3 million frames

**Format**: Frame-level annotated video feature vectors

**Annotation**: Frame-level annotation by human annotators and LLM-based anonymization for text descriptions.

## 🔬 Methodology

**Methods**:
- GNN-based video description model
- Hierarchical message passing for classification
- LLM prompting

**Metrics**:
- AUC-ROC
- BLEU Score
- ROUGE-L
- METEOR
- BERTScore

**Calculation**: Measures are calculated based on classification accuracy in frame-level annotation and text description generation.

**Interpretation**: Higher AUC indicates better performance in differentiating between normal and abnormal events.

**Baseline Results**: MissionGNN achieved a mean AUC (mAUC) of 94.61 on the PV-VTT dataset.

**Validation**: Evaluation against state-of-the-art models in video anomaly recognition and video description tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misclassification of privacy violations leading to false accusations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Only video feature vectors provided to ensure participant confidentiality; no raw video data released.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
