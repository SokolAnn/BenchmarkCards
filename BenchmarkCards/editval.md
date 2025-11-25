# EDITVAL

## 📊 Benchmark Details

**Name**: EDITVAL

**Overview**: EDITVAL is a standardized benchmark for quantitatively evaluating text-guided image editing methods, consisting of a curated dataset of images, editable attributes, and an automated evaluation pipeline using pre-trained vision-language models.

**Data Type**: images

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TedBench
- EditBench

**Resources**:
- [Resource](https://deep-ml-research.github.io/editval/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating text-guided image editing methods across various edit types.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Image Editing

**Limitations**: N/A

## 💾 Data

**Source**: Curated dataset from MS-COCO

**Size**: 92 images with 648 unique edit operations

**Format**: JSON

**Annotation**: Manual annotation and validation by human raters

## 🔬 Methodology

**Methods**:
- Automated evaluation using vision-language models
- Human evaluation study

**Metrics**:
- Correlation with human preferences
- Editing quality scores

**Calculation**: Automated metrics evaluate image fidelity using vision-language models and human evaluation assesses the quality of edits based on predefined criteria.

**Interpretation**: Higher scores indicate better fidelity of image edits to original properties and successful application of edits.

**Baseline Results**: Instruct-Pix2Pix, Null-Text, and SINE are top-performing methods.

**Validation**: Convergence between automated evaluations and human assessments confirmed through correlation studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Failures in spatial edits leading to inconsistent edited images.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
