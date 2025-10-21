# Qbias - A Dataset on Media Bias in Search Queries and Query Suggestions

## 📊 Benchmark Details

**Name**: Qbias - A Dataset on Media Bias in Search Queries and Query Suggestions

**Overview**: Qbias is a large dataset of Google and Bing search queries, a scraping tool and dataset for biased news articles, as well as language models for the investigation of bias in online search.

**Data Type**: search query suggestions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/irgroup/Qbias)
- [Resource](https://doi.org/10.5281/zenodo.7682914)

## 🎯 Purpose and Intended Users

**Goal**: To provide datasets and language models for bias research in online information search.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Bias Detection
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Search queries and articles from Google, Bing, and AllSides

**Size**: 671,669 search query suggestions; 21,747 news articles

**Format**: CSV

**Annotation**: Manual annotation by experts for bias labeling

## 🔬 Methodology

**Methods**:
- Data Scraping
- Manual Evaluation
- Fine-tuning Transformer models

**Metrics**:
- Rank Biased Overlap (RBO)
- Cohen’s Kappa for inter-annotator agreement

**Calculation**: Performance evaluated on the difference in predictions between left and right biased models.

**Interpretation**: Lower RBO scores indicate better model differentiation between political stances.

**Validation**: Models validated through manual assessment and quantitative measures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Misuse**: Non-disclosure, Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: ['Risk of reproducing biased and harmful language outputs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
