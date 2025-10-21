# TOOLRET (Tool Retrieval Benchmark)

## 📊 Benchmark Details

**Name**: TOOLRET (Tool Retrieval Benchmark)

**Overview**: TOOLRET is a comprehensive benchmark for tool retrieval tasks, designed to evaluate information retrieval models in selecting relevant tools from a large corpus of tools for large language models (LLMs). It includes 7.6k diverse retrieval tasks and a corpus of 43k tools.

**Data Type**: query-tool pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gtbTool-Retrieval-Benchmark)
- [Resource](https://huggingface.co/datasets/TOOLRET)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of TOOLRET is to systematically evaluate the performance of various information retrieval models on tool retrieval tasks to improve LLM capabilities in practical applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Tool Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: TOOLRET benchmark integrates tasks and tools collected from existing datasets, public research papers, and open-source platforms.

**Size**: 7,615 retrieval tasks, 43,215 tools

**Format**: JSON

**Annotation**: Manually annotated by experts and includes diverse task scenarios and tool descriptions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- NDCG@10
- Precision@10
- Recall@10
- Completeness@10

**Calculation**: Metrics are calculated based on the relevance of retrieved tools and their alignment with the input queries.

**Interpretation**: Higher NDCG, precision, and recall indicate better retrieval performance, reflecting the effectiveness of the information retrieval models.

**Baseline Results**: The best-performing model achieved NDCG@10 of 33.83, showcasing significant challenges in tool retrieval tasks.

**Validation**: Validated through performance comparison with existing IR models and human expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Poor retrieval may lead to ineffective tool-use LLM performances.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
