# BeliN (Bengali Religious News)

## 📊 Benchmark Details

**Name**: BeliN (Bengali Religious News)

**Overview**: The BeliN corpus is a novel dataset focused on Bengali religious news, comprising 2,520 articles and their corresponding headlines, aimed at enhancing headline generation by incorporating contextual features such as category, aspect, and sentiment.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Similar Benchmarks**:
- Shironaam

**Resources**:
- [GitHub Repository](https://github.com/akabircs/BeliN)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for improving Bengali religious news headline generation through a multi-input approach incorporating contextual features.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Headline Generation
- Text Summarization
- Sentiment Analysis
- Aspect Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from prominent Bangladeshi online newspapers and religious news portals.

**Size**: 2,520 articles

**Format**: N/A

**Annotation**: Manually annotated for categories, aspects, and sentiment.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERTScore
- METEOR

**Calculation**: Metrics are calculated based on n-gram overlap and similarity to reference outputs.

**Interpretation**: Higher scores indicate better fluency and relevance of generated headlines.

**Baseline Results**: Baseline models include prior systems that utilized content-only input.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of religious sentiment across diverse categories.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
