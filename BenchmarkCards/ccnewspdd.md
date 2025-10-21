# CCNewsPDD

## 📊 Benchmark Details

**Name**: CCNewsPDD

**Overview**: CCNewsPDD is a temporally unbiased benchmark for evaluating the Pre-Training Data Detection (PDD) task, employing rigorous data transformations to ensure consistent time distributions between training and non-training data.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ArxivMIA
- WikiMIA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop a reliable benchmark for detecting pre-training data in large language models using neuronal activation patterns.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Membership Inference

**Limitations**: NA-PDD requires access to model weights and activation information, making it unsuitable for closed-source models.

## 💾 Data

**Source**: CCNews corpus with data transformations including back translation, masking, and LLM rewriting.

**Size**: 1,200 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Neuronal Activation Determination
- Neuronal Identity Discrimination
- Membership Inference

**Metrics**:
- Area Under the ROC Curve (AUC)

**Calculation**: AUC is calculated based on the ratio of member neuron activation to non-member neuron activation for given data inputs.

**Interpretation**: Higher AUC indicates better performance in detecting whether specific data was part of the training corpus.

**Baseline Results**: NA-PDD significantly outperformed existing methods, achieving an AUC of 99.7% on CCNewsPDD.

**Validation**: Evaluated across three benchmark datasets with a focus on eliminating time drift confounding effects.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
