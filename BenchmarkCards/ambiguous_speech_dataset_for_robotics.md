# Ambiguous Speech Dataset for Robotics

## 📊 Benchmark Details

**Name**: Ambiguous Speech Dataset for Robotics

**Overview**: We present the first ambiguous speech dataset for robotics, designed to advance research in speech disambiguation, consisting of 1,540 ambiguous utterances.

**Data Type**: speech instructions

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To improve the understanding and execution of ambiguous spoken language instructions by robots through the use of prosodic features.

**Target Audience**:
- ML Researchers
- Robotics Developers

**Tasks**:
- Speech Disambiguation

**Limitations**: The dataset is limited in size (1,540 samples) and participant diversity, which may affect generalizability.

## 💾 Data

**Source**: Collected from 22 participants recording ambiguous instructions.

**Size**: 1,540 utterances

**Format**: audio recordings

**Annotation**: Manually annotated by participants for referent intents.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated comparing predicted intent labels against the ground truth labels.

**Interpretation**: Higher accuracy indicates better disambiguation of ambiguous speech instructions.

**Validation**: Training and evaluation sets are split to ensure no overlap between training and testing data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset primarily includes participants aged 18–22, which may limit findings to this age group.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
