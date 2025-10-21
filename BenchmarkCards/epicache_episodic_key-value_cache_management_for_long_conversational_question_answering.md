# EPICACHE (Episodic Key-Value Cache Management for Long Conversational Question Answering)

## 📊 Benchmark Details

**Name**: EPICACHE (Episodic Key-Value Cache Management for Long Conversational Question Answering)

**Overview**: EPICACHE is a training-free Key-Value (KV) cache management framework designed for long conversational question answering under fixed memory budgets. It employs block-wise prefill and episodic KV compression to manage memory efficiently while preserving response accuracy.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Realtalk
- LoCoMo
- LongMemEval

**Resources**:
- [GitHub Repository](https://github.com/xiaowu0162/LongMemEval)

## 🎯 Purpose and Intended Users

**Goal**: To enable efficient long conversational question answering under strict memory constraints while improving accuracy through effective cache management.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: LongConvQA benchmarks including Realtalk, LoCoMo, and LongMemEval.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the model's performance on various QA tasks across different cache sizes.

**Interpretation**: Higher accuracy indicates better performance in answering questions accurately based on long contextual information.

**Baseline Results**: EPICACHE outperforms existing methods by 20% in accuracy under compressed memory budgets.

**Validation**: Validated against multiple conversation history benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
