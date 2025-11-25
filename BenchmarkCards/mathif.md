# MathIF

## 📊 Benchmark Details

**Name**: MathIF

**Overview**: MathIF is a dedicated benchmark for evaluating instruction-following in mathematical reasoning tasks, focusing on the ability of large reasoning models to adhere to user directives.

**Data Type**: math problem prompts with constraints

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- IFEval
- FollowBench

**Resources**:
- [GitHub Repository](https://github.com/TingchenFu/MathIF)

## 🎯 Purpose and Intended Users

**Goal**: To systematically measure instruction-following performance in large reasoning models within math domains.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Math problems collected from public datasets, including GSM8K, MATH500, Minerva, Olympiad, AIME.

**Size**: 420 examples

**Format**: N/A

**Annotation**: Programmatically verified against Python constraints

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Hard accuracy (HAcc)
- Soft accuracy (SAcc)

**Calculation**: Hard accuracy reflects full compliance with constraints, while soft accuracy measures the proportion of satisfied constraints.

**Interpretation**: Higher accuracy indicates better instruction adherence.

**Baseline Results**: Models evaluated include Qwen3-14B, Qwen3-32B, DeepSeek-R1-Distill-Qwen series among others.

**Validation**: Empirical evaluations through direct model performance assessment on the MathIF benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
