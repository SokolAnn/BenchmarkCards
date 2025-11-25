# Development of a Dataset and a Deep Learning Baseline Named Entity Recognizer for Three Low Resource Languages: Bhojpuri, Maithili and Magahi

## 📊 Benchmark Details

**Name**: Development of a Dataset and a Deep Learning Baseline Named Entity Recognizer for Three Low Resource Languages: Bhojpuri, Maithili and Magahi

**Overview**: This paper focuses on the development of a Named Entity Recognition (NER) benchmark dataset for Bhojpuri, Maithili and Magahi, which are low resource languages. The dataset was annotated using 22 entity labels and is aimed at improving machine translation systems.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bhojpuri
- Maithili
- Magahi

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop an NER dataset for Bhojpuri, Maithili and Magahi languages to improve machine translation systems from these languages to Hindi.

**Target Audience**:
- NLP Researchers
- Machine Translation Developers

**Tasks**:
- Named Entity Recognition
- Machine Translation

**Limitations**: N/A

## 💾 Data

**Source**: Annotated corpora from Bhojpuri, Maithili, and Magahi languages

**Size**: 228,373 tokens for Bhojpuri, 157,468 tokens for Maithili, 56,190 tokens for Magahi

**Format**: N/A

**Annotation**: Annotated using a defined entity tagset and guidelines applicable for Indian languages.

## 🔬 Methodology

**Methods**:
- Conditional Random Fields (CRF)
- LSTM-CNNs-CRF

**Metrics**:
- F1 Score

**Calculation**: F1 scores were calculated based on entity recognition results from the NER tools.

**Interpretation**: Higher F1 scores indicate better performance of the NER tools.

**Baseline Results**: CRF: Bhojpuri 70.56%, Maithili 73.19%, Magahi 84.18%; LSTM-CNNs-CRF: Bhojpuri 61.41%, Maithili 71.38%, Magahi 86.39%.

**Validation**: The results were validated based on training and testing datasets split with a ratio of 80-20.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
