# Cross-lingual Named Entity Corpus for Slavic Languages

## 📊 Benchmark Details

**Name**: Cross-lingual Named Entity Corpus for Slavic Languages

**Overview**: This paper presents a corpus manually annotated with named entities for six Slavic languages, consisting of 5017 documents annotated with five classes of named entities. It aims to foster research in named entity recognition and linking across multiple Slavic languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bulgarian
- Czech
- Polish
- Slovenian
- Russian
- Ukrainian

**Resources**:
- [GitHub Repository](https://github.com/SlavicNLP/SlavicNER)
- [Resource](https://bsnlp.cs.helsinki.fi/SlavicNER)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality dataset for named entity recognition, linking, and lemmatization across Slavic languages.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Named Entity Linking
- Lemmatization

**Limitations**: N/A

## 💾 Data

**Source**: Manually annotated corpus derived from online news articles in six Slavic languages.

**Size**: 5017 documents, 152,888 named-entity mentions

**Format**: Annotated text files

**Annotation**: Manual annotation by native speakers with multiple consistency checks.

## 🔬 Methodology

**Methods**:
- Baseline evaluation using transformer-based models

**Metrics**:
- F1 Score

**Calculation**: The F1 Score is calculated over the various categories of named entities, using standard evaluation procedures.

**Interpretation**: Higher F1 Scores indicate better performance in correctly identifying and categorizing named entities.

**Baseline Results**: Micro-averaged F-score of 0.8503 (single topic out), 0.9222 (cross topics).

**Validation**: Cross-validation techniques were utilized to ensure the reliability of the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
