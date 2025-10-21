# BiblioPage

## 📊 Benchmark Details

**Name**: BiblioPage

**Overview**: BiblioPage is a dataset of scanned title pages annotated with structured bibliographic metadata, aimed at supporting automated extraction of bibliographic information and serving as a benchmark for document understanding, document question answering, and document information extraction.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Czech

**Similar Benchmarks**:
- FUNSD
- DocVQA

**Resources**:
- [GitHub Repository](https://github.com/DCGM/biblio-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To automate the extraction of bibliographic information from scanned title pages and provide a benchmark for evaluating various extraction methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Document Information Extraction
- Document Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Title pages sourced from 14 Czech libraries, comprising monographs primarily.

**Size**: 2,118 pages

**Format**: JSON

**Annotation**: Semi-automatic annotation using OCR and manual verification.

## 🔬 Methodology

**Methods**:
- Object Detection
- OCR
- Vision-Language Large Models

**Metrics**:
- mAP
- F1 Score

**Calculation**: Matched values are counted as true positives; unmatched proposed values as false positives; unmatched ground truth values as false negatives. Valid if Character Error Rate does not exceed 10%.

**Interpretation**: Higher scores indicate better performance in extracting bibliographic metadata.

**Baseline Results**: YOLOv11 medium achieved a mean F1 Score of 59; the best results from GPT-4o reached a mean F1 Score of 70 when supplemented with OCR.

**Validation**: Test set adequately covers all 16 attributes to ensure proper evaluation.

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
