# CORE-Bench (Computational Reproducibility Agent Benchmark)

## 📊 Benchmark Details

**Name**: CORE-Bench (Computational Reproducibility Agent Benchmark)

**Overview**: CORE-Bench consists of 270 tasks derived from 90 papers across computer science, social science, and medicine, designed to evaluate agents on their ability to reproduce the results of scientific studies using provided code and data.

**Data Type**: language-only and vision-language tasks

**Domains**:
- Natural Language Processing
- Computer Science
- Medicine
- Social Science

**Languages**:
- Python
- R

**Resources**:
- [GitHub Repository](https://github.com/siegelz/core-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of AI agents to reproduce scientific results, improving computational reproducibility in research.

**Target Audience**:
- AI Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Computational Reproducibility

**Limitations**: Limited accuracy of baseline agents demonstrated the need for further development.

## 💾 Data

**Source**: CodeOcean repositories with verified reproducibility.

**Size**: 270 tasks

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Agent-based evaluation

**Metrics**:
- Task accuracy

**Calculation**: Accuracy calculated as the proportion of tasks for which all task questions have been answered correctly.

**Interpretation**: Higher accuracy indicates better agent performance in reproducing scientific results.

**Baseline Results**: CORE-Agent achieved 60% accuracy on the easiest tasks.

**Validation**: Tasks validated through multiple evaluations of agents and manual reproduction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
