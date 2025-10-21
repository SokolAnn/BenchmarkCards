# CyberSOCEval

## 📊 Benchmark Details

**Name**: CyberSOCEval

**Overview**: CyberSOCEval is a suite of open-source benchmarks designed to evaluate Large Language Models (LLMs) in Malware Analysis and Threat Intelligence Reasoning, which are critical tasks for cybersecurity operational effectiveness.

**Data Type**: question-answering pairs

**Domains**:
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- CTIBench
- CyberMetric

**Resources**:
- [Resource](https://arxiv.org/abs/2509.20166)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLMs in cybersecurity tasks to improve model performance in supporting Security Operations Centers.

**Target Audience**:
- Cybersecurity Practitioners
- AI Researchers
- Cyber Defense Analysts

**Tasks**:
- Malware Analysis
- Threat Intelligence Reasoning

**Limitations**: The benchmarks are primarily multiple-choice formats, which may not perfectly simulate real-world tasks requiring open-ended responses.

## 💾 Data

**Source**: Data generated from real malware samples and threat intelligence reports validated by cybersecurity experts.

**Size**: 609 questions for Malware Analysis, 588 questions for Threat Intelligence Reasoning

**Format**: JSON

**Annotation**: Manually validated by cybersecurity experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of multiple-choice questions answered correctly by the model.

**Interpretation**: Higher accuracy indicates better performance in understanding and analyzing cybersecurity threats.

**Baseline Results**: Baseline accuracy for Malware Analysis is approximately 0.63% for random guessing, while for Threat Intelligence Reasoning is approximately 1.7%.

**Validation**: Results validated through manual review and comparison to baseline performances.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
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
