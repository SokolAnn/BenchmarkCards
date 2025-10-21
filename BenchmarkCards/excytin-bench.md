# ExCyTIn-Bench

## 📊 Benchmark Details

**Name**: ExCyTIn-Bench

**Overview**: ExCyTIn-Bench is the first benchmark to evaluate an LLM agent on the task of Cyber Threat Investigation through security questions derived from investigation graphs. It aids in the development and evaluation of LLM agents in cybersecurity by leveraging logs from simulated multi-step attacks.

**Data Type**: question-answering pairs

**Domains**:
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- CTIBench
- SECURE

**Resources**:
- [GitHub Repository](https://github.com/SecRL/ExCyTIn-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To assist the development and evaluation of LLM agents for automatic threat investigation in cybersecurity.

**Target Audience**:
- ML Researchers
- Cybersecurity Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Data Analysis

**Limitations**: The benchmark is based on simulated scenarios and may not capture the full diversity of real-world attack techniques and log schemas.

## 💾 Data

**Source**: Data collected from a fictional Microsoft Azure tenant with data covering multiple simulated attack scenarios and logs from Microsoft Sentinel.

**Size**: 589 questions

**Format**: JSON

**Annotation**: Automatically generated using LLMs from bipartite incident graphs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Average Reward
- Success Rate

**Calculation**: Average reward is calculated based on the number of correct answers over the total number of questions.

**Interpretation**: A higher average reward indicates better performance of the LLM agents in threat investigation tasks.

**Baseline Results**: Baseline performance from various LLMs shown with average rewards ranging from 0.249 to 0.368.

**Validation**: Cross-validation with multiple LLM models to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark does not currently account for demographic factors in its evaluations.

**Potential Harm**: ['Potential misuse of the benchmark for developing harmful cybersecurity tools.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: PII has been anonymized in the dataset to protect user identity and sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
