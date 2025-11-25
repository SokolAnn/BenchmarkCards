# MS CINLI: A Diverse Benchmark for Scientific Natural Language Inference

## 📊 Benchmark Details

**Name**: MS CINLI: A Diverse Benchmark for Scientific Natural Language Inference

**Overview**: MS CINLI is a dataset containing 132,320 sentence pairs extracted from research articles in five domains: 'Hardware', 'Networks', 'Software & its Engineering', 'Security & Privacy', and 'NeurIPS', aimed at evaluating scientific Natural Language Inference (NLI) tasks.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SCINLI

**Resources**:
- [GitHub Repository](https://github.com/msadat3/MSciNLI)

## 🎯 Purpose and Intended Users

**Goal**: To introduce diversity in the scientific NLI task and provide a challenging benchmark for evaluating models' reasoning and inference capabilities on scientific texts.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Natural Language Inference

**Limitations**: MS CINLI presents challenges for both traditional PLMs and state-of-the-art LLMs, indicating there is room for improvement in model performance.

## 💾 Data

**Source**: Sentence pairs extracted from scientific articles published in various domains.

**Size**: 132,320 sentence pairs

**Format**: text

**Annotation**: Automatic labeling using distant supervision and manual annotation by experts.

## 🔬 Methodology

**Methods**:
- Fine-tuning Pre-trained Language Models (PLMs)
- Prompting Large Language Models (LLMs)

**Metrics**:
- Macro F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on model predictions against human-annotated labels.

**Interpretation**: Higher Macro F1 and accuracy scores indicate better model understanding and agreement with human judgments.

**Baseline Results**: The best performing PLM baseline, ROBERTA, achieves a Macro F1 of 77.21%. The best LLM baseline, LLAMA-2, reaches a Macro F1 of 51.77%.

**Validation**: Models were validated using development sets and cross-validated against test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: The dataset involves diverse domains which contribute to the potential for demographic analysis.

**Potential Harm**: The performance gap between human annotators and models indicates potential harm in misclassification.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
