# JaPOC (Japanese Post-OCR Correction)

## 📊 Benchmark Details

**Name**: JaPOC (Japanese Post-OCR Correction)

**Overview**: We proposed JaPOC, a post-OCR correction benchmark based on Japanese vouchers, which contains real-world errors from two different OCR services, providing various characteristics to assist future research.

**Data Type**: image-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Japanese

**Resources**:
- [GitHub Repository](https://github.com/FastAccounting/ocr_correction_benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To create a benchmark for post-OCR correction methods for Japanese vouchers.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Correction

**Limitations**: N/A

## 💾 Data

**Source**: Real-world document images and annotations based on OCR results from various services.

**Size**: 11,000 voucher images

**Format**: N/A

**Annotation**: Annotated by a human specializing in text recognition.

## 🔬 Methodology

**Methods**:
- Language Model Evaluation
- Rule-based Evaluation

**Metrics**:
- Accuracy

**Calculation**: Measured based on word-level character matching between OCR results and ground truth.

**Interpretation**: Results are interpreted in terms of improvement in recognition accuracy due to post-OCR correction.

**Baseline Results**: Baseline models using T5 and a rule-based method were evaluated with accuracy metrics showing improvements.

**Validation**: Validation was performed using separate train, validation, and test datasets based on the image samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Removed personal information such as company representative names from the dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Used images with permission from invoice documents.

**Compliance With Regulations**: Not Applicable
