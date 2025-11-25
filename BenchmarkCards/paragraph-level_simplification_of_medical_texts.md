# Paragraph-level Simplification of Medical Texts

## 📊 Benchmark Details

**Name**: Paragraph-level Simplification of Medical Texts

**Overview**: This work introduces a new corpus of parallel texts in English comprising technical and lay summaries of all published evidence pertaining to different clinical topics. It aims to improve accessibility to medical information by developing automated approaches to text simplification.

**Data Type**: paired texts

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AshOlogn/Paragraph-level-Simplification-of-Medical-Texts)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research into the automated simplification of medical texts and to improve accessibility for lay audiences.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Text Simplification

**Limitations**: N/A

## 💾 Data

**Source**: Cochrane Database of Systematic Reviews

**Size**: 4,459 pairs

**Format**: Plain text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human Evaluation
- Automated metrics

**Metrics**:
- Flesch-Kincaid
- Automated Readability Index (ARI)
- SARI
- BLEU
- ROUGE

**Calculation**: Metrics were calculated according to standard definitions used in readability assessments and text simplification tasks.

**Interpretation**: Lower Flesch-Kincaid and ARI scores indicate higher readability, while higher SARI and BLEU scores indicate better simplification quality.

**Baseline Results**: N/A

**Validation**: Cross-validation was employed in training the models, with results reported on test splits.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
