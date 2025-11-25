# BioASR-NER

## 📊 Benchmark Details

**Name**: BioASR-NER

**Overview**: This paper introduces a dataset, BioASR-NER, designed to bridge the ASR-NLP gap in the biomedical domain, focusing on extracting adverse drug reactions and mentions of entities from the Brief Test of Adult Cognition by Telephone (BTACT) exam. The dataset comprises almost 2,000 clean and noisy recordings.

**Data Type**: audio-transcription pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://zenodo.org/records/10864063)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for biomedical NLP researchers to improve and explore the biomedical ASR-NLP gap.

**Target Audience**:
- ML Researchers
- Healthcare Professionals

**Tasks**:
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is built from CADEC (Karimi et al., 2015) and a Synthetic BTACT dataset created by the authors.

**Size**: 2,000 recordings

**Format**: Audio files

**Annotation**: Annotated based on named entities including adverse drug reactions, fruits, and animals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics are calculated by evaluating the named entities detected against the ground truth in the transcripts.

**Interpretation**: Higher F1 Score indicates better performance in identifying biomedical entities from noisy transcripts.

**Validation**: The effectiveness of noise reduction methods was validated by comparing model performance on original and noisy transcripts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
