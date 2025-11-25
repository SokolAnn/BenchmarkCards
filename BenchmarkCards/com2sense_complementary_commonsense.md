# COM2SENSE (Complementary Commonsense)

## 📊 Benchmark Details

**Name**: COM2SENSE (Complementary Commonsense)

**Overview**: A new commonsense reasoning benchmark dataset comprising 4,000 natural language true/false statements, with each sample paired with its complementary counterpart. It aims to assess AI's commonsense reasoning ability with a pairwise accuracy metric.

**Data Type**: true/false statement pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/PlusLabNLP/Com2Sense)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging evaluation benchmark for commonsense reasoning abilities in NLP models.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Collected via Amazon Mechanical Turk (MTurk) with an adversarial model-in-the-loop approach.

**Size**: 4,000 statement pairs

**Format**: CSV

**Annotation**: Crowdsourced, with quality checks by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Standard Accuracy
- Pairwise Accuracy

**Calculation**: Pairwise accuracy requires both statements in a pair to be correct.

**Interpretation**: Higher accuracy indicates better commonsense reasoning ability.

**Baseline Results**: UniﬁedQA-3B achieves ~71% standard accuracy and ~51% pairwise accuracy.

**Validation**: Dataset validation was conducted by internal members for consistency and quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Personal information of workers was discarded during dataset creation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: This work has been reviewed by the IRB and granted exempt status.
