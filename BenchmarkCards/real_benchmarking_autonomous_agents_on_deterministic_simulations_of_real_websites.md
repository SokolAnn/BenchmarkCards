# REAL (Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites)

## 📊 Benchmark Details

**Name**: REAL (Benchmarking Autonomous Agents on Deterministic Simulations of Real Websites)

**Overview**: REAL is a benchmark and framework for multi-turn agent evaluations on deterministic simulations of real-world websites. It comprises high-fidelity, publicly hosted, deterministic replicas of 11 widely-used websites across various domains, designed for evaluating the capabilities and reliability of autonomous agents.

**Data Type**: evaluation tasks

**Domains**:
- Natural Language Processing
- Computer Vision
- E-commerce
- Travel
- Communication
- Professional Networking

**Languages**:
- English

**Resources**:
- [Resource](https://realevals.xyz)
- [GitHub Repository](https://github.com/agi-inc/agisdk)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to evaluate and improve the accuracy and reliability of autonomous web agents in performing complex tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Retrieval
- Action-oriented tasks
- Combined tasks

**Limitations**: N/A

## 💾 Data

**Source**: 11 high-fidelity, deterministic replicas of popular websites developed using React and Next.js.

**Size**: 112 evaluation tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Programmatic checks
- LLM-based judgments

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on task completion and correctness determined through programmatic state verification or rubric-based evaluations.

**Interpretation**: A higher accuracy rate indicates better performance in completing the tasks as specified.

**Baseline Results**: The current best model achieves a success rate of 41.07% in task performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
