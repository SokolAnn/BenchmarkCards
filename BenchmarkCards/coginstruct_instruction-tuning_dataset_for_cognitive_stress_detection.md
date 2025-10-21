# CogInstruct (Instruction-Tuning Dataset for Cognitive Stress Detection)

## 📊 Benchmark Details

**Name**: CogInstruct (Instruction-Tuning Dataset for Cognitive Stress Detection)

**Overview**: CogInstruct is an instruction-tuning dataset designed for cognitive stress detection, leveraging a three-stage self-reflective annotation pipeline to create cognition chain data that enhances explainability in psychological stress detection from social media.

**Data Type**: cognition chain data

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2412.14009)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset that improves instruction-tuning for stress detection models based on cognitive appraisal theory.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Stress Detection
- Explainable AI

**Limitations**: The quality and quantity of the cognition chain dataset are critical for model performance, and high-quality manual labeling is required.

## 💾 Data

**Source**: Automatically generated from social media posts, verified by experts.

**Size**: 4,282 examples

**Format**: JSON

**Annotation**: Three-stage self-reflection annotation pipeline using LLMs and manual verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated based on predictions compared to human labeled data.

**Interpretation**: Higher metrics indicate better performance in detecting stress and explaining reasoning.

**Validation**: Performance was validated through comparisons with established stress detection models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Explainability

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Explainability**: Unexplainable output

**Demographic Analysis**: The dataset comprises diverse social media posts reflecting different stress experiences.

**Potential Harm**: Potential for inadequate support if misinterpreted stress conditions are identified.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data sourced from public social media platforms with no personal identifiers retained.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
