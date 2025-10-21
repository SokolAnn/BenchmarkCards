# SurveillanceVQA-589K

## 📊 Benchmark Details

**Name**: SurveillanceVQA-589K

**Overview**: SurveillanceVQA-589K is the largest open-ended video question answering (VQA) benchmark tailored to the surveillance domain, comprising 589,380 QA pairs across 12 cognitively diverse question types, enabling comprehensive semantic understanding of both normal and abnormal video content.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/fei213/SurveillanceVQA-589K)

## 🎯 Purpose and Intended Users

**Goal**: To advance video-language understanding in safety-critical applications such as intelligent monitoring, incident analysis, and autonomous decision-making.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Four surveillance video datasets used for annotation: MSAD, MEVA, NWPU, and UCA.

**Size**: 589,380 QA pairs

**Format**: JSON

**Annotation**: Hybrid annotation combining human-written captions with Large Vision-Language Model (LVLM) assisted QA generation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Detail Orientation
- Contextual Understanding
- Temporal Understanding

**Calculation**: Average Score (Avg) calculated by normalizing individual scores across multiple dimensions.

**Interpretation**: Scores are on a 0-5 scale, with 5 indicating full accuracy and relevance.

**Baseline Results**: N/A

**Validation**: Evaluation was carried out on the test set of the SurveillanceVQA-589K dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
