# AttackSeqBench

## 📊 Benchmark Details

**Name**: AttackSeqBench

**Overview**: AttackSeqBench is a benchmark designed to systematically evaluate Large Language Models' capability to understand and reason attack sequences in Cyber Threat Intelligence reports through three distinct Question Answering tasks.

**Data Type**: question-answering pairs

**Domains**:
- Cybersecurity

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Javiery3889/AttackSeqBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that advances LLM-driven Cyber Threat Intelligence report understanding and fosters its application in real-world cybersecurity operations.

**Target Audience**:
- Cybersecurity Researchers
- ML Researchers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from real-world Cyber Threat Intelligence reports.

**Size**: 1,697 questions for AttackSeq-Tactic, 1,917 questions for AttackSeq-Technique, 2,635 questions for AttackSeq-Procedure

**Format**: N/A

**Annotation**: Automated dataset construction with human evaluation and systematic evaluation metrics.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the number of correctly answered questions divided by the total number of questions.

**Interpretation**: Higher accuracy indicates better understanding and reasoning capabilities of the LLM.

**Baseline Results**: N/A

**Validation**: Extensive experiments conducted with both fast-thinking and slow-thinking LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: This study adheres to ethical research practices by focusing on publicly available CTI reports and ensuring that no proprietary or sensitive information is used.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
