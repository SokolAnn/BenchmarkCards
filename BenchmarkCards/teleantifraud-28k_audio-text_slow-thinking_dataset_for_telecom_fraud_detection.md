# TeleAntiFraud-28k (Audio-Text Slow-Thinking Dataset for Telecom Fraud Detection)

## 📊 Benchmark Details

**Name**: TeleAntiFraud-28k (Audio-Text Slow-Thinking Dataset for Telecom Fraud Detection)

**Overview**: TeleAntiFraud-28k is the first open-source audio-text slow-thinking dataset specifically designed for automated telecom fraud analysis, comprised of 28,511 rigorously processed audio-text pairs with detailed annotations for fraud reasoning.

**Data Type**: audio-text pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/JimmyMa99/TeleAntiFraud)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for the development and evaluation of automated telecom fraud detection models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Scenario Classification
- Fraud Detection
- Fraud Type Classification

**Limitations**: N/A

## 💾 Data

**Source**: Generated through real call ASR processing, large language model imitation, and multi-agent adversarial synthesis.

**Size**: 28,511 audio-text pairs

**Format**: N/A

**Annotation**: Annotations performed through slow-thinking reasoning with models generating structured outputs for various fraud-related tasks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score

**Calculation**: Weighted F1 scores calculated as accuracy metrics across various classification tasks.

**Interpretation**: Higher F1 scores indicate better classification performance across scenario, fraud, and fraud type tasks.

**Baseline Results**: The AntiFraud-Qwen2-Audio model achieved an 83% average F1 score in evaluations.

**Validation**: Systematic evaluations against the TeleAntiFraud-Bench evaluation framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymized audio data used to protect user identities during dataset creation.

**Data Licensing**: Open source for community-driven dataset expansion.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
