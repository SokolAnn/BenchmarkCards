# NETPRESS

## 📊 Benchmark Details

**Name**: NETPRESS

**Overview**: NETPRESS is an automated benchmark generation framework for evaluating LLM agents in network applications, facilitating dynamic generation of diverse query sets and ground truths to improve reliability in high-stakes tasks like network operations.

**Data Type**: query-action pairs

**Domains**:
- Computer Networking

**Languages**:
- English

**Similar Benchmarks**:
- DyVal

**Resources**:
- [GitHub Repository](https://github.com/Froot-NetSys/NetPress)

## 🎯 Purpose and Intended Users

**Goal**: To enable effective evaluation of LLM-based agents in real-world network applications through dynamic queries that simulate complex operational scenarios.

**Target Audience**:
- ML Researchers
- Network Engineers
- System Administrators

**Tasks**:
- Network Configuration Troubleshooting
- Network Policy Deployment

**Limitations**: N/A

## 💾 Data

**Source**: Dynamic query generation and simulation environments with network emulators.

**Size**: millions of queries

**Format**: N/A

**Annotation**: Automatically generated through system execution and user-defined parameters.

## 🔬 Methodology

**Methods**:
- Dynamic query generation
- Network emulation
- Automated evaluation

**Metrics**:
- Correctness
- Safety
- Latency

**Calculation**: Metrics are calculated based on the evaluation of LLM-generated actions against ground truths and safety constraints through network emulation.

**Interpretation**: Successful resolution of network issues is indicated by the ability to restore connectivity without introducing new risks.

**Baseline Results**: N/A

**Validation**: Evaluations are conducted using network emulators that validate LLM outputs in a realistic simulated environment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Safety

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy
- **Fairness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
