# ToolHop

## 📊 Benchmark Details

**Name**: ToolHop

**Overview**: ToolHop is a dataset comprising 995 user queries and 3,912 associated tools, specifically designed for rigorous evaluation of multi-hop tool use in large language models.

**Data Type**: query-tool pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- API-Bank
- ToolAlpaca
- RestBench
- ToolBench
- MetaTool
- TaskBench
- T-Eval
- ToolEyes
- UltraTool
- Seal-Tools
- AnyToolBench
- BFCL v3

**Resources**:
- [Resource](https://huggingface.co/datasets/bytedance-research/ToolHop)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ToolHop is to evaluate large language models in their ability to use tools effectively in multi-hop scenarios.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Multi-Hop Reasoning

**Limitations**: The dataset primarily focuses on multi-hop tool use and may not extensively cover simple tool invocation tasks.

## 💾 Data

**Source**: Constructed using a query-driven data construction approach based on the MoreHopQA dataset.

**Size**: 995 queries and 3,912 tools

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Invocation Error

**Calculation**: Metrics are calculated based on the proportion of correct answers and invocation errors through comparison with predefined answers.

**Interpretation**: An accuracy score of 100% indicates perfect model performance, while higher invocation errors suggest greater difficulty in tool use.

**Validation**: The benchmark was validated through comprehensive evaluations of multiple model families.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
