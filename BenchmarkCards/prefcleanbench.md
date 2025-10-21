# PrefCleanBench

## 📊 Benchmark Details

**Name**: PrefCleanBench

**Overview**: PrefCleanBench offers a standardized protocol to assess cleaning strategies in terms of alignment performance and generalizability across diverse datasets, model architectures, and optimization algorithms, focusing on evaluating 13 preference data cleaning methods for LLM alignment.

**Data Type**: preference data pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RewardBench

**Resources**:
- [GitHub Repository](https://github.com/deeplearning-wisc/PrefCleanBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating various data cleaning methods and enhance LLM alignment through better data quality.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Preference Data Cleaning
- Alignment Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Four widely adopted preference datasets: Anthropic-HH, UltraFeedback, PKU-SafeRLHF, and HelpSteer2.

**Size**: 169,352 preference pairs

**Format**: N/A

**Annotation**: Human annotation and AI-generated labels.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Win-tie rate
- Average reward

**Calculation**: Metrics calculated by assessing the performance of models trained on cleaned vs. original datasets.

**Interpretation**: Higher win-tie rates and average rewards indicate better alignment.

**Baseline Results**: Models trained on uncleaned datasets serve as the baseline.

**Validation**: Results validated through controlled experiments across multiple datasets.

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
