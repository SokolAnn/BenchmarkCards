# HVVMemes (Hero, Villain, Victim, and Other) & HVVMemes-2 (Hero, Villain, Victim, and Other)

## 📊 Benchmark Details

**Name**: HVVMemes (Hero, Villain, Victim, and Other) & HVVMemes-2 (Hero, Villain, Victim, and Other)

**Overview**: This benchmark evaluates narrative role classification in Internet memes across multilingual and multimodal models, addressing categories such as Hero, Villain, Victim, and Other.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Hindi

**Similar Benchmarks**:
- Hateful Memes

**Resources**:
- [Resource](https://arxiv.org/abs/2506.23122)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the task of identifying narrative roles in memes across diverse cultural and linguistic contexts.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Narrative Role Classification

**Limitations**: The persistent challenge of accurately identifying the 'Victim' class and generalization across cultural and code-mixed contexts.

## 💾 Data

**Source**: Originally from the HVVMemes dataset, extended and diversified for CLEF 2024 shared task.

**Size**: 5,000 examples

**Format**: CSV

**Annotation**: Manual annotation for narrative roles by researchers.

## 🔬 Methodology

**Methods**:
- Zero-shot model evaluation
- Prompt engineering tests
- Performance benchmarking across 25+ models

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated across four narrative classes (Hero, Villain, Victim, Other).

**Interpretation**: F1 Scores indicate the effectiveness of models in classifying narrative roles, with higher scores reflecting better model performance.

**Baseline Results**: DeBERTa-v3 achieved the highest macro F1 score of 0.54.

**Validation**: Comparative performance across multiple model architectures and framework settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt leaking

**Demographic Analysis**: Analysis of performance across narrative roles identifies challenges in cultural representation.

**Potential Harm**: Potential misclassification of narrative roles that may perpetuate cultural stereotypes.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
