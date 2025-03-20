# FAVABENCH

## 📊 Benchmark Details

**Name**: FAVABENCH

**Overview**: A comprehensive benchmark for fine-grained hallucination detection and editing in language models.

**Data Type**: Human judgments

**Domains**:
- General Knowledge
- Information-seeking

**Languages**:
- English

**Similar Benchmarks**:
- CommonSenseQA
- OpenBookQA

**Resources**:
- [Resource](https://fine-grained-hallucination.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the performance of models in detecting and editing hallucinations in language model outputs.

**Target Audience**:
- NLP Researchers
- Machine Learning Practitioners

**Tasks**:
- Fine-grained hallucination detection
- Error editing in language model outputs

**Limitations**: None

## 💾 Data

**Source**: FAVABENCH annotations from responses of ChatGPT, Llama2-Chat 7B, and Llama2-Chat 70B on knowledge-intensive queries.

**Size**: About 1,000 fine-grained human judgments.

**Format**: An annotated dataset identifying hallucinations and their types.

**Annotation**: Annotated by trained students with high inter-annotator agreement on identification of hallucinations.

## 🔬 Methodology

**Methods**:
- Automatic and human evaluations
- Fine-grained error detection
- Error editing

**Metrics**:
- F1 Score
- Precision
- Recall
- Factuality Score

**Calculation**: Evaluation of performance based on error detection and correction capabilities.

**Interpretation**: Systems are evaluated on their ability to identify and correct factual errors in model outputs.

**Validation**: Inter-annotator agreement calculated using Cohen's kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Potential Harm**: Potential dissemination of misinformation due to hallucinations in generated outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Responses were anonymized during annotation.

**Data Licensing**: Data is sourced from publicly available language model outputs.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
