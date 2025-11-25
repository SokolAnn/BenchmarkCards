# Digikala dataset

## 📊 Benchmark Details

**Name**: Digikala dataset

**Overview**: The authors collected opinions from the DigiKala website to create an evaluation protocol for Persian/Arabic multi-domain sentiment analysis. They collected 50,799 opinions in 10 different areas and used this dataset (and an Amazon Arabic dataset) to evaluate multi-domain polarity detection and domain-of-belonging detection.

**Data Type**: text (customer review / opinion texts)

**Domains**:
- Natural Language Processing
- E-commerce (Product Reviews)

**Languages**:
- Persian
- Arabic

**Similar Benchmarks**:
- Oca (Opinion Corpus for Arabic)

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide a multi-domain sentiment analysis evaluation protocol/dataset for Persian and Arabic and to evaluate the proposed WcapsuleE method for simultaneous domain identification and sentiment polarity detection.

**Tasks**:
- Sentiment Analysis
- Domain Identification

**Limitations**: Collected data is highly unbalanced; the number of negative samples is much less than positive samples.

## 💾 Data

**Source**: Collected opinions from the DigiKala website (Persian) and collected opinions from Amazon (Arabic).

**Size**: 50,799 examples

**Format**: N/A

**Annotation**: Manual annotation. Polarity labeling defined as comments with a positive score of 4 or higher labeled positive, and those with less than two (stars) labeled negative.

## 🔬 Methodology

**Methods**:
- Automated metrics computed from confusion matrix
- Train/test split evaluation (80% train / 20% test)
- Cross-validation (5-fold)

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- Geometric mean (Gmean)

**Calculation**: Metrics are calculated from the confusion matrix using formulas provided in the paper: Precision = TP / (TP + FP); Recall = TP / (TP + FN); F1 Score = 2 * Precision * Recall / (Precision + Recall); Accuracy = (TP + TN) / (TP + TN + FP + FN); Geometric mean (Gmean) as defined in the paper.

**Interpretation**: Higher metric values indicate better performance. The paper compares models using these metrics but does not provide absolute thresholds for good vs. poor performance.

**Baseline Results**: Persian (80% train / 20% test): WcapsuleE test polarity accuracy = 0.9489 (train 0.9565); WcapsuleE + cost sensitivity test polarity accuracy = 0.9699 (train 0.9744). Domain identification: WcapsuleE test accuracy = 0.8020; WcapsuleE + cost sensitivity = 0.8212. Average per-domain accuracy (Persian): WcapsuleE = 0.9144; WcapsuleE + cost sensitivity = 0.9173. Arabic dataset: WcapsuleE polarity accuracy = 0.8607; WcapsuleE + cost sensitivity = 0.8698. Arabic domain classification: WcapsuleE = 0.9609; WcapsuleE + cost sensitivity = 0.9695. Comparisons with baseline models (CNN-MultiChannel, Character-level CNN, NeuroSent, Bi-GRUCapsule) are reported in tables.

**Validation**: 80% training / 20% testing split and cross-validation with fold=5 (5-fold cross-validation) are used for validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
