# Default Dataset

## 📊 Benchmark Details

**Name**: Default Dataset

**Overview**: We introduce a new open dataset featuring financial transactions with credit default labels, enhancing the scope for practical research and development.

**Data Type**: sequences of financial transactions

**Domains**:
- Finance

**Languages**:
- N/A

**Similar Benchmarks**:
- Churn Dataset

**Resources**:
- [Resource](https://vorsineo.github.io/adv_mltournament/#subsection4)

## 🎯 Purpose and Intended Users

**Goal**: To explore effective attacks and defenses for models trained for classification tasks related to credit default in financial transactions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Binary Classification

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is composed of anonymized financial transaction sequences with credit default labels.

**Size**: Between 4,000 to 7,000 sequences per fold

**Format**: N/A

**Annotation**: Manual encoding of credit default target based on transaction sequences.

## 🔬 Methodology

**Methods**:
- Competitions for attack and defense strategies

**Metrics**:
- ROC AUC

**Calculation**: Difference in ROC AUC values between model predictions for the original and adversarially altered transaction sequences.

**Interpretation**: Higher ROC AUC indicates better model performance against adversarial attacks.

**Baseline Results**: N/A

**Validation**: Competition structure with different phases to assess model robustness through direct confrontations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User names are replaced with identification numbers, and transaction amounts are anonymized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
