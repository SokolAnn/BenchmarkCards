# EasyMath

## 📊 Benchmark Details

**Name**: EasyMath

**Overview**: EasyMath is a compact benchmark for practical math reasoning in small language models, covering thirteen categories from basic arithmetic to word problems, and assessing models' everyday math skills in a zero-shot setting.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GSM8K
- MathQA
- Hendrycks-MATH
- Math-500

**Resources**:
- [GitHub Repository](https://github.com/meta-llama/llama)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the real-world mathematical reasoning capabilities of small language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: The benchmark focuses on small language models and does not assess multilingual performance or reasoning over non-text modalities.

## 💾 Data

**Source**: Questions and solutions were manually created to ensure quality and relevance.

**Size**: N/A

**Format**: N/A

**Annotation**: Manually constructed by authors.

## 🔬 Methodology

**Methods**:
- Exact matching
- Numerical evaluation
- Symbolic equivalence checks

**Metrics**:
- Accuracy

**Calculation**: Responses are checked for exact, symbolic, or numerical equivalence to the correct answers.

**Interpretation**: Higher accuracy indicates better practical performance in everyday mathematical problem solving.

**Baseline Results**: N/A

**Validation**: Evaluation methods ensure robustness across diverse mathematical problem types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
