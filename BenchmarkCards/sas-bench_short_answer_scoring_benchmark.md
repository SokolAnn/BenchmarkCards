# SAS-Bench (Short Answer Scoring Benchmark)

## 📊 Benchmark Details

**Name**: SAS-Bench (Short Answer Scoring Benchmark)

**Overview**: SAS-Bench is a benchmark specifically designed for evaluating Short Answer Scoring (SAS) with Large Language Models (LLMs). It provides fine-grained, step-wise scoring and expert-annotated error categories, facilitating detailed evaluation of model reasoning processes and explainability.

**Data Type**: question-answering pairs

**Domains**:
- Education

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/PKU-DAIR/SAS-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs on Short Answer Scoring tasks using fine-grained and interpretable metrics.

**Target Audience**:
- ML Researchers
- Educators
- Assessment Developers

**Tasks**:
- Short Answer Scoring

**Limitations**: N/A

## 💾 Data

**Source**: GAOKAO-Benchmark based on China's National College Entrance Examination.

**Size**: 1,030 questions and 4,109 student responses

**Format**: CSV

**Annotation**: Annotated by domain experts with step-wise scores and error labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Collaborative Consistency Score (CCS)
- Errors Consistency Score (ECS)
- Quadratic Weighted Kappa (QWK)
- F1 Score

**Calculation**: CCS and ECS metrics measure model consistency with human annotations across overall and step-wise evaluations.

**Interpretation**: Higher CCS and ECS scores indicate better alignment with human evaluations.

**Baseline Results**: N/A

**Validation**: Evaluation of LLMs is conducted using an extensive set of experiments across sixteen widely used models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Explainability

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
