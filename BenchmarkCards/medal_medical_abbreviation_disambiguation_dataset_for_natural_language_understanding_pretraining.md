# MeDAL (Medical Abbreviation Disambiguation Dataset for Natural Language Understanding Pretraining)

## 📊 Benchmark Details

**Name**: MeDAL (Medical Abbreviation Disambiguation Dataset for Natural Language Understanding Pretraining)

**Overview**: MeDAL is a large medical text dataset curated for abbreviation disambiguation, designed for natural language understanding pre-training in the medical domain.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/BruceWen120/medal)

## 🎯 Purpose and Intended Users

**Goal**: To enable effective pre-training and improve performance on downstream medical tasks during fine-tuning.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Abbreviation Disambiguation
- Mortality Prediction
- Diagnosis Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Created from PubMed abstracts released in 2019

**Size**: 14,393,619 articles

**Format**: N/A

**Annotation**: Generated using reverse substitution techniques, without human labeling.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Top-k recall
- Accuracy

**Calculation**: Top-k recall is calculated as the number of diagnosis codes present in the top k predictions of the model divided by the total number of diagnosis codes in that admission.

**Interpretation**: Higher top-k recall values indicate better performance of models at predicting relevant diagnoses.

**Baseline Results**: LSTM: 82.80% test accuracy (pre-trained), ELECTRA: 84.43% test accuracy (pre-trained)

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
