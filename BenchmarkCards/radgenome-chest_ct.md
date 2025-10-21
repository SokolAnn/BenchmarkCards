# RadGenome-Chest CT

## 📊 Benchmark Details

**Name**: RadGenome-Chest CT

**Overview**: RadGenome-Chest CT is a comprehensive, large-scale, region-guided 3D chest CT interpretation dataset based on CT-RATE, designed to enhance the development of multimodal medical foundation models. It includes organ-level segmentation masks, multi-granularity grounded reports, and grounded visual question answering pairs.

**Data Type**: 3D chest CT volumes and reports

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/ibrahimhamamci/CT-RATE)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to advance the development of agent-based multimodal medical foundation models that can generate texts based on corresponding visual regions.

**Target Audience**:
- ML Researchers
- Medical Professionals

**Tasks**:
- Visual Question Answering
- Segmentation

**Limitations**: N/A

## 💾 Data

**Source**: CT-RATE, which consists of 25,692 non-contrast 3D chest CT volumes and reports.

**Size**: 25,692 CT volumes and reports

**Format**: N/A

**Annotation**: Segmentation masks generated using the SAT model and reports annotated with region-specific structures.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are computed based on the accuracy of segmentation and report generation as outlined in the methodology.

**Interpretation**: Higher accuracy indicates better alignment between generated text and segmentation masks.

**Baseline Results**: N/A

**Validation**: All datasets have gone through manual verification to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
