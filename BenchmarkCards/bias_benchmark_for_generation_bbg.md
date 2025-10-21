# Bias Benchmark for Generation (BBG)

## 📊 Benchmark Details

**Name**: Bias Benchmark for Generation (BBG)

**Overview**: The Bias Benchmark for Generation (BBG) is designed to evaluate social bias in long-form generation by having large language models generate continuations of story prompts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Korean

**Similar Benchmarks**:
- Bias Benchmark for Question Answering (BBQ)

**Resources**:
- [Resource](https://jinjh0123.github.io/BBG)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the social bias of large language models in generating story continuations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text Generation

**Limitations**: BBG captures only the stereotypes addressed in the BBQ and KoBBQ datasets.

## 💾 Data

**Source**: Constructed from BBQ (Parrish et al., 2022) and KoBBQ (Jin et al., 2024) datasets.

**Size**: 82,136 pairs of seed stories and QA for English, 38,316 pairs for Korean

**Format**: N/A

**Annotation**: Adjusted from existing datasets to ensure neutral and unbiased story generation.

## 🔬 Methodology

**Methods**:
- Machine reading comprehension evaluations
- Comparison with multiple-choice question answering

**Metrics**:
- Neutral generation score (ntr_gen)
- Bias score (bias_gen)

**Calculation**: Neutrality and bias scores calculated based on the associations made by language models in generated narratives.

**Interpretation**: A higher neutrality score indicates more neutral story outputs, while a lower bias score indicates fewer bias-aligned outputs.

**Validation**: Reliability tested using human annotators' assessments against model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: Evaluates social bias across various categories including age, gender, and socioeconomic status.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dataset does not contain personally identifying information.

**Data Licensing**: MIT License for BBG dataset.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
