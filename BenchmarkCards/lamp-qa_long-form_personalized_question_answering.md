# LaMP-QA (Long-form Personalized Question Answering)

## 📊 Benchmark Details

**Name**: LaMP-QA (Long-form Personalized Question Answering)

**Overview**: The LaMP-QA benchmark is designed for evaluating personalized question answering in three diverse domains: Art & Entertainment, Lifestyle & Personal Development, and Society & Culture. It captures user-specific preferences and expectations for a more accurate and satisfying response.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LaMP

**Resources**:
- [Resource](https://arxiv.org/abs/2506.00137)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of personalized question answering systems by providing a dataset that includes user context and expectations.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The LaMP-QA benchmark

**Size**: 2,830 questions

**Format**: JSON

**Annotation**: Expert annotations based on user queries and personalized rubrics.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on the extent to which generated responses match user expectations as specified in user context.

**Interpretation**: Higher scores indicate better alignment between generated responses and user-specific needs.

**Validation**: Evaluated through comparative analysis against established baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User profiles are anonymized to respect user privacy during data collection and analysis.

**Data Licensing**: Not Applicable

**Consent Procedures**: Explicit consent obtained from users for data usage in research.

**Compliance With Regulations**: Not Applicable
