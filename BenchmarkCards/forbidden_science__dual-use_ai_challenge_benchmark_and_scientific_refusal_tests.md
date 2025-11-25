# Forbidden Science: Dual-Use AI Challenge Benchmark and Scientific Refusal Tests

## 📊 Benchmark Details

**Name**: Forbidden Science: Dual-Use AI Challenge Benchmark and Scientific Refusal Tests

**Overview**: This paper presents an open-source dataset and testing framework for evaluating large language model (LLM) safety mechanisms across controlled substance queries, analyzing four major models' responses to systematically varied prompts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- OR-Bench

**Resources**:
- [GitHub Repository](https://github.com/reveondivad/forbidden)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that allows for systematic evaluation of the balance between safety restrictions and potential over-censorship in scientific inquiry by LLMs.

**Target Audience**:
- AI Safety Researchers
- Model Developers
- Policy Makers

**Tasks**:
- Safety Evaluation
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available datasets from US government agencies (OSHA, FDA, EPA) and novel curated prompts.

**Size**: 512 prompts

**Format**: JSON

**Annotation**: Manually curated by researchers with a focus on dual-use scientific queries.

## 🔬 Methodology

**Methods**:
- Red Team Testing
- Quantitative Analysis
- Chain-of-Thought Analysis

**Metrics**:
- Refusal Rate
- Response Consistency

**Calculation**: Measured response refusal rates and analyzed the variability in responses across different prompt engineering strategies.

**Interpretation**: The analysis aims to detect the effectiveness of model responses in handling sensitive scientific queries without unnecessary censorship.

**Validation**: Results were validated by comparing responses across major LLMs against established literature.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Potential misuse of scientific information']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
