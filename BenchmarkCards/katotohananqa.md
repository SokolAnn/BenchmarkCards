# KatotohananQA

## 📊 Benchmark Details

**Name**: KatotohananQA

**Overview**: KatotohananQA is a Filipino adaptation of the TruthfulQA benchmark, aimed at evaluating an LLM’s truthfulness in Filipino, an under-resourced language, using a binary-choice format with 790 questions across 37 categories.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Filipino

**Similar Benchmarks**:
- TruthfulQA

**Resources**:
- [GitHub Repository](https://github.com/Renzios/KatotohananQA)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the truthfulness of Large Language Models when responding to questions in Filipino.

**Target Audience**:
- ML Researchers
- Language Model Developers

**Tasks**:
- Question Answering

**Limitations**: The limited breadth of dialects and languages, limited diversity of models evaluated, limitations imposed by a binary-choice setting, and lack of cultural diversity in the questions.

## 💾 Data

**Source**: Translation from the original English TruthfulQA dataset through machine translation and manual verification.

**Size**: 790 questions

**Format**: N/A

**Annotation**: Machine translated and verified by native Filipino speakers.

## 🔬 Methodology

**Methods**:
- Programmatic evaluation of model responses

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated by evaluating the model's response against the correct answer label.

**Interpretation**: Higher accuracy indicates better truthfulness in responses.

**Baseline Results**: Average accuracy in English was 94.72% and in Filipino was 83.87%, with a mean difference of +10.85%.

**Validation**: Statistical tests (McNemar’s test) were conducted to determine the significance of performance differences.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
