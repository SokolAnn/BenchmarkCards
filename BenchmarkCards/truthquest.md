# TruthQuest

## 📊 Benchmark Details

**Name**: TruthQuest

**Overview**: TruthQuest is a benchmark designed to evaluate the suppositional reasoning capabilities of large language models through knights and knaves puzzles while presenting problems of varying complexity.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/datasets/mainlp/TruthQuest)

## 🎯 Purpose and Intended Users

**Goal**: To provide an evaluation benchmark for the reasoning capabilities of large language models in the context of knights and knaves puzzles.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Logical Reasoning
- Deductive Reasoning

**Limitations**: The benchmark currently includes only knights and knaves puzzles with a single, unique solution.

## 💾 Data

**Source**: Generated instances of knights and knaves puzzles

**Size**: 2,400 unique instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the exactness of the model's predictions against the correct solutions.

**Interpretation**: A high accuracy rate indicates proficient reasoning capabilities.

**Baseline Results**: N/A

**Validation**: Evaluation and validation through manual inspection of a subset of model responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

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
