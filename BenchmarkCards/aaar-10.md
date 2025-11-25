# AAAR-1.0

## 📊 Benchmark Details

**Name**: AAAR-1.0

**Overview**: AAAR-1.0 is a benchmark dataset designed to evaluate LLM performance in four fundamental research tasks: Equation Inference, Experiment Design, Paper Weakness assessment, and Review Critique.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://renzelou.github.io/AAAR-1.0/)

## 🎯 Purpose and Intended Users

**Goal**: To comprehensively assess the LLMs’ capacity on expert-level research tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Equation Inference
- Experiment Design
- Paper Weakness
- Review Critique

**Limitations**: N/A

## 💾 Data

**Source**: Data crawled from peer-reviewed papers accepted by top-tier conferences and ICLR 2023 submissions.

**Size**: 993 instances, 1,049 positive equations, 3,147 negative equations, 100 instances for EXPDESIGN

**Format**: JSON

**Annotation**: Expert annotation by senior AI researchers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- S-Match
- ROUGE-L

**Calculation**: Metrics calculated based on model outputs compared against expert-annotated data.

**Interpretation**: Higher scores indicate better alignment with expert evaluations for each task.

**Validation**: Multi-round peer discussion among experts for data quality

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
