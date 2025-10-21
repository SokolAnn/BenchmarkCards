# Southern Newswire Corpus: A Large-Scale Dataset of Mid-Century Wire Articles Beyond the Front Page

## 📊 Benchmark Details

**Name**: Southern Newswire Corpus: A Large-Scale Dataset of Mid-Century Wire Articles Beyond the Front Page

**Overview**: I introduce a new large-scale dataset of historical wire articles from U.S. Southern newspapers, spanning 1960–1975 and covering multiple wire services, providing a detailed perspective on how Southern newspapers relayed national and international news.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Digital Humanities
- Computational Social Science

**Languages**:
- English

**Similar Benchmarks**:
- Newswire
- Headlines

**Resources**:
- [Resource](https://mike-mcrae.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a detailed perspective on how wire news was transmitted and transformed in the American South during a period of profound social and political change.

**Target Audience**:
- Scholars
- Researchers
- Computational Linguists
- Digital Humanists

**Tasks**:
- Named Entity Recognition
- Topic Modeling
- Quantitative Text Analysis

**Limitations**: Some newspapers or date ranges remain undigitised. OCR artefacts may persist despite corrections. Historical biases in language have been preserved for authenticity.

## 💾 Data

**Source**: Historical wire articles extracted from approximately 10 million digitised pages published in Southern newspapers from 1960 to 1975.

**Size**: 57,547,723 articles

**Format**: text

**Annotation**: Automated classification using fine-tuned BERT models to identify wire service origins.

## 🔬 Methodology

**Methods**:
- Layout detection
- Optical Character Recognition (OCR)
- De-duplication
- LLM-based text correction

**Metrics**:
- F1 Score

**Calculation**: F1 Score calculated on the performance of classifiers trained to detect wire service origins.

**Interpretation**: High F1 Score indicates the effectiveness of the classifiers in identifying articles by wire services.

**Baseline Results**: F1-scores: AP model – 0.9925, UPI – 0.9999, NEA – 0.9876

**Validation**: The methodology has been validated through a process of testing classifiers on a labeled dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The dataset will be lawfully distributable under a permissive license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
