# RTL-Breaker

## 📊 Benchmark Details

**Name**: RTL-Breaker

**Overview**: RTL-Breaker provides a novel framework to assess the security of large language models (LLMs) against backdoor attacks in the context of HDL code generation, by analyzing various trigger mechanisms and their effectiveness.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DfX-NYUAD/RTL-Breaker)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and analyze backdoor attacks on LLMs generating HDL code and foster research on countermeasures.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Code Generation
- Security Assessment

**Limitations**: N/A

## 💾 Data

**Source**: A dataset of HDL codes was sourced from various publicly available repositories and clean samples paired with poisoned samples were analyzed.

**Size**: 78M data items

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Case studies

**Metrics**:
- pass@k

**Calculation**: Measures the proportional success rates of the generated outputs based on specified prompts.

**Interpretation**: Higher scores on pass@k indicate better performance of the generated HDL code.

**Baseline Results**: N/A

**Validation**: The framework was validated through multiple case studies focusing on different backdoor attack mechanisms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Security
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Code generation vulnerabilities due to backdoor attacks']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
