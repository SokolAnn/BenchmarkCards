# SAFETY ARITHMETIC

## 📊 Benchmark Details

**Name**: SAFETY ARITHMETIC

**Overview**: SAFETY ARITHMETIC is a training-free framework for aligning Large Language Models (LLMs) by steering them away from harmful directions and aligning their latent spaces towards safe content generation. It enhances safety measures for base, supervised fine-tuned, and edited models, while preserving their utility.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/declare-lab/safety-arithmetic)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive safety alignment framework for large language models across various utilization scenarios, reducing harmful outputs while maintaining model performance.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Safety Alignment
- Text Classification

**Limitations**: The framework's experiments involved models up to 7 billion parameters, limiting its applicability to larger models.

## 💾 Data

**Source**: NOINTENT EDIT dataset composed of edit instances which could compromise model safety if used unintentionally; evaluated using five established datasets.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Attack Success Rate (ASR)

**Calculation**: ASR is calculated as the proportion of responses deemed unsafe out of the total number of input queries to the model.

**Interpretation**: Lower ASR indicates better safety alignment performance of the model.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Harmful content generation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
