# NCSE v2.0 (Nineteenth-Century Serials Edition Version 2.0)

## 📊 Benchmark Details

**Name**: NCSE v2.0 (Nineteenth-Century Serials Edition Version 2.0)

**Overview**: The NCSE v2.0 dataset features improved article identification, high-quality OCR, and text classified into four types and seventeen topics, created from a collection of 19th-century English newspapers and periodicals using an image-to-text model.

**Data Type**: text

**Domains**:
- Natural Language Processing
- History

**Languages**:
- English

**Resources**:
- [Resource](https://doi.org/10.5522/04/28381610.v1)
- [GitHub Repository](https://github.com/JonnoB/reading_the_unreadable)

## 🎯 Purpose and Intended Users

**Goal**: To create a new, cleaned, classified, and searchable dataset of 19th-century newspapers for the benefit of historians and social scientists.

**Target Audience**:
- Historians
- Social Scientists
- Researchers

**Tasks**:
- Text Classification
- Optical Character Recognition

**Limitations**: N/A

## 💾 Data

**Source**: A collection of 84,000 pages of 19th-century English newspapers and periodicals.

**Size**: 60 GB (reduced to approximately 27GB after processing)

**Format**: PDF, PNG

**Annotation**: Manual annotation using bounding box techniques and classification algorithms.

## 🔬 Methodology

**Methods**:
- OCR Extraction
- Text Classification
- Statistical Analysis

**Metrics**:
- Character Error Rate (CER)
- F1 Score

**Calculation**: Character Error Rate (CER) is calculated as the sum of character substitutions, deletions, and insertions divided by the total number of characters.

**Interpretation**: A lower CER indicates better OCR accuracy. An F1 Score measures the balance between precision and recall in classification tasks.

**Baseline Results**: Pixtral achieved a median CER of 0.01, outperforming all other OCR methods.

**Validation**: Evaluation was performed on the NCSE test set and BLN600 for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC BY).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
