# METATOOL

## 📊 Benchmark Details

**Name**: METATOOL

**Overview**: METATOOL is a benchmark designed to evaluate whether large language models (LLMs) possess tool usage awareness and can correctly choose tools. It includes a dataset called TOOLE, which contains diverse user queries requiring tool utilization, addressing both single-tool and multi-tool scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolQA
- ToolBench
- API Bank
- ToolLLM

**Resources**:
- [GitHub Repository](https://github.com/geekan/MetaGPT)
- [Resource](https://arxiv.org/abs/2310.03128)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs based on their tool usage awareness and tool selection capabilities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Tool Usage Awareness
- Tool Selection

**Limitations**: N/A

## 💾 Data

**Source**: User queries generated using various prompting methods and curated through manual validation.

**Size**: 21,127 queries

**Format**: JSON

**Annotation**: Human-validated and curated.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- Correct Selection Rate (CSR)

**Calculation**: Metrics calculated based on LLM responses to the benchmark tasks using defined ground truths.

**Interpretation**: Metrics are interpreted based on performance comparisons of LLMs against expected outcomes on the benchmark tasks.

**Baseline Results**: N/A

**Validation**: Performance of LLMs was validated through extensive testing across eight popular models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
