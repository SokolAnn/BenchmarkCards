# REFNLI

## 📊 Benchmark Details

**Name**: REFNLI

**Overview**: REFNLI is a diagnostic benchmark for identifying reference ambiguity in Natural Language Inference (NLI) examples, featuring 1,143 pairs where the premise is retrieved from a knowledge source and does not necessarily refer to the same context as the hypothesis.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/refnli-authors/refnli)

## 🎯 Purpose and Intended Users

**Goal**: To study the effect of reference determinacy in NLI and the impact of this common assumption in the creation processes of NLI datasets.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed by sampling claims from the validation and test splits of fact verification datasets (FEVER and VitaminC) and retrieving corresponding evidence from Wikipedia.

**Size**: 1,143 examples

**Format**: N/A

**Annotation**: Annotated by expert raters with 4 labels (Entailment, Contradiction, Neutral, Ambiguous).

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Precision
- Recall
- AUROC

**Calculation**: Metrics are computed based on the output label token with the highest softmax probability.

**Interpretation**: Higher precision and recall values indicate better model performance in recognizing entailment and contradiction.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
