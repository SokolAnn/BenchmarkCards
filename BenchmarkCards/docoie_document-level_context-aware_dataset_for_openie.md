# DocOIE (Document-level Context-Aware Dataset for OpenIE)

## 📊 Benchmark Details

**Name**: DocOIE (Document-level Context-Aware Dataset for OpenIE)

**Overview**: DocOIE consists of 800 expert-annotated sentences from 80 documents, enabling OpenIE models to take relevant contexts for accurate tuple extraction.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OIE2016
- Wire57
- CaRB

**Resources**:
- [GitHub Repository](https://github.com/daviddongkc/DocOIE)

## 🎯 Purpose and Intended Users

**Goal**: To extract relational tuples with document-level contexts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Open Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Expert-annotated sentences from patent documents.

**Size**: 800 sentences

**Format**: N/A

**Annotation**: Expert annotation by two OpenIE experts.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision, Recall, and F1 Score are computed based on tuple extraction matches.

**Interpretation**: Higher values in Precision, Recall, and F1 Score indicate better performance in tuple extraction.

**Baseline Results**: DocIE model benchmarks against various traditional OpenIE models and demonstrates improved extraction accuracy.

**Validation**: Annotation consistency achieved 89.9% F1 score among expert annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
