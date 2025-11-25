# THEATER (THinking Evaluation And Testing for Erroneous Reasoning)

## 📊 Benchmark Details

**Name**: THEATER (THinking Evaluation And Testing for Erroneous Reasoning)

**Overview**: THEATER is a comprehensive benchmark that systematically investigates Fake Reasoning Bias in language models by manipulating reasoning structures. It evaluates 17 advanced models across different types of reasoning manipulations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/fake-reasoning-bias-0B5A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the susceptibility of language models to Fake Reasoning Bias and provide insights into mitigating these vulnerabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Bias Evaluation
- Reasoning Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Evaluated on DPO datasets and factual datasets adapted from MMLU-Pro.

**Size**: Approximately 400 pairs across different datasets.

**Format**: N/A

**Annotation**: Human-annotated response pairs.

## 🔬 Methodology

**Methods**:
- Pairwise comparison
- Quantitative evaluation

**Metrics**:
- Accuracy
- Robustness Rate

**Calculation**: Accuracy is calculated based on the model’s judgment matching the ground-truth label. Robustness Rate measures the stability of the model's prediction against bias injections.

**Interpretation**: Higher accuracy and robustness rates indicate better performance in assessing reasoning without bias.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
