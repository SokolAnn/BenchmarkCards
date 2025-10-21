# FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets

## 📊 Benchmark Details

**Name**: FinGPT: Instruction Tuning Benchmark for Open-Source Large Language Models in Financial Datasets

**Overview**: The paper introduces a benchmarking scheme designed for end-to-end training and testing of open-source Large Language Models (LLMs) in financial contexts, emphasizing instruction tuning for various NLP tasks within finance.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FLUE
- PIXIU

**Resources**:
- [GitHub Repository](https://github.com/AI4Finance-Foundation/FinGPT)
- [GitHub Repository](https://github.com/AI4Finance-Foundation/FinGPT/tree/master/fingpt/FinGPT_Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate the benchmarking of open-source Large Language Models in the financial sector through a comprehensive instruction tuning approach.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Named Entity Recognition
- Sentiment Analysis
- Relation Extraction
- Headline Classification

**Limitations**: N/A

## 💾 Data

**Source**: Financial datasets adapted from the FLUE benchmark and others for specific tasks.

**Size**: 10,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Task-Specific Instruction Tuning
- Multi-Task Instruction Tuning
- Zero-Shot Instruction Tuning

**Metrics**:
- F1 Score

**Calculation**: Metrics are calculated based on entity-level and relation-only F1 scores for financial NLP tasks.

**Interpretation**: Higher F1 scores indicate better performance on sentiment analysis, NER, headline classification, and relation extraction tasks.

**Baseline Results**: Llama2, Falcon, MPT, BLOOM, ChatGLM2, and Qwen were evaluated across multiple tasks.

**Validation**: Comprehensive validation across tasks to ensure effectiveness of each model.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
