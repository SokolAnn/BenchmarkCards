# MML ONG BENCH -DOC

## 📊 Benchmark Details

**Name**: MML ONG BENCH -DOC

**Overview**: MML ONG BENCH -DOC is a long-context, multi-modal benchmark comprising 1,082 expert-annotated questions, constructed from 135 lengthy PDF-formatted documents to evaluate the Document Understanding (DU) capabilities of Large Vision-Language Models (LVLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- DocVQA
- ChartQA
- FinanceBench

**Resources**:
- [Resource](https://mayubo2333.github.io/MMLongBench-Doc)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the long-context document understanding abilities of Large Vision-Language Models (LVLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 135 lengthy PDF-formatted documents spanning across 7 diverse domains, including documents sourced from existing datasets and newly collected documents.

**Size**: 1,082 questions

**Format**: PDF

**Annotation**: Expert annotation by ten expert-level annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Scores are calculated based on the comparison between generated answers and reference answers.

**Interpretation**: Generalized accuracy and F1 Score are reported to balance the answerable (positive) and unanswerable (negative) questions.

**Baseline Results**: N/A

**Validation**: Extensive evaluation across 14 LVLMs was conducted.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
