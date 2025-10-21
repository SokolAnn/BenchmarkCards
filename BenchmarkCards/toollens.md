# ToolLens

## 📊 Benchmark Details

**Name**: ToolLens

**Overview**: ToolLens is a new dataset crafted specifically for multi-tool scenarios, containing queries that require the collaborative use of multiple tools to simulate real-world retrieval conditions.

**Data Type**: query-tool pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolBench

**Resources**:
- [GitHub Repository](https://github.com/quchangle1/COLT)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive resource for improving tool retrieval performance in the context of large language models (LLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Tool Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing tool data and refined using human verification and GPT-4 generative prompts.

**Size**: 18,770 queries

**Format**: N/A

**Annotation**: Human verified and generated using GPT-4

## 🔬 Methodology

**Methods**:
- Fine-tuning PLM-based retrieval models
- Collaborative learning with bipartite graphs

**Metrics**:
- COMP@K
- Recall@K
- NDCG@K

**Calculation**: Performance is calculated using a novel metric COMP@K, which measures the completeness of retrieved tools.

**Interpretation**: Higher COMP@K values indicate better completeness in the tool retrieval results.

**Baseline Results**: N/A

**Validation**: Extensive experiments including comparisons to established benchmarks and metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
