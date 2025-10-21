# Nvr-X-MMLU

## 📊 Benchmark Details

**Name**: Nvr-X-MMLU

**Overview**: Nvr-X-MMLU is a variation of the MMLU benchmark designed to mitigate the base-rate effect and disambiguate test-taking ability from actual task performance.

**Data Type**: multiple choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)

**Resources**:
- [GitHub Repository](https://github.com/KyleAMoore/MMLU-cloze-vs-cf)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more accurate measure of model performance by mitigating the biases introduced by base-rate probabilities in multiple choice question answering.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: LLMs were not tested with models larger than 10B parameters and results may vary with other model architectures.

## 💾 Data

**Source**: The Nvr-X variants are constructed from the MMLU dataset.

**Size**: 15,908 multiple choice questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the minimum accuracy over the four Nvr-X variation sets.

**Interpretation**: Lower accuracy on Nvr-X-MMLU indicates a strong preference for certain answer choices; higher accuracy suggests better understanding of the questions.

**Baseline Results**: N/A

**Validation**: Evaluated using cloze and counterfactual prompting methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
