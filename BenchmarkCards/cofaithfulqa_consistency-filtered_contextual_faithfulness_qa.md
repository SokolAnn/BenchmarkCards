# CoFaithfulQA (Consistency-filtered Contextual Faithfulness QA)

## 📊 Benchmark Details

**Name**: CoFaithfulQA (Consistency-filtered Contextual Faithfulness QA)

**Overview**: CoFaithfulQA is a benchmark specifically designed to evaluate faithfulness in scenarios where internal knowledge conflicts with accurate external evidence. It focuses on realistic scenarios rather than synthetic conflicts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ConFiQA

**Resources**:
- [GitHub Repository](https://github.com/OpenBMB/ParamMute)

## 🎯 Purpose and Intended Users

**Goal**: To enhance contextual faithfulness of large language models through suppression of unfaithfulness-associated feed-forward networks (FFNs) and promote reliance on external evidence.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from six widely-used open-domain QA datasets: Natural Questions, SQuAD, NewsQA, TriviaQA, SearchQA, and HotpotQA.

**Size**: 32,580 instances

**Format**: JSON

**Annotation**: Manual annotation based on model-generated responses with binary faithfulness labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Context Recall (ConR)
- Memory Recall (MemR)
- Memorization Ratio (MR)

**Calculation**: ConR measures model alignment with external context, while MemR indicates reliance on internal parametric knowledge; MR quantifies the tendency to favor memorized content.

**Interpretation**: Higher ConR with lower MemR indicates better contextual faithfulness and reduced reliance on internal memory.

**Baseline Results**: ParamMute consistently outperformed strong baselines on both CoFaithfulQA and the established ConFiQA benchmark.

**Validation**: Extensive experiments conducted on CoFaithfulQA and ConFiQA demonstrate the framework's effectiveness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias, Output bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: ['Generating factually incorrect responses', 'Undermining model trustworthiness']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Varies by source dataset; details provided in the appendix.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
