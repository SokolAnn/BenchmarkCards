# CAMB (Civil Aviation Maintenance Benchmark)

## 📊 Benchmark Details

**Name**: CAMB (Civil Aviation Maintenance Benchmark)

**Overview**: This benchmark serves a standardized tool to measure LLM capabilities within civil aviation maintenance, identifying specific gaps in domain knowledge and complex reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Aerospace
- Engineering

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/CamBenchmark/cambenchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark specifically designed for civil aviation maintenance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering
- Multi-choice Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from civil aviation maintenance textbooks, bilingual aligned corpora, FIM and TSM manuals, typical fault cases, and related articles.

**Size**: 7 datasets and 11,000+ examples

**Format**: N/A

**Annotation**: Manual annotation and alignment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- F1 Score

**Calculation**: Metrics calculated based on model output against reference answers.

**Interpretation**: Higher scores indicate better model performance in correctly answering maintenance-related questions.

**Baseline Results**: Various models tested including Qwen3 family and others with specific accuracy metrics.

**Validation**: Evaluation performed through comparative analysis of model performances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
