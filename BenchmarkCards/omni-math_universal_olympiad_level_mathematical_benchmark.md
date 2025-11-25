# Omni-MATH (Universal Olympiad Level Mathematical Benchmark)

## 📊 Benchmark Details

**Name**: Omni-MATH (Universal Olympiad Level Mathematical Benchmark)

**Overview**: Omni-MATH is a comprehensive benchmark designed to assess the mathematical reasoning capabilities of large language models (LLMs) at the Olympiad level, comprising a dataset of 4428 competition-level problems meticulously categorized into over 33 sub-domains and spanning more than 10 distinct difficulty levels.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- Olympiad Bench
- CHAMP

**Resources**:
- [GitHub Repository](https://github.com/user/repo)
- [Resource](https://huggingface.co/datasets/Omni-MATH)
- [Resource](https://huggingface.co/models/OmniJudge)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide a challenging evaluation framework for LLMs to measure their mathematical reasoning at a high level.

**Target Audience**:
- ML Researchers
- Model Developers
- Education Professionals

**Tasks**:
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: International Mathematical Competitions and curated problem sets

**Size**: 4428 examples

**Format**: JSON

**Annotation**: Manual annotation by experts and verification for solution consistency

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are computed based on the percentage of correct answers relative to the total number of problems.

**Interpretation**: Higher accuracy indicates better mathematical reasoning capabilities of the evaluated models.

**Baseline Results**: OpenAI o1-mini achieved 60.54% accuracy.

**Validation**: Cross-validation with expert annotation to ensure data quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
