# SolEval

## 📊 Benchmark Details

**Name**: SolEval

**Overview**: SolEval is the first repository-level benchmark for Solidity smart contract generation, consisting of 1,507 samples from 28 different repositories across 6 popular domains, designed to evaluate the performance of LLMs on Solidity.

**Data Type**: function samples

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- BenchSol

**Resources**:
- [GitHub Repository](https://github.com/pzy2000/SolEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of LLMs in generating secure and efficient Solidity smart contracts.

**Target Audience**:
- Researches in AI
- Developers working with blockchain and smart contracts

**Tasks**:
- Repository-level Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Samples collected from public GitHub repositories focused on Solidity smart contracts.

**Size**: 1,507 samples

**Format**: JSON

**Annotation**: Manually annotated by students with Solidity experience.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Pass@k
- Compile@k
- Gas@k
- Vul@k

**Calculation**: Metrics are calculated based on the number of functions that pass tests or meet gas efficiency requirements.

**Interpretation**: Higher Pass@k indicates better performance at generating functional Solidity code.

**Validation**: The benchmark was validated using unit tests from the repositories.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from publicly available repositories with no private information.

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
