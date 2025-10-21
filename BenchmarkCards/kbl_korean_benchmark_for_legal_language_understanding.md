# KBL (Korean Benchmark for Legal Language Understanding)

## 📊 Benchmark Details

**Name**: KBL (Korean Benchmark for Legal Language Understanding)

**Overview**: KBL is a benchmark for assessing the Korean legal language understanding of large language models. It consists of 7 legal knowledge tasks (510 examples), 4 legal reasoning tasks (288 examples), and the Korean bar exam (4 domains, 53 tasks, 2,510 examples).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Korean

**Similar Benchmarks**:
- KMMLU
- LegalBench
- LawBench

**Resources**:
- [GitHub Repository](https://github.com/lbox-kr/kbl)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of KBL is to evaluate the performance of large language models in understanding and processing Korean legal language across various tasks.

**Target Audience**:
- ML Researchers
- Legal Professionals
- AI Developers

**Tasks**:
- Knowledge Assessment
- Legal Reasoning
- Bar Exam Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: The datasets were compiled using various sources, including Korean precedents, statutes, and legal QA datasets.

**Size**: 3,308 examples

**Format**: N/A

**Annotation**: The datasets were developed in close collaboration with lawyers to ensure quality assurance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the correctness of model responses to the tasks.

**Interpretation**: High accuracy indicates better understanding and reasoning capabilities in legal contexts.

**Baseline Results**: N/A

**Validation**: The tasks were verified by licensed lawyers to ensure the quality and relevance of the questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personal information is redacted by the Korean government or court.

**Data Licensing**: Datasets will be released under a CC BY-NC license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
