# MIB (Mechanistic Interpretability Benchmark)

## 📊 Benchmark Details

**Name**: MIB (Mechanistic Interpretability Benchmark)

**Overview**: MIB is a Mechanistic Interpretability Benchmark that facilitates the evaluation of mechanistic interpretability methods by comparing their ability to locate and validate task mechanisms or specific concepts in neural language models. It features two tracks: circuit localization and causal variable localization, with evaluations spanning four tasks across five models.

**Data Type**: task-based evaluation datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RA VEL
- CausalGym

**Resources**:
- [Resource](https://huggingface.co/datasets/mib)
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To establish stable standards for comparing mechanistic interpretability methods in a principled manner.

**Target Audience**:
- Researcher in AI Safety
- ML Researchers
- Interpretability Researchers

**Tasks**:
- Circuit Localization
- Causal Variable Localization

**Limitations**: N/A

## 💾 Data

**Source**: Tasks involve synthetic datasets composed of well-defined questions

**Size**: 10000 examples for each task

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Intervention evaluations

**Metrics**:
- Accuracy
- Faithfulness

**Calculation**: Metrics are calculated using a range of evaluation tasks and results from model outputs.

**Interpretation**: Higher accuracy and faithfulness scores indicate a better understanding of model mechanisms.

**Baseline Results**: N/A

**Validation**: Performance is validated against established models and tasks with set benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
