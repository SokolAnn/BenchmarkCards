# REASON MAP

## 📊 Benchmark Details

**Name**: REASON MAP

**Overview**: REASON MAP is a benchmark designed to evaluate the fine-grained visual understanding and spatial reasoning capabilities of MLLMs using high-resolution transit maps. It encompasses 1,008 human-verified question-answer pairs constructed over transit maps from 30 cities across 13 countries.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Hungarian
- Chinese
- Italian

**Similar Benchmarks**:
- MathVQA
- MathVerse
- VisuLogic

**Resources**:
- [Resource](https://fscdc.github.io/Reason-Map)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for assessing multimodal large language models on fine-grained visual reasoning tasks using transit maps.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Reasoning
- Question Answering

**Limitations**: The benchmark primarily focuses on high-resolution transit maps and may not generalize to other types of visual reasoning tasks.

## 💾 Data

**Source**: High-resolution transit maps from publicly available online sources covering 30 cities across 13 countries.

**Size**: 1,008 question-answer pairs

**Format**: JSON

**Annotation**: Manual annotation with human verification for correctness and quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Map Score

**Calculation**: Accuracy is evaluated based on correct route identification, while Map Score assesses the quality of the answer according to predefined criteria.

**Interpretation**: Higher accuracy scores indicate better model performance; Map Score reflects the overall quality of the response.

**Validation**: The benchmark validation involves manual route verification and evaluation against a structured two-level framework.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**

**Demographic Analysis**: The dataset includes question-answer pairs in multiple languages, enabling some analysis of multimodal fairness across demographics.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data is publicly sourced, ensuring compliance with relevant licenses without containing personal data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with relevant licenses and usage terms for public data.
