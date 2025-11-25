# Multi-Modal Vision vs. Text-Based Parsing

## 📊 Benchmark Details

**Name**: Multi-Modal Vision vs. Text-Based Parsing

**Overview**: This benchmark evaluates eight multi-modal large language models on multiple invoice processing datasets, comparing direct image processing with structured parsing methods, providing insights for model selection and processing strategies.

**Data Type**: invoice image data

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Docbench

**Resources**:
- [Resource](https://anonymous.4open.science/r/invoice%20benchmark%20paper-4361/README.md)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate different LLM approaches for invoice processing using multiple datasets and processing strategies.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Document Understanding

**Limitations**: The benchmark's performance may be constrained by specific document formats and extraction challenges, especially with alphanumeric fields.

## 💾 Data

**Source**: Three diverse datasets: Clean Invoices (Donut), Scanned Receipts (ICDAR-2019-SROIE), and Scanned Invoices (inv-cdip)

**Size**: 1,850 images

**Format**: image files

**Annotation**: Structured JSON annotations and bounding boxes for text localization

## 🔬 Methodology

**Methods**:
- Evaluation against ground truth annotations
- Field-specific accuracy measurement

**Metrics**:
- Overall Accuracy
- Field-specific Accuracy

**Calculation**: Metrics calculated based on correctly extracted fields compared to total fields in the ground truth with minimal normalization for variations.

**Interpretation**: Accuracy provides insight into each model's performance across different document characteristics.

**Baseline Results**: N/A

**Validation**: Comparison of model output against established ground truth for fair evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
