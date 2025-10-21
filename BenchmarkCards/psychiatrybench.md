# PsychiatryBench

## 📊 Benchmark Details

**Name**: PsychiatryBench

**Overview**: PsychiatryBench is a multi-task benchmark for evaluating large language models in psychiatry, comprising eleven distinct question-answering tasks sourced from expert-validated psychiatric textbooks and casebooks.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MentalBench-10
- PsychBench

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive, clinically-grounded evaluation framework for large language models' performance in psychiatric applications.

**Target Audience**:
- ML Researchers
- Clinical Practitioners

**Tasks**:
- Diagnostic Reasoning
- Treatment Planning
- Management Plan
- Sequential Case Analysis
- Longitudinal Follow-up
- Multiple-Choice Questions
- Clinical Approach

**Limitations**: N/A

## 💾 Data

**Source**: Expert-curated psychiatric textbooks and casebooks, including DSM-5-TR Clinical Cases and Stahl’s Essential Psychopharmacology.

**Size**: over 5,300 expert-annotated items

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-judge assessment

**Metrics**:
- Accuracy
- F1 Score
- Similarities scores (0-100)

**Calculation**: Metrics calculated using similarity scoring and traditional classification metrics.

**Interpretation**: Scores reflect alignment with expert-validated responses, capturing both correctness and clinical relevance.

**Baseline Results**: N/A

**Validation**: Rigorous evaluation across leading LLMs against expert reference answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All materials were derived from publicly available, authoritatively authored psychiatric textbooks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
