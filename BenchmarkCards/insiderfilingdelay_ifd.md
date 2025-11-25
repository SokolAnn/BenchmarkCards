# InsiderFilingDelay (IFD)

## 📊 Benchmark Details

**Name**: InsiderFilingDelay (IFD)

**Overview**: The InsiderFilingDelay (IFD) dataset is the first large-scale, behavior-rich dataset specifically curated for detecting delayed insider filings in violation of SEC rules, containing over 4,051,143 labeled SEC Form 4 transactions from 2002 to 2025, enriched with structured attributes.

**Data Type**: transaction records

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/CH-YellowOrange/MaBoost-and-IFD)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset and framework for studying insider filing violations and regulatory compliance in financial markets.

**Target Audience**:
- Researchers
- Regulators
- Finance professionals

**Tasks**:
- Binary Classification

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from WRDS and processed in SAS, focusing on valid trades and excluding amended filings.

**Size**: 4,051,143 transactions

**Format**: N/A

**Annotation**: Annotated with binary labels indicating compliance or violation, and enriched with over 50 features.

## 🔬 Methodology

**Methods**:
- Hybrid framework combining Mamba-based sequence modeling with XGBoost classification

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the binary classification outcomes of the insider filing delays.

**Interpretation**: High values of Precision, Recall, and F1 Score indicate strong models in detecting violations.

**Baseline Results**: Compared against classical statistical models, deep learning baselines, and large language models with MaBoost outperforming them.

**Validation**: Cross-validation and hold-out sets for performance evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
