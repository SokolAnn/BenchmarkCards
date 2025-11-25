# OrangeSum

## 📊 Benchmark Details

**Name**: OrangeSum

**Overview**: OrangeSum is a novel French summarization dataset, designed to address the lack of generative tasks in the existing FLUE benchmark, enabling the evaluation of summarization models for the French language.

**Data Type**: summarization pairs

**Domains**:
- Natural Language Processing

**Languages**:
- French

**Similar Benchmarks**:
- XSum

**Resources**:
- [GitHub Repository](https://github.com/Tixierae/OrangeSum)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for evaluating abstractive summarization models for the French language.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Scraped articles from the Orange Actu website, featuring titles and abstracts for summarization tasks.

**Size**: 6,000 examples

**Format**: CSV

**Annotation**: Manual extraction from the scraped articles

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- BERTScore

**Calculation**: Metrics calculated based on n-gram overlap and contextual similarity for summarization text.

**Interpretation**: Higher ROUGE scores indicate better alignment between generated summaries and gold references.

**Baseline Results**: Performance comparisons against XSum and BART-based models.

**Validation**: Model performance is validated through quantitative metrics and human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
