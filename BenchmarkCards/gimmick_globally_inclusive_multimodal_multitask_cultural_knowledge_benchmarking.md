# GIMMICK (Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking)

## 📊 Benchmark Details

**Name**: GIMMICK (Globally Inclusive Multimodal Multitask Cultural Knowledge Benchmarking)

**Overview**: GIMMICK is a comprehensive evaluation framework assessing 31 state-of-the-art models across six tasks built on three novel datasets, incorporating 728 unique cultural events or facets from 144 countries in six global macro-regions.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- CulturalBench
- CROPE
- CulturalVQA

**Resources**:
- [GitHub Repository](https://github.com/floschne/gimmick)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the cultural knowledge of large vision-language models across various cultural contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Cultural Studies Scholars

**Tasks**:
- Cultural Image VQA
- Cultural Video VQA
- Cultural Origin QA
- Cultural Knowledge QA

**Limitations**: English-Only Benchmark; Small Number of Samples; Open-Ended VQA measures pose evaluation challenges.

## 💾 Data

**Source**: UNESCO Intangible Cultural Heritage (ICH) project

**Size**: 7,239 samples

**Format**: JSON

**Annotation**: Manual annotation by experts from diverse cultural backgrounds.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the correctness of answers to questions about cultural knowledge, with adjustments for subjective interpretations.

**Interpretation**: Higher accuracy indicates better cultural understanding by the evaluated models, particularly in nuanced cultural knowledge.

**Validation**: Tested for reliability using annotations from trained experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark includes a demographic analysis of cultural knowledge assessment across various global regions.

**Potential Harm**: ['Cultural misrepresentation risks associated with AI models due to bias in training data.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participating annotators were trained and informed about privacy measures.

**Data Licensing**: Data derived from the UNESCO ICH project is open access; specific licensing details regarding images and videos used from these sources were not clarified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
