# SYMPCODER

## 📊 Benchmark Details

**Name**: SYMPCODER

**Overview**: SYMPCODER is a human-annotated dataset derived from Vaccine Adverse Event Reporting System (VAERS) reports, designed to benchmark the performance of models for symptom coding in medical contexts. It includes three variants targeting both common and rare symptoms.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LEAF-Lab-Stevens/TACO-Prompting)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating model performance across diverse cases in medical symptom coding.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Symptom Extraction
- Symptom Linking

**Limitations**: N/A

## 💾 Data

**Source**: Vaccine Adverse Event Reporting System (VAERS) reports

**Size**: 487 reports

**Format**: N/A

**Annotation**: Human-annotated by a team of experts following a rigorous validation process.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- Fuzzy Match
- Precision
- Recall
- BLEU Score

**Calculation**: Metrics are calculated based on the two-stage evaluation framework assessing linking accuracy and mention coherence.

**Interpretation**: Higher scores in EM and Fuzzy metrics indicate better model performance in accurately linking symptoms and extracting coherent mentions.

**Validation**: The dataset underwent thorough annotation and validation by trained annotators and validators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
