# STEERINGCONTROL

## 📊 Benchmark Details

**Name**: STEERINGCONTROL

**Overview**: STEERINGCONTROL is a benchmark for evaluating representation steering methods across alignment objectives such as bias, harmful generation, and hallucination. It assesses steering effectiveness and behavioral entanglement through a dataset of safety-relevant primary and secondary behaviors.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Harmbench
- TruthfulQA

**Resources**:
- [GitHub Repository](https://github.com/wang-research-lab/SteeringControl.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate representation steering methods and their effectiveness on various alignment objectives while studying their unintended side effects on other behaviors.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Bias Evaluation
- Harmful Generation Evaluation
- Hallucination Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: A collection of 17 datasets focusing on primary and secondary alignment behaviors.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Effectiveness
- Entanglement

**Calculation**: Effectiveness and entanglement are calculated based on performance measures for both primary and secondary behaviors.

**Interpretation**: Higher effectiveness scores indicate better steering performance, while lower entanglement indicates less unintended side effects.

**Baseline Results**: N/A

**Validation**: Conducted through a fixed train/validation/test split of each dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
