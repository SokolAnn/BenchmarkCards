# NEST FUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls

## 📊 Benchmark Details

**Name**: NEST FUL: A Benchmark for Evaluating LLMs on Nested Sequences of API Calls

**Overview**: NEST FUL is a benchmark designed to evaluate LLMs on nested sequences of API calls, emphasizing the complexity of passing outputs of one API call as inputs to subsequent calls.

**Data Type**: nested sequences of API calls

**Domains**:
- Natural Language Processing
- Coding

**Languages**:
- English

**Similar Benchmarks**:
- BFCL v1
- BFCL v2
- BFCL v3
- API-Blend
- NesTools

**Resources**:
- [GitHub Repository](https://github.com/IBM/NESTFUL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the performance of LLMs in complex nested API call sequences.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Function Calling
- API Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Built from MathQA and StarCoder2-Instruct datasets.

**Size**: 1800+ nested sequences

**Format**: JSON

**Annotation**: Each instance includes user queries, API specifications, and corresponding gold sequences.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Partial Match Accuracy
- Full Match Accuracy
- Win Rate

**Calculation**: Scores are calculated based on the alignment of predicted API sequences with gold standard outputs.

**Interpretation**: High scores indicate better performance in generating correct API sequences.

**Baseline Results**: GPT-4o achieves the best performance with a Full Match Accuracy of 28% and a Win Rate of 60%.

**Validation**: The benchmark was validated by executing the nested sequences to confirm the correct outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
