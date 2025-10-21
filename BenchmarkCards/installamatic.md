# INSTALLAMATIC

## 📊 Benchmark Details

**Name**: INSTALLAMATIC

**Overview**: A dataset of 40 open source Python repositories designed to serve as a benchmark for evaluating the effectiveness of repository-level agents' understanding of repository contents and environment management tasks. Each repository is assigned a set of tags indicating its installation method and a ground truth working installation file.

**Data Type**: repository installation tasks

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- SWE-bench

**Resources**:
- [GitHub Repository](https://github.com/coinse/installamatic)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM-based agents for the task of automatically installing open source Python repositories.

**Target Audience**:
- ML Researchers
- Software Engineers
- Domain Experts

**Tasks**:
- Environment Management
- Software Installation

**Limitations**: N/A

## 💾 Data

**Source**: 40 open source Python repositories from GitHub

**Size**: 40 repositories

**Format**: JSON

**Annotation**: Manual inspection of repositories to identify install-relevant documentation and installation processes.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Empirical evaluation

**Metrics**:
- Success rate of installations
- Recall of install-relevant documents

**Calculation**: The successful installation rate is calculated as the number of successful installations over total attempts for each repository. Recall is defined as the proportion of relevant documents retrieved.

**Interpretation**: Higher metrics indicate better performance of the installation agent.

**Baseline Results**: The agent successfully installs 21 out of 40 repositories at least once, achieving a 28.8% average installation rate.

**Validation**: Empirical evaluation of INSTALLAMATIC's performance through multiple runs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
