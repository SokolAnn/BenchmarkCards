# Theory of Mind Benchmark Dataset

## 📊 Benchmark Details

**Name**: Theory of Mind Benchmark Dataset

**Overview**: We introduce a novel dataset of 68 tasks for probing Theory of Mind (ToM) in Large Language Models (LLMs), including potentially challenging variations which are assigned to 10 complexity classes, providing novel insights into the challenges LLMs face.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToMBench
- FANToM

**Resources**:
- [Resource](https://arxiv.org/abs/2410.06271)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the Theory of Mind capabilities of Large Language Models through a systematic and structured dataset.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Theory of Mind Evaluation

**Limitations**: The low goal accuracy across all tested models makes it hard to draw meaningful conclusions about the models' performance.

## 💾 Data

**Source**: Manually crafted unexpected content and unexpected transfer tasks based on complexity classes.

**Size**: 1088 scenes

**Format**: N/A

**Annotation**: Manually annotated 

## 🔬 Methodology

**Methods**:
- Machine evaluation

**Metrics**:
- Turn Accuracy
- Goal Accuracy

**Calculation**: Turn accuracy is calculated as the proportion of correct answers to total answers, while goal accuracy is calculated as the proportion of correctly answered scenes.

**Interpretation**: Models with higher turn accuracy do not necessarily have higher goal accuracy, indicating that the models may understand some linguistic patterns without sustaining robust Theory of Mind capabilities.

**Baseline Results**: N/A

**Validation**: Evaluated on four State-of-the-Art models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
