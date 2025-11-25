# SciAssess

## 📊 Benchmark Details

**Name**: SciAssess

**Overview**: SciAssess is a benchmark specifically designed for the comprehensive evaluation of Large Language Models (LLMs) in scientific literature analysis. It assesses capabilities in Memorization (L1), Comprehension (L2), and Analysis & Reasoning (L3) across a variety of scientific fields.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU-Pro
- MaScQA

**Resources**:
- [GitHub Repository](https://github.com/sci-assess/SciAssess)

## 🎯 Purpose and Intended Users

**Goal**: To thoroughly assess the efficacy of LLMs by evaluating their capabilities in scientific literature analysis.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification
- Named Entity Recognition
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually curated by domain experts and derived from existing datasets.

**Size**: 6,888 questions

**Format**: CSV

**Annotation**: Manual annotation by expert domain specialists.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- Recall

**Calculation**: Metrics are calculated based on the proportion of correct answers to total questions.

**Interpretation**: An accuracy of 70% or higher is considered acceptable.

**Baseline Results**: Performance metrics comparing 11 LLMs across multiple tasks.

**Validation**: Expert cross-validation ensures accuracy and reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures were implemented to avoid using sensitive information.

**Data Licensing**: Data constructed from scratch while ensuring copyright compliance.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
