# LIBRA (Long Input Benchmark for Russian Analysis)

## 📊 Benchmark Details

**Name**: LIBRA (Long Input Benchmark for Russian Analysis)

**Overview**: LIBRA is a new benchmark for the evaluation of LLM long context understanding abilities in the Russian language, comprising 21 adapted datasets to study the LLM’s abilities to understand long texts thoroughly.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Russian

**Similar Benchmarks**:
- LongBench
- L-Eval

**Resources**:
- [GitHub Repository](https://github.com/ai-forever/LIBRA)
- [Resource](https://huggingface.co/spaces/ai-forever/LIBRA-Leaderboard)

## 🎯 Purpose and Intended Users

**Goal**: To create a reliable instrument for long context understanding evaluation, enabling the study of LLMs' abilities to solve tasks of different complexities.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Dialog Context Understanding

**Limitations**: The benchmark may not cover the full range of Russian language usage, potentially leading to biased performance metrics.

## 💾 Data

**Source**: Various adapted datasets and translations, including tasks from previous benchmarks.

**Size**: 21 datasets with variable sizes ranging from 4k to 128k tokens

**Format**: N/A

**Annotation**: Annotated by human annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Exact Match (EM)
- F1 Score

**Calculation**: Metrics calculated based on the correct answers against provided correct responses in each dataset.

**Interpretation**: The score indicates the accuracy of the models on the given tasks with respect to context length.

**Baseline Results**: Evaluated models include GPT-4o, GLM4-9B-Chat, among others, with varying performance across tasks.

**Validation**: The benchmark has been validated against multiple LLMs with long context capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark may demonstrate performance variations across different Russian dialects and contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data collection processes included measures for confidentiality and obtained necessary permissions.

**Data Licensing**: Datasets are published under the MIT license.

**Consent Procedures**: All users contributed with transparent permission.

**Compliance With Regulations**: Not Applicable
