# PL-Guard

## 📊 Benchmark Details

**Name**: PL-Guard

**Overview**: We introduce PL-Guard, a manually verified Polish-language benchmark for safety classification, along with PL-Guard-adv, its adversarial extension featuring text perturbations to evaluate model robustness.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- WildGuard
- PolyGuard

**Resources**:
- [Resource](https://huggingface.co/collections/NASK-PIB/PL-Guard-684945df2cff1837f1bc6e95)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation of language model safety specifically for Polish, addressing the gap in non-English safety evaluation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Safety Classification

**Limitations**: N/A

## 💾 Data

**Source**: Manually annotated Polish-language data and translated datasets from WildGuard and PolyGuard.

**Size**: 7,000 samples for PL-Guard; 900 samples for PL-Guard-test.

**Format**: N/A

**Annotation**: Manual review and re-annotation by trained annotators with high inter-annotator agreement.

## 🔬 Methodology

**Methods**:
- Fine-tuning
- Adversarial testing

**Metrics**:
- F1 Score

**Calculation**: Calculated as macro F1 scores for binary safety and multiclass hazard categories.

**Interpretation**: Higher F1 scores indicate better performance in detecting unsafe outputs.

**Baseline Results**: HerBERT-based classifier achieves high performance on safety classification tasks.

**Validation**: Evaluated using both original and adversarial test datasets to assess robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
