# edgar -corpus

## 📊 Benchmark Details

**Name**: edgar -corpus

**Overview**: edgar -corpus is the largest financial NLP corpus available, comprising annual reports from all publicly traded companies in the US, spanning a period of more than 25 years, provided in an easy-to-use JSON format.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://zenodo.org/record/5528490)
- [GitHub Repository](https://github.com/nlpaueb/edgar-crawler)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive financial NLP corpus that facilitates research in financial text analysis.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Limitations**: N/A

## 💾 Data

**Source**: Annual reports (10-K filings) from all publicly traded companies in the US collected via web crawling.

**Size**: 6.5B tokens

**Format**: JSON

**Annotation**: Manual extraction of sections from annual reports.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Mean Squared Error (MSE)

**Calculation**: Standard metrics such as Accuracy, F1 Score, and MSE were used to evaluate the performance in financial NLP tasks.

**Interpretation**: Better performance indicates better embeddings for financial NLP tasks.

**Baseline Results**: edgar -w2v outperforms generic glove embeddings and other financial embeddings.

**Validation**: 10-fold cross-validation was used for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
