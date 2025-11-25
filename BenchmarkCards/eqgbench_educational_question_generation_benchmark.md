# EQGBench (Educational Question Generation Benchmark)

## 📊 Benchmark Details

**Name**: EQGBench (Educational Question Generation Benchmark)

**Overview**: EQGBench is a comprehensive benchmark specifically designed for evaluating LLMs’ performance in Chinese Educational Question Generation (EQG), consisting of 900 evaluation samples spanning three middle school disciplines: mathematics, physics, and chemistry.

**Data Type**: question-generation pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of EQGBench is to evaluate the ability of models to generate high-quality educational questions that align with pedagogical goals.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Question Generation

**Limitations**: N/A

## 💾 Data

**Source**: Structured user instructions generated through a three-step template process involving initial instruction design by teachers, parameterization, and dynamic information filling.

**Size**: 900 samples

**Format**: N/A

**Annotation**: Manual review by experienced teachers ensuring quality and applicability.

## 🔬 Methodology

**Methods**:
- Automated evaluation using LLM-based scoring
- Human evaluation for validation

**Metrics**:
- Knowledge Point Alignment
- Question Type Alignment
- Question Item Quality
- Solution Explanation Quality
- Competence-Oriented Guidance

**Calculation**: The scores for metrics are calculated on a scale of Excellent (2), Good (1), and Poor (0).

**Interpretation**: Scores indicate the degree to which generated questions meet educational effectiveness criteria.

**Baseline Results**: N/A

**Validation**: Validated through a systematic evaluation of 46 mainstream LLMs including both open-source and closed-source models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
