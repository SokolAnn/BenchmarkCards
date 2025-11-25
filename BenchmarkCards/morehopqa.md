# MoreHopQA

## 📊 Benchmark Details

**Name**: MoreHopQA

**Overview**: MoreHopQA is a multi-hop dataset designed to evaluate reasoning capabilities of models through generative answers, avoiding shortcuts commonly taken by models in traditional extractive datasets. It includes enhanced questions requiring commonsense, arithmetic, and symbolic reasoning, thereby shifting the focus from basic extraction to complex reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- 2WikiMultihopQA
- MuSiQue

**Resources**:
- [GitHub Repository](https://github.com/Alab-NII/morehopqa)

## 🎯 Purpose and Intended Users

**Goal**: To create a more challenging dataset that emphasizes multi-hop reasoning capabilities in large language models, helps to benchmark reasoning skills, and prevents reliance on heuristics.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-hop Question Answering

**Limitations**: Some generated answers may not be thoroughly verified, potentially leading to incorrect answers.

## 💾 Data

**Source**: Derived from HotpotQA, 2WikiMultihopQA, and MuSiQue, enhanced through manual curation and semi-automated processes.

**Size**: 1,118 samples

**Format**: JSON

**Annotation**: Human verification performed on the dataset to ensure quality and answerability.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match
- F1 Score

**Calculation**: Metrics calculated based on the comparison of model-generated answers to ground-truth answers.

**Interpretation**: Higher Exact Match scores indicate better model performance in understanding and reasoning.

**Baseline Results**: Baseline performance handled using an artifact-based baseline with Llama-8B.

**Validation**: Multiple prompting strategies evaluated, such as zero-shot, few-shot, and Chain-of-Thought prompting validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset builds upon publicly available datasets, ensuring that no personal information was used.

**Data Licensing**: The dataset is intended to be published under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
