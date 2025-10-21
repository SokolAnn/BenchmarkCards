# SyncBench

## 📊 Benchmark Details

**Name**: SyncBench

**Overview**: SyncBench is a benchmark featuring 24,332 instances of agent out-of-sync scenarios in real-world Collaborative Software Engineering (CSE) derived from 21 popular GitHub repositories with executable verification tests.

**Data Type**: agent out-of-sync scenarios

**Domains**:
- Software Engineering

**Languages**:
- Python

**Resources**:
- [Resource](https://xhguo7.github.io/SyncMind/)

## 🎯 Purpose and Intended Users

**Goal**: To assess agent out-of-sync recovery in collaborative software engineering and provide insights into existing LLM agents’ capabilities and limitations.

**Target Audience**:
- ML Researchers
- Software Engineers
- AI Developers

**Tasks**:
- Out-of-Sync Recovery Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from 21 GitHub repositories

**Size**: 24,332 instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Success Rate (SR)
- Localization Accuracy (LA)
- Assistance Seeking Rate (ASR)

**Calculation**: Metrics are calculated based on the success rates of agent out-of-sync recovery actions.

**Interpretation**: Higher success rates indicate better performance of agents in recovering from out-of-sync states.

**Validation**: The evaluation was performed using executable tests from the repository.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
