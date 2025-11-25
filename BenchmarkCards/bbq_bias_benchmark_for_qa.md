# BBQ (Bias Benchmark for QA)

## 📊 Benchmark Details

**Name**: BBQ (Bias Benchmark for QA)

**Overview**: BBQ is designed to test bias in large language models (LLMs) on social domains, featuring polarized questions and demographic targets.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- CrowS-pairs

**Resources**:
- [GitHub Repository](https://github.com/nyu-mll/BBQ)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate bias in large language models by measuring responses to polarized questions across various demographic identities.

**Target Audience**:
- ML Researchers
- Ethics Researchers
- AI Developers

**Tasks**:
- Bias Measurement
- Question Answering

**Limitations**: The demographic groups considered are not exhaustive and the study is limited to the BBQ dataset.

## 💾 Data

**Source**: BBQ dataset (Parrish et al., 2022)

**Size**: 3,432 questions

**Format**: CSV

**Annotation**: Manually crafted by researchers

## 🔬 Methodology

**Methods**:
- Question Answering

**Metrics**:
- TARGET BIAS (TB)
- BIAS AMOUNT (BAMT)
- PERSONA BIAS (PB)

**Calculation**: Metrics are calculated based on the responses of LLMs to questions framed with assigned personas, evaluating bias by summing perception scores.

**Interpretation**: Higher absolute values in bias metrics indicate stronger biases displayed by the model towards specific demographic identities.

**Baseline Results**: None provided

**Validation**: Metrics validated through experiments on multiple LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis includes various demographic identities across age, race, religion, socioeconomic status, and sexual orientation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
