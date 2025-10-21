# PromptShield

## 📊 Benchmark Details

**Name**: PromptShield

**Overview**: PromptShield is a benchmark for training and evaluating deployable prompt injection detectors, carefully curated and including both conversational and application-structured data. It aims to reflect realistic deployment settings and improve detector performance in identifying prompt injections.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/hendzh/PromptShield)
- [GitHub Repository](https://github.com/wagner-group/PromptShield)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for training and evaluating prompt injection detectors in realistic deployment scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Prompt Injection Detection

**Limitations**: N/A

## 💾 Data

**Source**: Curated from open-source datasets and prompt injection attack strategies, including Ultrachat, LMSYS, Alpaca, and others.

**Size**: 20,000 examples

**Format**: CSV

**Annotation**: Manually curated and automatically generated based on existing strategies.

## 🔬 Methodology

**Methods**:
- Binary classification
- Fine-tuning on curated data
- Validation using distinct data splits

**Metrics**:
- Area Under ROC Curve (AUC)
- True Positive Rate (TPR) at low False Positive Rates (FPR)

**Calculation**: Metrics calculated based on the model's performance on the evaluation split, focusing on TPR at various FPR thresholds.

**Interpretation**: High TPR at low FPR thresholds indicates effective detection performance; the goal is to achieve low FPRs while maintaining high TPR.

**Baseline Results**: Performance of prior detectors such as PromptGuard, which shows significant improvement with the PromptShield detector.

**Validation**: Detectors are validated through training/evaluation splits that do not overlap, ensuring robust performance assessment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
