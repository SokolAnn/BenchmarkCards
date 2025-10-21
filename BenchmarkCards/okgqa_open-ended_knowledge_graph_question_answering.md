# OKGQA (Open-ended Knowledge Graph Question Answering)

## 📊 Benchmark Details

**Name**: OKGQA (Open-ended Knowledge Graph Question Answering)

**Overview**: A new benchmark specifically designed to evaluate LLMs augmented with KGs in open-ended, real-world question answering settings, reflecting practical complexities through diverse question types.

**Data Type**: open-ended question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Y-Sui/OKGQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLMs enhanced with KGs under open-ended, real-world question answering scenarios and evaluate hallucination rates alongside overall response quality.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated DBPedia

**Size**: 2,050 questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- FActScore
- SAFE

**Calculation**: Metrics are calculated by decomposing long-form text into atomic facts and validating against external knowledge sources like Wikipedia.

**Interpretation**: High scores indicate higher factual accuracy and lower hallucinations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
