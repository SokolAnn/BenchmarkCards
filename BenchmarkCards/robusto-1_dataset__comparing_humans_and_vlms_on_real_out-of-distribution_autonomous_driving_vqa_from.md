# Robusto-1 Dataset: Comparing Humans and VLMs on real out-of-distribution Autonomous Driving VQA from Peru

## 📊 Benchmark Details

**Name**: Robusto-1 Dataset: Comparing Humans and VLMs on real out-of-distribution Autonomous Driving VQA from Peru

**Overview**: The Robusto-1 dataset is designed to evaluate the cognitive alignment between humans and Vision-Language Models (VLMs) in autonomous driving scenarios through Visual Question Answering (VQA). It uses dashcam video data from Peru to explore how well these models generalize to out-of-distribution situations.

**Data Type**: video and question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/Robusto-1)

## 🎯 Purpose and Intended Users

**Goal**: To compare the cognitive alignment of humans and VLMs in driving contexts through a new dataset that features real-world traffic scenarios in Peru.

**Target Audience**:
- Researchers
- Industry practitioners

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Dashcam video data collected from two vehicles in Peru, annotated with questions for VQA.

**Size**: 200 five-second video segments sampled from 285 videos

**Format**: N/A

**Annotation**: Manual annotation and question formulation by the authors based on metadata derived from video content.

## 🔬 Methodology

**Methods**:
- Quantitative analysis of responses through Representational Similarity Analysis (RSA)
- Visual Question Answering tasks administered to both humans and VLMs.

**Metrics**:
- Cognitive alignment score based on similarity of responses

**Calculation**: Measured the similarity of responses between humans and VLMs using Pearson correlation.

**Interpretation**: Higher similarity scores indicate better cognitive alignment between humans and VLMs.

**Validation**: Performance compared to responses from both human participants and multiple VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: Analysis of participant demographics for understanding variability in responses across different backgrounds.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants provided digital consent, and data was anonymized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Digital consent was obtained from participant volunteers for their data usage.

**Compliance With Regulations**: Not Applicable
