# GRS-QA (Graph Reasoning-Structured Question Answering Dataset)

## 📊 Benchmark Details

**Name**: GRS-QA (Graph Reasoning-Structured Question Answering Dataset)

**Overview**: GRS-QA introduces a novel dataset that captures explicit reasoning structures for multi-hop question answering, enabling fine-grained evaluation of LLM capabilities across various reasoning structures by constructing reasoning graphs.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HotpotQA
- MuSiQue
- 2WikiMultiHopQA

**Resources**:
- [Resource](https://arxiv.org/abs/2411.00369)

## 🎯 Purpose and Intended Users

**Goal**: To enable a fine-grained evaluation of LLM multi-hop reasoning capabilities and to facilitate understanding of logical structures in question answering.

**Target Audience**:
- ML Researchers
- Model Developers
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: Imbalance in the distribution of reasoning graph types may bias models toward frequent types.

## 💾 Data

**Source**: Constructed from the training sets of existing multi-hop QA datasets: HotpotQA, MuSiQue, and 2WikiMultiHopQA.

**Size**: Various graphs across multiple reasoning types, specific numbers not stated

**Format**: N/A

**Annotation**: Graphs constructed by treating sentences as nodes with logical relations defining edges.

## 🔬 Methodology

**Methods**:
- Retrieval Performance Benchmark
- LLM QA Performance Benchmark

**Metrics**:
- Exact Match
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated by comparing retrieved and generated answers against ground truth.

**Interpretation**: Performance metrics are analyzed to understand model reasoning capabilities.

**Baseline Results**: Current LLM models: GPT-3.5, Llama3, and GPT-4o-mini.

**Validation**: Conducted on a shared GPU environment with strict control of question types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International License (CC BY 4.0).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
