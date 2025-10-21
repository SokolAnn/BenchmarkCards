# MedOdyssey (Medical Domain Benchmark for Long Context Evaluation)

## 📊 Benchmark Details

**Name**: MedOdyssey (Medical Domain Benchmark for Long Context Evaluation)

**Overview**: MedOdyssey is the first medical long-context benchmark consisting of two primary components: the medical-context 'needles in a haystack' task and a series of tasks specific to medical applications, comprising 10 datasets designed to evaluate long-context capabilities of large language models (LLMs) in the medical domain.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/JOHNNY-fans/MedOdyssey)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the study of large language models in long-context scenarios within the medical domain.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Needles in a Haystack
- Medical QA
- Counting
- Terminology Normalization
- Knowledge Graph Question Answering
- Table QA
- Case QA

**Limitations**: Evaluating limit lengths to ensure different models share the same contextual cues.

## 💾 Data

**Source**: Diverse medical corpora, including medical books, clinical guides, terminology databases, and electronic health records.

**Size**: 10 datasets with various lengths ranging from 4K to 200K tokens

**Format**: N/A

**Annotation**: Combination of manual and automated methods for fairness and minimizing data contamination.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on exact string matching (ESM) and subset string matching (SSM) methods.

**Interpretation**: A higher score indicates better performance in answering medical-based questions under long-context evaluation.

**Baseline Results**: Various LLMs including GPT-4, GPT-4o, Claude 3, and others with varying performance on the benchmark tasks.

**Validation**: Evaluated against both proprietary and open-source LLMs across different context lengths.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets are collected according to ethical guidelines and respect copyright laws.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
