# StableToolBench

## 📊 Benchmark Details

**Name**: StableToolBench

**Overview**: StableToolBench is a newly proposed benchmark designed to enhance the stability of evaluations in tool learning for Large Language Models (LLMs) by incorporating a virtual API system and stable evaluation methods.

**Data Type**: API call scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolBench

**Resources**:
- [GitHub Repository](https://github.com/THUNLP-MT/StableToolBenchgeneral)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of StableToolBench is to provide a stable and scalable evaluation framework for assessing LLMs' capabilities in utilizing external tools.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Tool Utilization

**Limitations**: The evaluation framework relies on GPT-4 as the automatic evaluator, which may increase costs.

## 💾 Data

**Source**: Generated from the virtual API system and simulated environments.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics based on GPT-4
- Human evaluation for performance assessment

**Metrics**:
- Solvable Pass Rate (SoPR)
- Solvable Win Rate (SoWR)

**Calculation**: Metrics are calculated based on the performance of LLMs against evaluated tasks categorized as solvable or unsolvable.

**Interpretation**: Higher SoPR and SoWR indicate better tool utilization capabilities of LLMs.

**Validation**: Evaluation procedures are conducted with multiple model runs and analyzed for consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
