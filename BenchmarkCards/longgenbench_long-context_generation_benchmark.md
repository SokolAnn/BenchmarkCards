# LongGenBench (Long-context Generation Benchmark)

## 📊 Benchmark Details

**Name**: LongGenBench (Long-context Generation Benchmark)

**Overview**: LongGenBench is a synthetic benchmark designed to evaluate the long-context generation capabilities of large language models (LLMs), focusing on consistency in logical flow across lengthy passages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- GSM8K
- CommonSenseQA

**Resources**:
- [GitHub Repository](https://github.com/Dominic789654/LongGenBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive assessment of the long-context generation capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Long-context Generation
- Question Answering

**Limitations**: The experiments were conducted on a limited set of models and datasets.

## 💾 Data

**Source**: Synthesized from existing popular LLM benchmarks: MMLU, GSM8K, CommonSenseQA.

**Size**: 16,000 examples

**Format**: Synthetic textual data

**Annotation**: Generated with automated methods.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Comparative evaluations

**Metrics**:
- Accuracy

**Calculation**: Measured by comparing generated long-context responses with ground truth answers.

**Interpretation**: Lower accuracy percentages indicate greater performance degradation in long-context scenarios.

**Validation**: Experiment results averaged from three runs for robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: All datasets used are released under MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
