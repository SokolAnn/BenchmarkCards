# MMAFFBen (Multilingual and Multimodal Affective Analysis Benchmark)

## 📊 Benchmark Details

**Name**: MMAFFBen (Multilingual and Multimodal Affective Analysis Benchmark)

**Overview**: MMAFFBen is the first extensive open-source benchmark for multilingual multimodal affective analysis, covering text, image, and video modalities across 35 languages and four core affective tasks: sentiment polarity, sentiment intensity, emotion classification, and emotion intensity.

**Data Type**: text, image, video

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Arabic
- Spanish
- Chinese

**Similar Benchmarks**:
- AEB
- XED
- MMS
- FABA
- EMOTIC

**Resources**:
- [GitHub Repository](https://github.com/lzw108/MMAFFBen)
- [Resource](https://huggingface.co/datasets/lzw1008/MMAFFBen/tree/main)
- [Resource](https://huggingface.co/datasets/lzw1008/MMAFFIn/tree/main)

## 🎯 Purpose and Intended Users

**Goal**: To foster transparent, reproducible, and inclusive progress in affective analysis studies and applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Sentiment Polarity
- Sentiment Intensity
- Emotion Classification
- Emotion Intensity

**Limitations**: Due to limitations in computational resources and cost, we only tested open-source models up to 13B in size, as well as GPT-4o-mini.

## 💾 Data

**Source**: Open-source datasets curated from prior research for LLM evaluation

**Size**: 216,568 examples

**Format**: Various formats based on the original datasets (e.g., text, images, video)

**Annotation**: Carefully curated from prior studies to adapt for LLM evaluation

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Systematic comparison of LLM capabilities

**Metrics**:
- Accuracy
- F1 Score
- Pearson Correlation Coefficient (PCC)

**Calculation**: Evaluation metrics calculated based on standardized tasks for emotion and sentiment analysis.

**Interpretation**: Higher scores indicate better performance in affective analysis tasks.

**Validation**: Framework established using open-source datasets with careful curation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: Includes analysis across various languages and modalities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Carefully curated data to minimize personal information exposure.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
