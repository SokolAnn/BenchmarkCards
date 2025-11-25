# LOGIC GAME

## 📊 Benchmark Details

**Name**: LOGIC GAME

**Overview**: LOGIC GAME is a novel benchmark designed to evaluate the comprehensive rule understanding, execution, and planning capabilities of LLMs, focusing on logical reasoning through diverse rule-based games.

**Data Type**: rule-based reasoning games

**Domains**:
- Artificial Intelligence

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- BIG-Bench
- CLUTRR
- GSM8K

**Resources**:
- [GitHub Repository](https://github.com/Hypatiaalegra/LogicGame-Data)
- [Resource](https://www.codabench.org/competitions/4140/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the rule-based reasoning capabilities of large language models through diverse tasks that assess understanding and execution of predefined rules.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Execution
- Planning

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated rule-based problems designed for assessing LLMs' logical reasoning capabilities.

**Size**: 304 task samples

**Format**: JSON

**Annotation**: Manually crafted by a team of expert annotators

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Human evaluation

**Metrics**:
- Answer Accuracy
- Process Accuracy
- Answer Process Accuracy

**Calculation**: Metrics are calculated based on binary correctness of answers and character-level similarity of processes.

**Interpretation**: Higher scores indicate better reasoning capabilities and adherence to logical rules.

**Validation**: Extensive evaluation across multiple models to identify reasoning deficiencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
