# KITAB-Bench

## 📊 Benchmark Details

**Name**: KITAB-Bench

**Overview**: KITAB-Bench is a comprehensive Arabic OCR benchmark that spans 9 major domains and 36 sub-domains, providing diverse document types for evaluation such as handwritten text, structured tables, and charts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- KHATT
- IFN/ENIT
- DocBank
- MIDAD

**Resources**:
- [Resource](https://mbzuai-oryx.github.io/KITAB-Bench/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of KITAB-Bench is to provide a standardized evaluation framework for Arabic OCR systems to enhance their performance and benchmark capabilities.

**Target Audience**:
- ML Researchers
- OCR Developers
- Document Analysis Engineers

**Tasks**:
- Optical Character Recognition
- Table Recognition
- Chart Extraction
- Visual Question Answering
- Document Layout Detection

**Limitations**: N/A

## 💾 Data

**Source**: KITAB-Bench dataset consists of curated samples from existing Arabic document datasets, manually annotated PDFs, and synthetically generated content using an LLM-assisted pipeline.

**Size**: 8,809 samples

**Format**: N/A

**Annotation**: Manual annotation by native Arabic speakers

## 🔬 Methodology

**Methods**:
- Baseline comparisons of OCR systems
- Evaluation of document understanding tasks
- Human evaluation for annotation validation

**Metrics**:
- Character Error Rate (CER)
- Word Error Rate (WER)
- Mean Average Precision (mAP)
- Markdown Recognition Score (MARS)
- Chart Extraction Score (CharTeX)

**Calculation**: Metrics are calculated using standard evaluation formulas, such as Levenshtein distance for CER and WER, precision and recall for layout detection, and others.

**Interpretation**: Higher scores indicate better performance in OCR tasks and a more accurate extraction of information.

**Baseline Results**: N/A

**Validation**: Validated by native Arabic speakers through rigorous review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
