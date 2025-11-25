# PRIME: A Dataset for Long-Context Personalization

## 📊 Benchmark Details

**Name**: PRIME: A Dataset for Long-Context Personalization

**Overview**: This paper introduces a new dataset derived from the Change My View (CMV) Reddit forum, designed to evaluate long-context personalization in large language models (LLMs).

**Data Type**: ranking-based recommendation pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LaMP

**Resources**:
- [GitHub Repository](https://github.com/launchnlp/LM_Personalization)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation benchmark for assessing personalization capabilities in large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification
- Ranking

**Limitations**: The introduced benchmark cannot comprehensively represent the entire spectrum of personalization tasks.

## 💾 Data

**Source**: Change My View Reddit forum

**Size**: 133 queries with 7,514 historical interactions

**Format**: JSON

**Annotation**: Automatically generated from historical engagement data

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Hit@1
- Hit@3
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated based on the ranking of responses to original posts.

**Interpretation**: Higher scores indicate better personalization and alignment with user preferences.

**Baseline Results**: The baseline performance is compared against existing models to validate the effectiveness of the PRIME framework.

**Validation**: Extensive experiments validated the dataset across multiple model architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Data poisoning
- **Privacy**: Personal information in data

**Demographic Analysis**: The benchmark analyzes personalization across user backgrounds.

**Potential Harm**: ['Potential exacerbation of biases in personalization', 'Data misuse if user histories are improperly managed']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: User data is anonymized to protect privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
