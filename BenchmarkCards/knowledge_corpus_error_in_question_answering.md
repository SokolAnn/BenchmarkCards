# Knowledge Corpus Error in Question Answering

## 📊 Benchmark Details

**Name**: Knowledge Corpus Error in Question Answering

**Overview**: This study introduces the concept of knowledge corpus error in open-domain question answering, empirically demonstrating that generated contexts can be more helpful than retrieved contexts from a conventional knowledge corpus. The paper shows that paraphrasing human-annotated gold contexts using large language models can enhance performance across multiple question-answering benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NQ
- HotPotQA
- StrategyQA
- QASC

**Resources**:
- [GitHub Repository](https://github.com/xfactlab/emnlp2023-knowledge-corpus-error)

## 🎯 Purpose and Intended Users

**Goal**: To empirically observe the knowledge corpus error in question answering and demonstrate the effectiveness of generated contexts.

**Target Audience**:
- ML Researchers
- Domain Experts
- NLP Practitioners

**Tasks**:
- Question Answering

**Limitations**: The study did not employ a retrieval setting and primarily focused on the analytic understanding of how generation can provide advantages over retrieval.

## 💾 Data

**Source**: The data is derived from established question-answering benchmarks: NQ, HotPotQA, StrategyQA, and QASC, with specific context passages selected from these datasets.

**Size**: NQ: 2532 samples, HotPotQA: 7405 samples, StrategyQA: 2290 samples, QASC: 926 samples

**Format**: JSONL

**Annotation**: Human-annotated context passages were used for the experiments.

## 🔬 Methodology

**Methods**:
- Empirical testing using paraphrasing with LLMs
- Performance comparison using two different reader models: GPT and Claude

**Metrics**:
- Exact Match
- Accuracy

**Calculation**: Performance is calculated as the percentage of correctly answered questions among the total.

**Interpretation**: An increase in performance indicates the effectiveness of paraphrased contexts over original gold contexts.

**Baseline Results**: NQ: 40.9% exact match, HotPotQA: 36.3% exact match, StrategyQA: 54.6% accuracy.

**Validation**: Results were validated through empirical testing across multiple question-answering benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
