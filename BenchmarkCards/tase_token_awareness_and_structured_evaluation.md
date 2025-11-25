# TASE (Token Awareness and Structured Evaluation)

## 📊 Benchmark Details

**Name**: TASE (Token Awareness and Structured Evaluation)

**Overview**: TASE is a comprehensive benchmark designed to evaluate LLMs’ ability to perceive and reason about token-level information across languages, covering 10 tasks under two core categories: token awareness and structural understanding.

**Data Type**: evaluation instances

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English
- Korean

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- XNLI

**Resources**:
- [GitHub Repository](https://github.com/cyzcz/Tase)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the fine-grained capabilities of large language models (LLMs) and address their limitations in token-level awareness and structural reasoning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Token Awareness
- Structural Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Curated evaluation set and a scalable synthetic data generation pipeline.

**Size**: 35,928 instances

**Format**: N/A

**Annotation**: Programmatically generated with known solutions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on raw accuracy compared to a human baseline.

**Interpretation**: Higher accuracy indicates a better understanding of token-level and structural tasks.

**Baseline Results**: Human accuracy averages 89.24%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
