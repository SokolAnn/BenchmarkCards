# PARADEHATE (Parallel Dataset for Hate Speech Detoxification)

## 📊 Benchmark Details

**Name**: PARADEHATE (Parallel Dataset for Hate Speech Detoxification)

**Overview**: PARADEHATE is a large-scale parallel dataset specifically for hate speech detoxification, consisting of over 8,000 hate/non-hate text pairs, generated through an LLM-in-the-loop methodology replacing human annotators.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ScaDS-AI/ParaDeHate)

## 🎯 Purpose and Intended Users

**Goal**: To provide a high-quality parallel dataset for evaluating models in the task of online hate speech detoxification.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Text Detoxification

**Limitations**: N/A

## 💾 Data

**Source**: Aggregated from multiple hate speech datasets including CreHate, HateXplain, Davidson, and Founta.

**Size**: 8,276 examples

**Format**: text pairs

**Annotation**: Automated generation and validation using LLMs for rephrasing, content preservation checking, and toxicity evaluation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Style Accuracy
- Content Preservation
- Fluency
- BLEU Score

**Calculation**: Metrics calculated by comparing LLM-generated texts against original references and assessing semantic fidelity.

**Interpretation**: Higher scores indicate better performance in detoxification tasks.

**Baseline Results**: BART fine-tuned on PARADEHATE achieves style accuracy of 0.95, content preservation of 0.78, and fluency of 0.71.

**Validation**: Dataset was validated through comparison with traditional methods and human-annotated data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
