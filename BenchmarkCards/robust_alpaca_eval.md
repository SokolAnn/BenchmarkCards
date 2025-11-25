# ROBUST ALPACA EVAL

## 📊 Benchmark Details

**Name**: ROBUST ALPACA EVAL

**Overview**: ROBUST ALPACA EVAL is a new benchmark that consists of semantically equivalent case-level queries, designed to evaluate the worst prompt performance of large language models (LLMs) in real-world scenarios. It emphasizes the importance of understanding model variability and robustness across diverse prompts by focusing on their worst-case performance.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TinyAlpacaEval
- AlpacaEval

**Resources**:
- [GitHub Repository](https://github.com/bwcao/RobustAlpacaEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the variability and robustness of large language models (LLMs) in response to diverse prompts, focusing particularly on the worst-case performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from TinyAlpacaEval, which itself is derived from existing prompts.

**Size**: N/A

**Format**: N/A

**Annotation**: Prompts were generated automatically and then manually reviewed to ensure semantic integrity and fluency.

## 🔬 Methodology

**Methods**:
- Evaluation on various LLMs

**Metrics**:
- Weighted win-rate

**Calculation**: Evaluators compare the outputs of the target model against a reference model to estimate winning probabilities.

**Interpretation**: The winning rate indicates the performance of models across prompts.

**Baseline Results**: Original performance serves as a benchmark for comparison but shows variable performance across tasks.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
