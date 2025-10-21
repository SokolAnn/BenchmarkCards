# TruthEval

## 📊 Benchmark Details

**Name**: TruthEval

**Overview**: TruthEval is a curated collection of challenging statements on sensitive topics for evaluating Large Language Models (LLMs), designed to measure their truthfulness and reliability.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TruthfulQA

**Resources**:
- [GitHub Repository](https://github.com/tanny411/TruthEval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' ability to understand truthfulness and reliability across various categories of statements.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Fact Verification

**Limitations**: The dataset should not be used for fine-tuning individual LLMs due to the ambiguous definitions of truth in some categories.

## 💾 Data

**Source**: Curated from Wikipedia, GPT-3 generated content, conspiracy theory papers, and external sources.

**Size**: 885 statements

**Format**: N/A

**Annotation**: Statements were labeled manually based on ground truth.

## 🔬 Methodology

**Methods**:
- LLM evaluation

**Metrics**:
- Accuracy

**Calculation**: Evaluation based on model responses to curated statements across different prompts.

**Interpretation**: Responses are analyzed for consistency and correctness in relation to the truth labels assigned.

**Baseline Results**: Evaluated using Mistral-7B model.

**Validation**: Initial analyses indicate LLMs struggle with answering based on the curated statements.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was gathered from publicly accessible sources and did not require external annotators.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
