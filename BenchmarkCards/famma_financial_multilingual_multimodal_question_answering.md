# FAMMA (Financial Multilingual Multimodal Question Answering)

## 📊 Benchmark Details

**Name**: FAMMA (Financial Multilingual Multimodal Question Answering)

**Overview**: FAMMA is an open-source benchmark for financial multilingual multimodal question answering (QA) that evaluates the abilities of large language models in answering complex reasoning questions requiring advanced financial knowledge. It consists of two versions: FAMMA-Basic with 1,945 questions extracted from university textbooks and exams, and FAMMA-LivePro with 103 novel questions created by domain experts.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English
- Chinese
- French

**Similar Benchmarks**:
- FiQA
- FinQA
- ConvFinQA
- FinanceBench
- FinBen

**Resources**:
- [Resource](https://famma-bench.github.io/famma/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of FAMMA is to advance robust financial QA systems and to provide a high-quality dataset for evaluating existing models.

**Target Audience**:
- Academic Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from university textbooks, exams, and authored by domain experts.

**Size**: 1,945 questions (FAMMA-Basic), 103 questions (FAMMA-LivePro)

**Format**: N/A

**Annotation**: Human-annotated answers and rationales.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated based on Pass@1 scores of model responses to benchmark questions.

**Interpretation**: Higher Pass@1 scores indicate better model performance on the benchmark.

**Baseline Results**: N/A

**Validation**: Competing LLMs are evaluated on both FAMMA-Basic and FAMMA-LivePro datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The data is released under a research-only license that prohibits commercial use.

**Consent Procedures**: Written consent was obtained from domain experts for contributions to FAMMA-LivePro.

**Compliance With Regulations**: Not Applicable
