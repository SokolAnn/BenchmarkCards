# 3D-RAD (3D Radiology Med-VQA Dataset)

## 📊 Benchmark Details

**Name**: 3D-RAD (3D Radiology Med-VQA Dataset)

**Overview**: 3D-RAD is a large-scale dataset designed to advance 3D Medical Visual Question Answering (Med-VQA) using radiology CT scans, comprising six diverse VQA tasks which support both open- and closed-ended questions, along with complex reasoning challenges.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- VQA-RAD
- SLAKE
- PathVQA
- M3D-VQA

**Resources**:
- [GitHub Repository](https://github.com/Tang-xiaoxiao/M3D-RAD)
- [Resource](https://huggingface.co/datasets/Tang-xiaoxiao/3D-RAD)

## 🎯 Purpose and Intended Users

**Goal**: To advance 3D Med-VQA research by providing a benchmark that supports multi-temporal and multi-task evaluation in the context of real-world clinical reasoning.

**Target Audience**:
- ML Researchers
- Medical Researchers
- Healthcare Practitioners

**Tasks**:
- Anomaly Detection
- Image Observation
- Medical Computation
- Existence Detection
- Static Temporal Diagnosis
- Longitudinal Temporal Diagnosis

**Limitations**: N/A

## 💾 Data

**Source**: Curated from CT-RATE, a large-scale 3D chest CT dataset paired with radiology reports

**Size**: 136,195 training samples, 34,000 benchmark samples

**Format**: N/A

**Annotation**: Generated using a semi-automated pipeline with strong large language models (LLMs) and extensive human validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-L
- Accuracy

**Calculation**: Metrics are calculated based on model performance on defined tasks using standard evaluation procedures.

**Interpretation**: Higher scores indicate better model performance in answering the clinical questions accurately.

**Baseline Results**: N/A

**Validation**: Validation through LLM scoring and human evaluations to ensure high-quality QA pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Licensed under CC BY-NC-SA

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
