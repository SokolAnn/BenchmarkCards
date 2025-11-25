# Biasly (Expert-Annotated Dataset for Misogyny Detection and Mitigation)

## 📊 Benchmark Details

**Name**: Biasly (Expert-Annotated Dataset for Misogyny Detection and Mitigation)

**Overview**: Biasly is an expert-annotated dataset capturing subtle forms of misogyny in North American movie subtitles. It is designed for tasks including misogyny classification, severity score regression, and mitigation through text rewriting, fostering responsible AI development for social good.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EDOS
- APPDIA
- ParaDetox

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop a comprehensive dataset for detecting and mitigating subtle forms of misogyny in language while promoting responsible AI development.

**Target Audience**:
- ML Researchers
- Social Scientists
- NLP Practitioners
- Bias Detection Researchers

**Tasks**:
- Text Classification
- Severity Score Regression
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Expert annotations of contemporary movie subtitles from a corpus available through English-corpora.org.

**Size**: 10,000 datapoints

**Format**: N/A

**Annotation**: Expert annotations by diverse annotators from gender studies and linguistics fields.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy
- BLEU Score

**Calculation**: Metrics are calculated based on binary classifications and regression analysis of the annotations.

**Interpretation**: Good performance is indicated by high scores on F1 and accuracy metrics, while BLEU score reflects text generation quality.

**Baseline Results**: Models used include BERT, RoBERTa, and BART with baseline F1 scores reported in the paper.

**Validation**: Inter-annotator agreement measured, and methodologies followed for comprehensive evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse of the dataset for generating subtle misogynistic content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
