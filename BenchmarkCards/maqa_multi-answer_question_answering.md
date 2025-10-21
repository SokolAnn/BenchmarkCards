# MAQA (Multi-Answer Question Answering)

## 📊 Benchmark Details

**Name**: MAQA (Multi-Answer Question Answering)

**Overview**: MAQA is a new dataset that introduces data uncertainty by constructing questions requiring multiple answers across world knowledge, mathematical reasoning, and commonsense reasoning tasks, aimed at evaluating uncertainty quantification methods.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Natural Questions
- AmbigQA

**Resources**:
- [GitHub Repository](https://github.com/YangYongJin/MAQA-Official-Repo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate uncertainty quantification methods in the context of data uncertainty by using a new dataset.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: Although we conducted quality checks, there may remain some ambiguous questions or unclear answers; also, the data primarily consists of short-form answers making the analysis of long-form answers challenging.

## 💾 Data

**Source**: Constructed dataset using both modified existing datasets and newly created questions with the help of LLMs (GPT-4-turbo).

**Size**: 2,042 question-answer pairs

**Format**: N/A

**Annotation**: Quality checked by human review and validated with multiple iterations of questions to ensure clarity and factual accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall
- Area Under ROC Curve (AUROC)
- Area Under the Precision-Recall Curve (AUPRC)

**Calculation**: Metrics are calculated based on the correctness of single answers, using precision, recall, and F1 score for multiple answers.

**Interpretation**: High AUROC and AUPRC scores indicate effective uncertainty quantification methods that can distinguish correct from incorrect predictions.

**Validation**: Validated through consensus among multiple authors for quality checks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The MAQA dataset is distributed under the Apache 2.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
