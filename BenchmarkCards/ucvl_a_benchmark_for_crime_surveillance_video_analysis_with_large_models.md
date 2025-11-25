# UCVL (A Benchmark for Crime Surveillance Video Analysis with Large Models)

## 📊 Benchmark Details

**Name**: UCVL (A Benchmark for Crime Surveillance Video Analysis with Large Models)

**Overview**: UCVL is the first benchmark designed to evaluate the capabilities of Multimodal Large Language Models in video anomaly analysis, offering a diverse range of tasks and question types.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- UCF-Crime
- UCF-Crime Annotation

**Resources**:
- [Resource](https://arxiv.org/abs/2502.09325)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for Multimodal Large Language Models in the context of analyzing crime surveillance videos.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Anomaly Detection
- Classification
- Event Description
- Temporal Grounding
- Multiple-Choice Questioning

**Limitations**: N/A

## 💾 Data

**Source**: UCF-Crime and UCF-Crime Annotation datasets, reorganized annotations, and new QA pairs generated.

**Size**: 1,829 videos

**Format**: video

**Annotation**: Automatically generated QA pairs from human annotations using large language models.

## 🔬 Methodology

**Methods**:
- Evaluation of Multimodal Large Language Models with diverse question types
- Pattern matching for objective questions
- Human evaluation for open-ended responses using GPT-4o

**Metrics**:
- Accuracy
- Intersection over Union (IoU)

**Calculation**: Metrics are calculated based on the model's responses compared to ground truth annotations.

**Interpretation**: Scores are normalized to a scale of 0-100, reflecting the model's predictive capabilities and understanding of video anomalies.

**Baseline Results**: Results benchmarked against eight prevalent models with varying parameter sizes.

**Validation**: Evaluated across test sets to ensure reliability and performance consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
