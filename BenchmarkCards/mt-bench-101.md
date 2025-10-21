# MT-Bench-101

## 📊 Benchmark Details

**Name**: MT-Bench-101

**Overview**: MT-Bench-101 is designed to evaluate the fine-grained abilities of large language models in multi-turn dialogues, using a three-tier hierarchical ability taxonomy comprising 4208 turns across 1388 multi-turn dialogues in 13 distinct tasks.

**Data Type**: dialogue turns

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- AlpacaEval
- MT-Bench
- MT-Bench++

**Resources**:
- [GitHub Repository](https://github.com/mtbench101/mt-bench-101)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the multi-turn dialogue capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering
- Instruction Clarification
- Self-Correction
- Content Rephrasing
- Format Rephrasing
- Mathematical Reasoning
- General Reasoning
- Proactive Interaction
- Anaphora Resolution
- Content Confusion
- Topic Shift
- Context Memory
- Adaptive Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dialogue data generated through prompts for evaluation tasks.

**Size**: 4208 turns

**Format**: N/A

**Annotation**: Rigorous curation by human annotators ensuring high-quality data.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Scores for multi-turn dialogues are taken based on the lowest score across all turns.

**Interpretation**: Higher scores indicate better performance in terms of multi-turn dialogue capabilities.

**Validation**: Performance validated through case studies and rigorous evaluations.

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

**Privacy And Anonymity**: Ensured participant privacy and data security during data collection.

**Data Licensing**: Not Applicable

**Consent Procedures**: Informed consent obtained from all participants.

**Compliance With Regulations**: Not Applicable
