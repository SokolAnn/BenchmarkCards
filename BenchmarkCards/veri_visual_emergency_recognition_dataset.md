# VERI (Visual Emergency Recognition Dataset)

## 📊 Benchmark Details

**Name**: VERI (Visual Emergency Recognition Dataset)

**Overview**: VERI is a diagnostic benchmark designed to evaluate Vision-Language Models (VLMs) on their ability to distinguish between genuine emergency situations and visually similar but safe scenarios. It comprises 200 synthetic images and 50 real-world images, organized into three categories: Accidents & Unsafe Behaviors, Personal Medical Emergencies, and Natural Disasters.

**Data Type**: image pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Dasool/VERI-Emergency)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of VLMs in safety-critical scenarios and to assess their reliability in distinguishing genuine emergencies from visually similar yet safe situations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Risk Identification
- Emergency Response

**Limitations**: N/A

## 💾 Data

**Source**: VERI dataset includes synthetic images created via a multi-stage process and validated with real-world images.

**Size**: 250 images

**Format**: N/A

**Annotation**: Images were annotated through multiple rounds of human verification and descriptive captions were generated for each image pair.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision, recall, and F1 scores were computed based on human-annotated binary ground truth labels.

**Interpretation**: High precision indicates fewer false positives, while high recall indicates good detection of true emergencies. A balance between both metrics is ideal for assessing VLMs in emergency recognition.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through comparative evaluations with both synthetic and real-world pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
