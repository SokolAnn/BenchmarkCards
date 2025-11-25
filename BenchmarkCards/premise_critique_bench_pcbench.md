# Premise Critique Bench (PCBench)

## 📊 Benchmark Details

**Name**: Premise Critique Bench (PCBench)

**Overview**: PCBench is a comprehensive benchmark designed to evaluate the Premise Critique Ability of large language models (LLMs) by incorporating problems with four categories of logical inconsistencies across three levels of difficulty.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/MLGroupJLU/Premise_Critique)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the premise critique abilities of large language models (LLMs).

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Evaluators

**Tasks**:
- Question Answering

**Limitations**: The dataset is limited to English and Chinese, which may overlook language-specific logical structures and cultural nuances.

## 💾 Data

**Source**: Curated using mathematical reasoning problems with logical inconsistencies and misleading information.

**Size**: 3600 problems

**Format**: JSON

**Annotation**: Manual annotation and error injection strategies.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Proactive Premise Critique Rate
- Assisted Premise Critique Rate
- Proactive Premise Critique Cost Ratio
- Assisted Premise Critique Cost Ratio

**Calculation**: Metrics are calculated based on models' ability to identify and articulate errors in input premises in various scenarios and difficulty levels.

**Interpretation**: High scores in proactive metrics indicate strong autonomous premise critique ability, while large discrepancies between proactive and assisted rates suggest heavy reliance on external prompts.

**Validation**: Evaluated 15 representative LLMs against the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: The benchmark explicitly measures performance across different error types and task complexities, providing insights into demographic fairness across model responses.

**Potential Harm**: Identifying flawed premises and implications in reasoning tasks.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
