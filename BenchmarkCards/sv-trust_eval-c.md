# SV-TRUST EVAL-C

## 📊 Benchmark Details

**Name**: SV-TRUST EVAL-C

**Overview**: SV-TRUST EVAL-C is a benchmark designed to evaluate LLMs’ abilities for vulnerability analysis of code written in the C programming language through structure reasoning and semantic reasoning, assessing how models identify relationships between code elements and their logical consistency under varying data and control flow complexities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- CVEFixes
- BigVul
- DiverseVul

**Resources**:
- [Resource](https://huggingface.co/datasets/LLMs4CodeSecurity/SV-TrustEval-C-1.0)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the SV-TRUST EVAL-C benchmark is to systematically evaluate the reasoning capabilities of large language models (LLMs) in analyzing vulnerabilities within source code.

**Target Audience**:
- Research Scientists
- Software Engineers
- Cybersecurity Professionals

**Tasks**:
- Vulnerability Analysis

**Limitations**: N/A

## 💾 Data

**Source**: The SV-TRUST EVAL-C dataset is developed based on the Structure-Oriented Variants Generator utilizing components from the Juliet Test Suite.

**Size**: 9,401 questions

**Format**: JSON

**Annotation**: Automatically generated based on structural and semantic properties of the code.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Zero-shot inference
- In-context learning

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the correct identification of vulnerabilities through structured reasoning and semantic understanding in question-answering tasks.

**Interpretation**: Higher accuracy indicates better reasoning capabilities of the models in vulnerability analysis.

**Baseline Results**: The results show significant variance across11 evaluated LLMs, with top-performing models scoring below 50% in semantic reasoning tasks.

**Validation**: The benchmark is validated through extensive testing against known vulnerabilities from the Juliet Test Suite.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
