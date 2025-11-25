# BanMANI

## 📊 Benchmark Details

**Name**: BanMANI

**Overview**: BanMANI is a dataset of social media content labeled with information manipulation relative to reference articles in the Bengali language.

**Data Type**: social media posts

**Domains**:
- Natural Language Processing

**Languages**:
- Bengali

**Similar Benchmarks**:
- MANITWEET

**Resources**:
- [GitHub Repository](https://github.com/kamruzzaman15/BanMANI)

## 🎯 Purpose and Intended Users

**Goal**: To identify whether a news-related social media item is manipulated.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Classification

**Limitations**: Due to budget constraints, a limited set of human-written social media items were collected.

## 💾 Data

**Source**: Social media posts collected from Facebook and news articles from the BanFakeNews dataset.

**Size**: 800 social media items

**Format**: N/A

**Annotation**: Annotated by human annotators following a semi-automatic method.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Exact Match
- ROUGE-L

**Calculation**: Metrics calculated based on classification and span extraction tasks.

**Interpretation**: Higher F1 scores indicate better classification performance.

**Baseline Results**: Zero-shot ChatGPT F1 score of 57.02%, fine-tuned model F1 score of 65.77%.

**Validation**: Inter-annotator agreement of 92.2% per Cohen's kappa.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
