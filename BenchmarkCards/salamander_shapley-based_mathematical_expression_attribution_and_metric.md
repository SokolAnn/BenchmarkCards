# SalaMAnder (Shapley-based Mathematical Expression Attribution and Metric)

## 📊 Benchmark Details

**Name**: SalaMAnder (Shapley-based Mathematical Expression Attribution and Metric)

**Overview**: SalaMAnder is a framework that employs Shapley-based attribution to enhance understanding and optimization of Chain-of-Thought reasoning in large language models, focusing on few-shot mathematical problem-solving.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MathQA
- AQUA
- MultiArith
- SV AMP

**Resources**:
- [Resource](https://arxiv.org/abs/2509.16561)

## 🎯 Purpose and Intended Users

**Goal**: To provide a theoretical foundation and practical framework for understanding the contributions of components in Chain-of-Thought reasoning for large language models.

**Target Audience**:
- ML Researchers
- Data Scientists
- Model Developers

**Tasks**:
- Mathematical Problem Solving
- Chain-of-Thought Reasoning Analysis

**Limitations**: Currently limited to mathematical reasoning problems; aiming to broaden application in future.

## 💾 Data

**Source**: Utilized existing mathematical benchmarks (GSM8K, MathQA, AQUA, MultiArith, SV AMP).

**Size**: Multiple datasets utilized, specifics vary.

**Format**: Text-based question-answer pairs

**Annotation**: Data derived from pre-existing benchmarks

## 🔬 Methodology

**Methods**:
- Automated metrics
- Statistical analysis

**Metrics**:
- CoSP (Cardinality of Shapley Positives)

**Calculation**: Involves Shapley value calculations to quantify contributions of mathematical expressions in reasoning.

**Interpretation**: High CoSP values indicate stronger contributions to model performance, while low values suggest minimal influence.

**Validation**: Empirical validation across various models and datasets to demonstrate robustness and correlation with model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
