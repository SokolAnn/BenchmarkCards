# PaCoST (Paired Confidence Significance Testing for Benchmark Contamination Detection)

## 📊 Benchmark Details

**Name**: PaCoST (Paired Confidence Significance Testing for Benchmark Contamination Detection)

**Overview**: PaCoST is a method for detecting benchmark contamination in large language models (LLMs) by using paired confidence significance testing to assess whether models are significantly more confident when responding to original benchmarks compared to rephrased questions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/lleozhang/PaCoST)

## 🎯 Purpose and Intended Users

**Goal**: To effectively detect benchmark contamination in large language models (LLMs) and ensure the integrity of model evaluations.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Benchmark Contamination Detection

**Limitations**: The method focuses on detecting benchmark-level contamination and is not suitable for instance-level contamination.

## 💾 Data

**Source**: Various popular LLMs and benchmarks including MMLU, HellaSwag, and TruthfulQA.

**Size**: Results presented as p-values analyzed from various models across sampled benchmarks.

**Format**: N/A

**Annotation**: Statistical analysis based on confidence scores obtained from rephrased instances and original questions.

## 🔬 Methodology

**Methods**:
- Statistical analysis
- Paired samples t-test

**Metrics**:
- Statistical significance (p-value)

**Calculation**: The method calculates the probability of the model being more confident using a t-test to compare original and rephrased confidence scores.

**Interpretation**: A p-value less than 0.05 indicates suspected contamination of the benchmark.

**Baseline Results**: N/A

**Validation**: Validated through experiments on popular open-source models and various benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: The method aims to reduce the potential harm associated with misleading evaluation results due to contamination.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
