# LongLaMP (Long-text Language Model Personalization Benchmark)

## 📊 Benchmark Details

**Name**: LongLaMP (Long-text Language Model Personalization Benchmark)

**Overview**: The LongLaMP Benchmark provides a comprehensive and diverse evaluation framework for personalized long-text generation, consisting of four distinct tasks: Personalized Email Generation, Personalized Abstract Generation, Personalized Review Writing, and Personalized Topic Writing.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](http://LongLaMP-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and enhance techniques for personalized long-text generation across a variety of tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Personalized Email Writing
- Personalized Abstract Generation
- Personalized Review Writing
- Personalized Topic Writing

**Limitations**: N/A

## 💾 Data

**Source**: Various datasets including the Avocado Research Email Collection, Citation Network Dataset, Amazon Reviews Dataset, and Reddit TL;DR dataset.

**Size**: Over 50,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- ROUGE-1
- ROUGE-L
- METEOR

**Calculation**: Metrics are calculated based on the semantic similarity between generated text and the expected output.

**Interpretation**: Higher ROUGE and METEOR scores indicate better alignment with human-written examples.

**Validation**: The benchmark has been validated through extensive experiments demonstrating performance improvements in personalized generation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The Avocado Research Email Collection is managed under a confidentiality agreement to ensure user privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
