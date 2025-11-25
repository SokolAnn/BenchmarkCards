# Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques

## 📊 Benchmark Details

**Name**: Sarc7: Evaluating Sarcasm Detection and Generation with Seven Types and Emotion-Informed Techniques

**Overview**: Sarc7 is a benchmark for fine-grained sarcasm evaluation that operationalizes seven pragmatically defined sarcasm types: self-deprecating, brooding, deadpan, polite, obnoxious, raging, and manic, enabling nuanced understanding of sarcasm in large language models.

**Data Type**: sarcasm classification and generation

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SarcasmBench

**Resources**:
- [GitHub Repository](https://github.com/langlglang/sarc7)

## 🎯 Purpose and Intended Users

**Goal**: Provide a foundation for evaluating nuanced sarcasm understanding and controllable generation in language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Sarcasm Classification
- Sarcasm Generation

**Limitations**: The benchmark is limited by its reliance on textual data, lacking multimodal context essential for understanding sarcasm.

## 💾 Data

**Source**: MUStARD dataset with manual annotations

**Size**: 690 utterances

**Format**: CSV

**Annotation**: Manually annotated by four trained annotators using defined sarcasm types.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Macro-averaged F1 Score

**Calculation**: Metrics calculated based on model predictions compared to human-annotated labels.

**Interpretation**: Higher F1 scores indicate better model performance in distinguishing sarcasm types.

**Validation**: Cohen’s kappa calculated for inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
