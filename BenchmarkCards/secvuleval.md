# SECVULEVAL

## 📊 Benchmark Details

**Name**: SECVULEVAL

**Overview**: SECVULEVAL is a comprehensive benchmark designed for evaluating fine-grained vulnerability detection in C/C++ by focusing on real-world vulnerabilities at the statement level with rich contextual information.

**Data Type**: statement-level vulnerability annotations

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- BigVul
- CVEFixes
- DiverseVul
- MegaVul
- PrimeVul

**Resources**:
- [Resource](https://huggingface.co/datasets/arag0rn/SecVulEval)
- [GitHub Repository](https://github.com/basimbd/SecVulEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable benchmark for evaluating the capability of LLMs in detecting security vulnerabilities in C/C++ projects.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Vulnerability Detection
- Context Identification

**Limitations**: N/A

## 💾 Data

**Source**: C/C++ vulnerabilities from the National Vulnerability Database (NVD) and GitHub commits.

**Size**: 25,440 function samples covering 5,867 unique CVEs

**Format**: N/A

**Annotation**: Automatically extracted and contextual information added using LLMs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Multi-agent evaluation

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the comparison of the model outputs against the ground truth in the dataset.

**Interpretation**: Higher scores indicate better model performance in detecting vulnerabilities.

**Baseline Results**: Claude-3.7-Sonnet achieved a 23.83% F1-score.

**Validation**: The benchmark ensures rigorous validation through a multi-agent system.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse by malicious users for exploitation of vulnerabilities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
