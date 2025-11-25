# CyberSOCEval

## 📊 Benchmark Details

**Name**: CyberSOCEval

**Overview**: CyberSOCEval is a new suite of open source benchmarks designed to evaluate Large Language Models (LLMs) in two tasks: Malware Analysis and Threat Intelligence Reasoning, which are core defensive domains that are currently inadequately covered by existing security benchmarks.

**Data Type**: multiple-choice questions

**Domains**:
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- CTIBench
- CyberMetric

**Resources**:
- [GitHub Repository](https://github.com/CrowdStrike/cybersoceval_data)

## 🎯 Purpose and Intended Users

**Goal**: To provide a clear evaluation platform for LLMs in SOC activities focusing on malware analysis and threat intelligence reasoning, guiding model improvement efforts.

**Target Audience**:
- AI model developers
- Cybersecurity practitioners

**Tasks**:
- Malware Analysis
- Threat Intelligence Reasoning

**Limitations**: The use of multiple choice format may not perfectly emulate real-world task performance.

## 💾 Data

**Source**: Public malware samples and threat intelligence reports.

**Size**: 1,197 question-answer pairs

**Format**: JSON

**Annotation**: Manual validation and editing by cybersecurity experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the share of questions for which the system selects all correct options and only the correct options.

**Interpretation**: Higher accuracy indicates better capability in malware analysis and threat intelligence reasoning tasks.

**Validation**: The benchmarks underwent manual review protocols and iterative refinements for quality assurance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
