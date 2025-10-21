# Larth: Dataset and Machine Translation for Etruscan

## 📊 Benchmark Details

**Name**: Larth: Dataset and Machine Translation for Etruscan

**Overview**: We propose a dataset for machine translation from Etruscan to English, which contains 2891 translated examples from existing academic sources. This dataset can help enable future research on this language and similar low-resource languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Etruscan
- English

**Resources**:
- [GitHub Repository](https://github.com/GianlucaVico/Larth-Etruscan-NLP.git)

## 🎯 Purpose and Intended Users

**Goal**: To create a usable corpus from Etruscan inscriptions for natural language processing and evaluate neural models for translation from Etruscan to English.

**Target Audience**:
- ML Researchers
- Linguists
- NLP Practitioners

**Tasks**:
- Machine Translation

**Limitations**: The dataset is limited in size and may not contain comprehensive coverage of all Etruscan texts.

## 💾 Data

**Source**: The dataset includes Etruscan texts extracted from academic resources such as ETP, CIEP, and Zikh Rasna.

**Size**: 2,891 examples

**Format**: CSV

**Annotation**: Data is manually and automatically annotated, with translations provided for each example.

## 🔬 Methodology

**Methods**:
- Neural machine translation
- Statistical models
- Data augmentation

**Metrics**:
- BLEU
- chr-F
- TER

**Calculation**: Metrics are computed based on n-grams matching between the machine-translated and reference translations.

**Interpretation**: Higher BLEU and chr-F scores indicate better translation quality, while lower TER scores indicate fewer edits needed.

**Baseline Results**: A small transformer model achieved a BLEU score of 10.1 on the dataset.

**Validation**: The training and validation splits are created from the available examples, typically using an 80/20 split.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
