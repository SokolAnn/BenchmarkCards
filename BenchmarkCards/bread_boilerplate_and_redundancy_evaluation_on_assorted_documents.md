# BREAD (Boilerplate and Redundancy Evaluation on Assorted Documents)

## 📊 Benchmark Details

**Name**: BREAD (Boilerplate and Redundancy Evaluation on Assorted Documents)

**Overview**: We create and release BREAD, a human-labeled benchmark on repetitive boilerplate vs. plausible linguistic content, spanning 360 languages. It tests and proposes a suite of metrics to identify redundancy in text.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- 360 languages

**Resources**:
- [GitHub Repository](https://github.com/toizzy/bread)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark and metrics for detecting redundancy in text, especially in low-resource languages.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Data Quality Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Expert-annotated dataset from the MADLAD-400 dataset.

**Size**: 2000 documents

**Format**: N/A

**Annotation**: Annotated by expert NLP practitioners.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- F1 Score

**Calculation**: Metrics are based on character n-gram frequency distributions and normalized for document length.

**Interpretation**: Scores indicate how much more redundant a document is compared to a natural document of the same length.

**Validation**: Grid search method for hyperparameter optimization.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Quality

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
