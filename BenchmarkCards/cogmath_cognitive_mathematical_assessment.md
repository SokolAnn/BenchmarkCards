# CogMath (Cognitive Mathematical Assessment)

## 📊 Benchmark Details

**Name**: CogMath (Cognitive Mathematical Assessment)

**Overview**: CogMath is a comprehensive evaluation framework that assesses large language models’ mathematical abilities through three cognitive stages and nine dimensions, inspired by human reasoning processes.

**Data Type**: mathematical problem-solving tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MATH
- E-GSM

**Resources**:
- [GitHub Repository](https://github.com/Ljyustc/CogMath)

## 🎯 Purpose and Intended Users

**Goal**: To assess the authentic mathematical capabilities of LLMs through a detailed cognitive framework.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Problem Solving

**Limitations**: N/A

## 💾 Data

**Source**: CogMath was applied to three benchmarks: GSM8K, MATH, and a newly created MExam dataset composed of real exam questions.

**Size**: 6,353 questions from MExam, 5,000 questions from MATH, 1,319 questions from GSM8K

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Pass Rate

**Calculation**: The pass rate for each LLM is calculated based on their performance in nine evaluation dimensions.

**Interpretation**: A higher pass rate indicates better mastery of mathematical problem-solving abilities.

**Baseline Results**: GPT-4 achieved 39.3% on MATH and 67.1% on GSM8K under CogMath assessment.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
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
