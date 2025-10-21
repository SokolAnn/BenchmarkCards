# LongHealth

## 📊 Benchmark Details

**Name**: LongHealth

**Overview**: The LongHealth benchmark is a collection of 20 fictional patient cases with detailed clinical narratives designed to evaluate the performance of large language models (LLMs) in medical question answering through 400 multiple-choice questions focused on information extraction, negation, and sorting.

**Data Type**: clinical case texts with question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/kbressem/LongHealth)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more realistic assessment of LLMs in a healthcare setting, especially in extracting information from lengthy clinical documents.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The benchmark's use of multiple-choice questions does not fully reflect real-world clinical situations, which typically involve open-ended queries.

## 💾 Data

**Source**: 20 fictional patient cases created by experienced physicians.

**Size**: 20 cases, each ranging from 5,090 to 6,754 words

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Mean accuracy is calculated over five runs

**Interpretation**: Higher accuracy indicates better performance in extracting information from clinical documents.

**Baseline Results**: Mixtral-8x7B-Instruct-v0.1 achieved the highest accuracy at 77%.

**Validation**: Evaluated via multiple rounds of information retrieval tasks

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Safety

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Misuse**: Spreading disinformation

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
