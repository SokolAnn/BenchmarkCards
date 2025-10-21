# Exploring Graph Tasks with Pure LLMs: A Comprehensive Benchmark and Investigation

## 📊 Benchmark Details

**Name**: Exploring Graph Tasks with Pure LLMs: A Comprehensive Benchmark and Investigation

**Overview**: This paper provides a comprehensive benchmarking framework for evaluating the performance of pure large language models (LLMs) on graph tasks, including node classification and link prediction, with a focus on instruction tuning and few-shot scenarios. It assesses the capabilities of LLMs in understanding graph structures and their robustness across various data conditions.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Graph Machine Learning

**Languages**:
- English

**Similar Benchmarks**:
- GLBench
- GraphICL

**Resources**:
- [GitHub Repository](https://github.com/myflashbarry/LLM-benchmarking)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark pure LLMs on graph tasks and explore their performance in few-shot learning and transferability settings.

**Target Audience**:
- ML Researchers
- Graph Learning Practitioners
- Model Developers

**Tasks**:
- Node Classification
- Link Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Datasets used include Cora, PubMed, OGBN-ArXiv, OGBN-Products.

**Size**: Cora: 2,708 nodes, 5,429 edges; PubMed: 19,717 nodes, 44,338 edges; OGBN-ArXiv: 169,343 nodes, 1,166,243 edges; OGBN-Products: 2,449,029 nodes, 61,859,140 edges.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Empirical performance evaluation over various models
- Hyperparameter tuning
- Few-shot instruction tuning
- Zero-shot evaluation
- Prompt design for graph tasks

**Metrics**:
- Accuracy

**Calculation**: Mean accuracy is calculated across different graph tasks and datasets to evaluate model performance.

**Interpretation**: Higher accuracy indicates better performance of LLMs on graph classification and link prediction tasks.

**Baseline Results**: Best performing models include instruction-tuned Llama8B and Qwen-plus for node classification and link prediction tasks.

**Validation**: Models were validated through standard training/validation/test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
