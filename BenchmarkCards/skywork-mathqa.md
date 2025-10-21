# Skywork-MathQA

## 📊 Benchmark Details

**Name**: Skywork-MathQA

**Overview**: Skywork-MathQA is a dataset consisting of 2.5 million diverse and high-quality synthetic instances specifically designed to enhance the mathematical reasoning capabilities of large language models (LLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GSM8K
- MATH

**Resources**:
- [Resource](https://arxiv.org/abs/2407.08348)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the data scaling laws for mathematical reasoning capabilities in LLMs and to provide a high-quality dataset that enhances their performance.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Mathematical Reasoning
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic data generated using GPT-4 along with normal and hard synthetic problems designed for mathematical reasoning.

**Size**: 2.5 million instances

**Format**: JSON

**Annotation**: Automatically generated and augmented through a two-stage data synthesis process.

## 🔬 Methodology

**Methods**:
- Supervised Fine-Tuning (SFT)
- Data augmentation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on performance on the GSM8K and MATH benchmarks.

**Interpretation**: Higher accuracy indicates better mathematical reasoning performance of the models evaluated.

**Validation**: The dataset and models were validated against the GSM8K and MATH benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
