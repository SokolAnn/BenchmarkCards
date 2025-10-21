# Benchmarking Group Fairness in Reward Models

## 📊 Benchmark Details

**Name**: Benchmarking Group Fairness in Reward Models

**Overview**: This work benchmarks group fairness in reward models without requiring the same prompt questions across different demographic groups by using expert-written text from arXiv.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RewardBench

**Resources**:
- [Resource](https://arxiv.org/abs/2503.07806)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark group fairness in reward models to develop large language models (LLMs) that benefit all demographic groups fairly.

**Target Audience**:
- ML Researchers
- Ethicists
- Policy Makers

**Tasks**:
- Fairness Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: arXiv Metadata dataset containing expert-written papers across diverse fields.

**Size**: 16,000 query-response pairs

**Format**: JSON

**Annotation**: Expert human annotations

## 🔬 Methodology

**Methods**:
- ANOVA
- Statistical analysis

**Metrics**:
- Normalized Maximum Group Difference
- F-statistics

**Calculation**: Normalized by dividing maximum difference in average rewards by the mean of the reward scores across all social groups.

**Interpretation**: A smaller normalized maximum group difference indicates better group fairness.

**Baseline Results**: Top-performing models from the RewardBench leaderboard exhibited better group fairness.

**Validation**: Statistical significance tested through ANOVA

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark includes demographic breakdowns across eight social groups based on expertise.

**Potential Harm**: ['Systematic unfairness in model outputs across demographic groups']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons CC0 1.0 Universal (Public Domain Dedication)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
