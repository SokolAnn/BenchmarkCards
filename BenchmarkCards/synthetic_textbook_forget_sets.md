# Synthetic Textbook Forget Sets

## 📊 Benchmark Details

**Name**: Synthetic Textbook Forget Sets

**Overview**: This work presents a scalable, automated approach to generate high-quality forget sets using language models for the purpose of unlearning sensitive knowledge in large language models. The generated synthetic datasets are evaluated against expert-curated sets and baseline alternatives.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WMDP

**Resources**:
- [GitHub Repository](https://github.com/xyzhu123/Synthetic Textbook)

## 🎯 Purpose and Intended Users

**Goal**: To provide a method for constructing synthetic forget sets to facilitate the unlearning of sensitive knowledge from language models.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Machine Unlearning

**Limitations**: N/A

## 💾 Data

**Source**: Generated using a large language model with structured prompting.

**Size**: 20,000 sentences

**Format**: Text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Unlearn Utility

**Calculation**: Unlearn utility computed as a trade-off between forgetting performance and retention of general capabilities.

**Interpretation**: Higher unlearn utility indicates more effective unlearning with preserved general capabilities.

**Baseline Results**: Evaluated against expert-curated and baseline synthetic datasets.

**Validation**: Results validated through comparative experiments against baseline unlearning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
