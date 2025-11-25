# American Stories (Structured text dataset of Historical U.S. Newspapers)

## 📊 Benchmark Details

**Name**: American Stories (Structured text dataset of Historical U.S. Newspapers)

**Overview**: The American Stories dataset provides high-quality structured article texts extracted from nearly 20 million newspaper scans in the Library of Congress’s Chronicling America project, addressing limitations of existing datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Social Science
- Digital Humanities

**Languages**:
- English

**Similar Benchmarks**:
- Newspaper Navigator

**Resources**:
- [Resource](https://huggingface.co/datasets/dell-research-harvard/AmericanStories)
- [GitHub Repository](https://github.com/dell-research-harvard/AmericanStories)

## 🎯 Purpose and Intended Users

**Goal**: To provide researchers with a high-quality corpus of structured and transcribed newspaper article texts from historical U.S. newspapers.

**Target Audience**:
- Researchers
- Historians
- Social Scientists
- NLP Practitioners

**Tasks**:
- Topic Classification
- Content Analysis
- Language Modeling

**Limitations**: The dataset contains historical language reflecting the cultural biases of the time.

**Out of Scope Uses**:
- Training generative models without filtering due to potential toxicity.

## 💾 Data

**Source**: Library of Congress’s Chronicling America project.

**Size**: 1.14 billion content regions

**Format**: JSON

**Annotation**: Automated via a deep learning pipeline with layout detection and OCR techniques.

## 🔬 Methodology

**Methods**:
- Layout Detection
- Optical Character Recognition (OCR)
- Article Association

**Metrics**:
- Character Error Rate (CER)
- Mean Average Precision (mAP)

**Calculation**: Metrics are evaluated based on comparison to ground truth annotations in dedicated validation datasets.

**Interpretation**: A lower CER indicates higher OCR accuracy.

**Baseline Results**: CER of 0.051 (0.044 after spellchecking) and mAP for article bounding boxes at 91.31.

**Validation**: Evaluated using labeled datasets and inter-annotator reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: Potential to analyze societal biases reflected in historical texts.

**Potential Harm**: Historical biases may reinforce stereotypes or cultural misconceptions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is derived from publicly available historical newspapers.

**Data Licensing**: Creative Commons CC-BY license.

**Consent Procedures**: N/A - Data is in the public domain.

**Compliance With Regulations**: N/A - Data is drawn from public domain sources.
