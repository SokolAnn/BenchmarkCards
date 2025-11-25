# LLMs as verification oracles for Solidity

## 📊 Benchmark Details

**Name**: LLMs as verification oracles for Solidity

**Overview**: This paper provides the first systematic evaluation of GPT-5 in the role of verification oracles for Solidity smart contracts by benchmarking its performance on a large dataset of verification tasks, comparing its outputs against established formal verification tools, and assessing its effectiveness in real-world auditing scenarios.

**Data Type**: verification tasks

**Domains**:
- Natural Language Processing
- Computer Security

**Languages**:
- English

**Similar Benchmarks**:
- VeriSolid

**Resources**:
- [Resource](https://anonymous.4open.science/r/LLMs-as-verification-oracles-for-Solidity-143B/)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the viability of using LLMs for smart contract verification.

**Target Audience**:
- Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Verification of smart contracts
- Audit assistance

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset containing 2034 verification tasks from different Solidity use cases.

**Size**: 2034 tasks

**Format**: N/A

**Annotation**: Manually crafted properties and mutations for verification.

## 🔬 Methodology

**Methods**:
- Evaluation against formal verification tools
- Quantitative metrics analysis
- Qualitative analysis of explanations

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on predictions versus ground truth from verification tasks.

**Interpretation**: High scores indicate strong reasoning capabilities of the LLM, especially in GPT-5 over GPT-4.

**Baseline Results**: GPT-5 achieved over 85% accuracy across all prediction metrics and outperformed GPT-4 by a margin of 25%-30%.

**Validation**: Tested against established verification tools SolCMC and Certora.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
