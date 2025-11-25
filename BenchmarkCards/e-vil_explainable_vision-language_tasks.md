# e-ViL (Explainable Vision-Language Tasks)

## 📊 Benchmark Details

**Name**: e-ViL (Explainable Vision-Language Tasks)

**Overview**: e-ViL is a benchmark for explainable vision-language tasks that establishes a unified evaluation framework and provides comprehensive comparisons of existing approaches generating natural language explanations (NLEs) for vision-language tasks. The benchmark spans four models and three datasets and incorporates both automatic metrics and human evaluation.

**Data Type**: natural language explanations and image-text pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- e-SNLI-VE

**Resources**:
- [GitHub Repository](https://github.com/maximek3/e-ViL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified evaluation framework for comparing models that generate natural language explanations for vision-language tasks.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Visual Question Answering
- Natural Language Explanation Generation

**Limitations**: N/A

## 💾 Data

**Source**: e-SNLI-VE dataset, generated from e-SNLI and SNLI-VE datasets.

**Size**: 430,796 instances

**Format**: image and accompanying text pairs with explanations

**Annotation**: Annotated by humans via Amazon Mechanical Turk, including relabeling of explanations and labels.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Accuracy determined by correct predictions; F1 Score, BLEU Score, and ROUGE-L calculated based on generated explanations compared to human-written ones.

**Interpretation**: Higher scores indicate better performance in generating accurate explanations.

**Baseline Results**: N/A

**Validation**: Evaluation conducted via crowdsourcing, with multiple annotators assessing each explanation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination, Evasion attack
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
