# ToolBH

## 📊 Benchmark Details

**Name**: ToolBH

**Overview**: A comprehensive diagnostic benchmark for evaluating hallucination issues in tool-augmented large language models (LLMs). It assesses LLMs' hallucinations through depth and breadth perspectives.

**Data Type**: Evaluation samples

**Similar Benchmarks**:
- AgentBench
- ToolBench
- AgentBoard
- API-Bank
- ToolQA

**Resources**:
- [GitHub Repository](https://github.com/ToolBeHonest/ToolBeHonest)

## 🎯 Purpose and Intended Users

**Goal**: To diagnose hallucination issues in tool-augmented LLMs.

**Target Audience**:
- Researchers
- Developers
- Practitioners in AI

**Tasks**:
- Assess hallucination depth via solvability detection.
- Analyze solution planning and missing-tool analysis.

**Limitations**: None

## 💾 Data

**Source**: Synthetic annotations and manual reviews across multiple scenarios.

**Size**: 700 evaluation samples

**Format**: N/A

**Annotation**: Multiple rounds of manual annotation and synthesis.

## 🔬 Methodology

**Methods**:
- Multi-level diagnostic assessments (solvability detection, solution planning, missing-tool analysis).

**Metrics**:
- Exact Match (EM)
- Progress Rate (PR)
- Matching Score (MS)

**Calculation**: Scores reported as percentages.

**Interpretation**: Scores denote model performance across various tasks and scenarios.

**Baseline Results**: Currently advanced models Gemini-1.5-Pro (45.3) and GPT-4o (37.0).

**Validation**: Evaluation across 14 LLMs including 7 proprietary and 7 open-weight models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucinatory responses
- Tool recognition issues
- Misidentification of task solvability

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Prompt injection attack, Data poisoning

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Synthetic data does not utilize personally identifiable information.

**Data Licensing**: Data is released under MIT License.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
