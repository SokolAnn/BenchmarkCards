# CRYPTO FORMAL EVAL

## 📊 Benchmark Details

**Name**: CRYPTO FORMAL EVAL

**Overview**: A benchmark to assess the ability of Large Language Models (LLMs) to autonomously identify vulnerabilities in new cryptographic protocols through interaction with a theorem prover.

**Data Type**: cryptographic protocols

**Domains**:
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Cristian-Curaba/CryptoFormalEval)
- [Resource](https://arxiv.org/abs/2411.13627)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLM-based agents to identify vulnerabilities in cryptographic protocols using symbolic reasoning tools.

**Target Audience**:
- ML Researchers
- Cybersecurity Experts
- Model Developers

**Tasks**:
- Vulnerability Detection

**Limitations**: The full dataset will only be available upon request to verified research groups.

## 💾 Data

**Source**: Manually curated dataset of cryptographic protocols with associated vulnerabilities.

**Size**: 15 protocols

**Format**: N/A

**Annotation**: Manual validation and automatic evaluation system for identified vulnerabilities.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The benchmark evaluates the LLMs' performance through their ability to identify vulnerabilities and their interaction with the theorem prover.

**Interpretation**: Higher accuracy indicates better ability of LLMs to identify vulnerabilities.

**Baseline Results**: Preliminary results showing varied performance among current frontier LLMs.

**Validation**: Results validated through interaction with the Tamarin prover and empirical evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: The risk of incorrect vulnerability identification potentially leading to security gaps.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset is shared only upon verification of the requesting group.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
