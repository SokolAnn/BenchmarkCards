# ToolBH (Tool-augmented Large Language Models Hallucination Diagnostic Benchmark)

## 📊 Benchmark Details

**Name**: ToolBH (Tool-augmented Large Language Models Hallucination Diagnostic Benchmark)

**Overview**: ToolBH is a multi-level hallucination diagnostic benchmark designed to assess tool-augmented large language models' (LLMs) hallucination issues, focusing on both the depth and breadth of hallucination phenomena across various tool usage scenarios.

**Data Type**: user-query and toolset pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA
- AgentBench
- ToolBench

**Resources**:
- [GitHub Repository](https://github.com/ToolBeHonest/ToolBeHonest)

## 🎯 Purpose and Intended Users

**Goal**: To diagnose hallucination phenomena in tool-augmented LLMs and provide resources for exploring their real-world performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Hallucination Detection
- Tool Usage Evaluation
- Multi-level Diagnostic Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Manually annotated user queries and toolsets designed to challenge LLMs under tool-using scenarios.

**Size**: 700 evaluation samples

**Format**: N/A

**Annotation**: Multiple rounds of manual annotation conducted by the authors.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Progress Rate (PR)
- Matching Score (MS)

**Calculation**: Metrics are calculated based on the specific performance of models across three diagnostic levels focusing on solvability and tool utilization.

**Interpretation**: Higher scores indicate better performance in accurately identifying solvable tasks and correctly planning tool usage.

**Baseline Results**: State-of-the-art models achieved scores of 45.3 for Gemini-1.5-Pro and 37.0 for GPT-4o in the ToolBH benchmark.

**Validation**: Evaluation against multiple tool-augmented tasks across various model architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
