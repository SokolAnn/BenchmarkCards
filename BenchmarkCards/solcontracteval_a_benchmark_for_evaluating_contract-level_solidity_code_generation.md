# SolContractEval (A Benchmark for Evaluating Contract-Level Solidity Code Generation)

## 📊 Benchmark Details

**Name**: SolContractEval (A Benchmark for Evaluating Contract-Level Solidity Code Generation)

**Overview**: SolContractEval is the first contract-level benchmark for Solidity code generation, encompassing 124 tasks from real on-chain contracts across nine major domains, designed to better evaluate models' capabilities in real-world contract development.

**Data Type**: question-answering pairs

**Domains**:
- Finance
- Gaming
- Blockchain

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- ClassEval
- BenchSol

**Resources**:
- [GitHub Repository](https://github.com/ZJU-CTAG/SolContractEval)

## 🎯 Purpose and Intended Users

**Goal**: Provide a standardized method to evaluate Solidity code generation capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers
- Smart Contract Developers

**Tasks**:
- Contract-Level Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Verified smart contracts from Etherscan

**Size**: 124 tasks

**Format**: N/A

**Annotation**: Independent annotation and cross-validation by experienced developers

## 🔬 Methodology

**Methods**:
- Transaction replay
- Dynamic validation

**Metrics**:
- Compile@k
- Pass@k

**Calculation**: Compilation correctness is measured by the number of outputs that compile successfully, and functional correctness by the outputs that pass specified tests.

**Interpretation**: Higher Compile@k and Pass@k scores indicate better performance in generating functional Solidity code.

**Baseline Results**: N/A

**Validation**: The benchmark was validated using historical transaction data to assess the functional correctness of generated contracts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
