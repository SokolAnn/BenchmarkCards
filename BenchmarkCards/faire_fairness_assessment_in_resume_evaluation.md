# FAIRE (Fairness Assessment In Resume Evaluation)

## 📊 Benchmark Details

**Name**: FAIRE (Fairness Assessment In Resume Evaluation)

**Overview**: FAIRE is a benchmark designed to test for racial and gender bias in large language models (LLMs) used to evaluate resumes across different industries. It utilizes direct scoring and ranking methods to measure how model performance changes when resumes reflect different racial or gender identities.

**Data Type**: resume evaluation scores and rankings

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/athenawen/FAIRE-Fairness-Assessment-In-Resume-Evaluation.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate racial and gender bias in AI-driven resume evaluations.

**Target Audience**:
- ML Researchers
- HR Professionals
- AI Practitioners

**Tasks**:
- Bias Evaluation

**Limitations**: Our benchmark includes only 10 job categories, which reduces the diversity of professions compared to the original resume dataset.

## 💾 Data

**Source**: Publicly available resume datasets and New York Census data.

**Size**: 10 job categories with 10 job descriptions each

**Format**: Various formats of resumes

**Annotation**: Resumes were modified to reflect different racial and gender identities.

## 🔬 Methodology

**Methods**:
- Direct scoring
- Ranking

**Metrics**:
- Average score differences
- Maximum bias gaps
- Ranking inconsistencies

**Calculation**: Scores are calculated based on LLM evaluations across different demographic markers.

**Interpretation**: Bias is interpreted through comparative analysis of score distributions between demographic groups.

**Baseline Results**: Results show varying levels of bias across models, particularly in subjective evaluation dimensions.

**Validation**: The benchmark validation and performance were measured against multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes improved fairness checks across different racial and gender demographics.

**Potential Harm**: ['Bias in resume evaluations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
