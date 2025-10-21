# Turk-LettuceDetect

## 📊 Benchmark Details

**Name**: Turk-LettuceDetect

**Overview**: Turk-LettuceDetect is the first suite of hallucination detection models specifically designed for Turkish RAG applications, addressing the challenges posed by hallucinations in low-resource languages.

**Data Type**: token classification pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Turkish

**Similar Benchmarks**:
- RAGTruth

**Resources**:
- [GitHub Repository](https://github.com/NewmindAI/Turk-LettuceDetect)

## 🎯 Purpose and Intended Users

**Goal**: To provide effective hallucination detection models and dataset for Turkish RAG applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering
- Data-to-Text Generation
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Machine-translated version of the RAGTruth dataset

**Size**: 17,790 instances

**Format**: JSON

**Annotation**: Manually annotated by human experts

## 🔬 Methodology

**Methods**:
- Token-level classification using encoder architectures

**Metrics**:
- Precision
- Recall
- Macro F1-Score
- Area Under the Receiver Operating Characteristic Curve (AUROC)

**Calculation**: Calculated using cross-entropy loss across all tokens with special tokens masked.

**Interpretation**: Precision measures the correctness of predictions, Recall measures the identification rate of true occurrences, and the macro F1 Score balances both metrics.

**Validation**: Comprehensive evaluation across multiple tasks

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open-source license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
