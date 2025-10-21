# SurgPub-Video

## 📊 Benchmark Details

**Name**: SurgPub-Video

**Overview**: SurgPub-Video is a comprehensive surgical video dataset composed of over 3,538 surgical videos and 25 million annotated frames across 11 specialties, designed to enhance vision-language model performance in surgical scene understanding and to support video-level Visual Question Answering benchmarks.

**Data Type**: video

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- Cholec80-VQA
- EndoVis-18-VQA
- SSG-VQA

**Resources**:
- [Resource](https://arxiv.org/abs/2508.10054)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, video-based surgical dataset for enhancing the capabilities of Vision-Language Models in understanding surgical procedures and support VQA.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Visual Question Answering
- Surgical Action Recognition
- Surgical Skill Assessment
- Procedure Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Peer-reviewed medical journals

**Size**: 3,538 videos, 25 million frames

**Format**: N/A

**Annotation**: Manually annotated with comprehensive VQA pairs and surgical concepts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Mean Average Precision (MAP)

**Calculation**: Metrics evaluated based on video-level comparisons and VQA pair matches

**Interpretation**: Higher accuracy indicates better performance of the model in understanding and answering surgical questions.

**Baseline Results**: SurgLLaV A-Video outperformed general-purpose models with 82.84% overall accuracy.

**Validation**: The evaluation metrics include overall accuracy and specialty-task specific accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
