# HALLU SHIFT

## 📊 Benchmark Details

**Name**: HALLU SHIFT

**Overview**: HALLU SHIFT is a hallucination detection technique designed to analyze distribution shifts in the internal state space and token probabilities of Large Language Models (LLMs) to distinguish between hallucinated and truthful generations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- TriviaQA
- CoQA
- TydiQA

**Resources**:
- [GitHub Repository](https://github.com/sharanya-dasgupta001/hallushift)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust mechanism for detecting hallucinations in LLM-generated text by analyzing internal state shifts and token probabilities.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Five different question-answering datasets: CoQA, TruthfulQA, TriviaQA, TydiQA-GP(English), and HaluEval.

**Size**: 30,000 task-specific instances across multiple datasets with distributions of 10,000 examples each.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Distribution shift analysis
- Token probability features

**Metrics**:
- Accuracy
- F1 Score
- AUC-ROC

**Calculation**: Metrics are calculated based on the output of the hallucination score assigned using a membership assignment function.

**Interpretation**: Scores are interpreted as likelihoods of hallucination; lower scores indicate truthful responses while higher scores indicate hallucinations.

**Baseline Results**: Not applicable.

**Validation**: Validated across multiple datasets and compared against existing state-of-the-art methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
