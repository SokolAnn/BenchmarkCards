# MizanQA

## 📊 Benchmark Details

**Name**: MizanQA

**Overview**: MizanQA is a benchmark designed to evaluate LLMs on Moroccan legal question answering (QA) tasks, characterised by rich linguistic and legal complexity. It comprises over 1,700 multiple-choice questions that capture the nuances of authentic legal reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Similar Benchmarks**:
- Hijazi et al. (2024) Arabic legal benchmark

**Resources**:
- [Resource](https://huggingface.co/datasets/adlbh/MizanQA-v0)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of existing large language models (LLMs) in answering legal questions within the Moroccan legal framework.

**Target Audience**:
- ML Researchers
- Legal Professionals
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset does not comprehensively represent Moroccan law, especially in uncodified areas and recent legislative updates.

## 💾 Data

**Source**: Extracted from publicly available Moroccan law MCQ banks and exams.

**Size**: 1,776 questions

**Format**: N/A

**Annotation**: Manually verified by legal experts and annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the machine's ability to select correct options for questions with multiple correct answers.

**Interpretation**: Higher scores indicate better understanding and accuracy of legal concepts in the Moroccan context.

**Baseline Results**: Baseline model evaluations included various multilingual and Arabic-centric LLMs.

**Validation**: Manual verification by legal experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes demographic breakdowns provided by proficient annotators.

**Potential Harm**: The benchmark aims to minimize bias in legal AI applications.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All QA pairs were manually verified for accuracy and relevance, with attention to minimizing bias.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
