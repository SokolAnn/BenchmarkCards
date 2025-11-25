# TRACE (Testing Robustness for Automated Complex instruction Evaluation)

## 📊 Benchmark Details

**Name**: TRACE (Testing Robustness for Automated Complex instruction Evaluation)

**Overview**: TRACE is a benchmark for enhancing the ability of large language models (LLMs) to follow complex instructions, consisting of 120K training data and 1K evaluation data.

**Data Type**: complex instruction pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CFBench
- IFEval
- INFOBENCH

**Resources**:
- [GitHub Repository](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/IOPO)

## 🎯 Purpose and Intended Users

**Goal**: To improve and evaluate the capability of LLMs to follow complex instructions.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Instruction Following

**Limitations**: The evaluation set has undergone strict manual verification, but the training set has not.

## 💾 Data

**Source**: Automatically constructed from manually sorted taxonomy of complex instructions with 26 constraint dimensions within 5 constraint types.

**Size**: 120,000 training examples and 1,042 evaluation examples

**Format**: JSON

**Annotation**: Generated using an automated data construction workflow and manually verified for evaluation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Instruction Following Score

**Calculation**: The overall instruction following score (I) is calculated based on adherence to constraints in the evaluation.

**Interpretation**: Higher scores indicate better adherence to the specific constraints outlined in complex instructions.

**Validation**: Extensive experiments on various datasets confirmed the effectiveness of TRACE.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data does not include personal data or sensitive information.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
