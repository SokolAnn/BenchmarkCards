# Historical Ink: 19th Century Latin American Spanish Newspaper Corpus with LLM OCR Correction

## 📊 Benchmark Details

**Name**: Historical Ink: 19th Century Latin American Spanish Newspaper Corpus with LLM OCR Correction

**Overview**: This paper presents a novel dataset of 19th-century Latin American newspaper texts addressing a critical gap in specialized corpora for historical and linguistic analysis in this region, and develops a framework utilizing a Large Language Model for OCR error correction and linguistic surface form detection.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish

**Resources**:
- [Resource](https://huggingface.co/datasets/Flaglab/latam-xix)
- [GitHub Repository](https://github.com/historicalink/LatamXIX)

## 🎯 Purpose and Intended Users

**Goal**: To address the gap in specialized corpora for 19th-century Latin American newspapers and provide tools for OCR error correction in historical texts.

**Target Audience**:
- ML Researchers
- Historians
- Digital Humanists

**Tasks**:
- Text Correction
- Linguistic Analysis

**Limitations**: Manual evaluation for assessing OCR accuracy introduces subjectivity.

## 💾 Data

**Source**: Compiled from Colombian digital newspaper archives and physical collections including 197 newspaper titles across various Latin American countries.

**Size**: 128MB

**Format**: N/A

**Annotation**: Errors detected and classified through a semi-automated framework utilizing a Large Language Model.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Character Error Rate (CER)
- MAP

**Calculation**: Character error rate (CER) is calculated based on OCR output compared to the ground truth.

**Interpretation**: Lower CER values indicate better accuracy of OCR corrections.

**Validation**: Framework validated through expert evaluation of correction outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Societal Impact

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Societal Impact**: Impact on education: plagiarism

**Demographic Analysis**: The dataset includes diverse contributions from various Latin American countries.

**Potential Harm**: Potential bias introduced by OCR errors and hallucinations from the LLM affecting historical accuracy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
