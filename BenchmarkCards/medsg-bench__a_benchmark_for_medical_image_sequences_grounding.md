# MedSG-Bench: A Benchmark for Medical Image Sequences Grounding

## 📊 Benchmark Details

**Name**: MedSG-Bench: A Benchmark for Medical Image Sequences Grounding

**Overview**: MedSG-Bench is the first benchmark tailored for Medical Image Sequences Grounding, comprising eight VQA-style tasks and totaling 9,630 question-answer pairs. It aims to evaluate the grounding capabilities of multimodal large language models (MLLMs) in sequential medical imaging scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/MedSG-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of MedSG-Bench is to evaluate the fine-grained visual grounding capabilities of MLLMs in medical image sequences.

**Target Audience**:
- ML Researchers
- Medical Professionals
- Data Scientists

**Tasks**:
- Image Difference Grounding
- Image Consistency Grounding
- Multi-View Grounding
- Object Tracking
- Visual Concept Grounding
- Visual Patch Grounding
- Cross-modal Grounding
- Referring Grounding

**Limitations**: N/A

## 💾 Data

**Source**: 76 publicly available medical imaging datasets under permissive licenses.

**Size**: 9,630 question-answer pairs

**Format**: N/A

**Annotation**: Manual annotations provided within the datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Intersection over Union (IoU)
- Accuracy at IoU threshold 0.5 (Acc@0.5)

**Calculation**: IoU is calculated as the area of overlap between the predicted and ground-truth bounding boxes divided by the area of their union.

**Interpretation**: Higher IoU and Acc@0.5 scores indicate better model performance in localizing and grounding the medical image sequences.

**Validation**: The benchmark was validated through evaluations of both general-purpose and medical-domain specialized MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data includes 76 datasets with permissive licenses (e.g., CC BY 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
