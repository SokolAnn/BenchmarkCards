# TESRBench (Temporal Event Sequence Retrieval Benchmark)

## 📊 Benchmark Details

**Name**: TESRBench (Temporal Event Sequence Retrieval Benchmark)

**Overview**: TESRBench is a comprehensive benchmark designed for evaluating temporal event sequence retrieval (TESR) from textual descriptions, comprising diverse real-world datasets with synthesized and reviewed textual descriptions.

**Data Type**: event sequences and textual descriptions

**Domains**:
- Natural Language Processing
- Social Networks
- Urban Dynamics
- E-Commerce
- Natural Disasters
- Transportation

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/tppllm)
- [GitHub Repository](https://github.com/zefang-liu/TPP-Embedding)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TESRBench is to provide a standardized platform for evaluating retrieval models on temporal event sequence retrieval tasks, highlighting the complexities of aligning event sequences with textual descriptions.

**Target Audience**:
- ML Researchers
- Academic Researchers
- Industry Practitioners

**Tasks**:
- Temporal Event Sequence Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Five real-world datasets: Stack Overflow, Chicago Crime, NYC Taxi Trip, U.S. Earthquake, Amazon Review

**Size**: 10,000 sequences (total across all datasets)

**Format**: Real-world datasets with synthesized textual descriptions

**Annotation**: Descriptions generated using GPT-4o-mini.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Reciprocal Rank (MRR)
- Recall@K

**Calculation**: Metrics calculated based on ranking position of the correct sequence and proportion in top K results for retrieval.

**Interpretation**: Higher MRR indicates better ranking of relevant event sequences for given descriptions; Recall@K shows the effectiveness of retrieval in locating correct sequences among top K results.

**Baseline Results**: Numerous embedding models were evaluated against TESRBench for comparative performance analysis in retrieval tasks.

**Validation**: Benchmark validated against baselines through multi-domain experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Robustness
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in prompt
- **Robustness**: Prompt injection attack
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for misuse in tracking personal activities']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sourced textual descriptions may reflect biases, and retrieval could be misused for tracking activities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
