# DIVERSE SUMM

## 📊 Benchmark Details

**Name**: DIVERSE SUMM

**Overview**: DIVERSE SUMM is a dataset for multi-document summarization focusing on capturing diverse information across multiple news articles about the same event, consisting of question-answer pairs validated by human annotators.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MULTI NEWS
- DUC
- TAC

**Resources**:
- [GitHub Repository](https://github.com/salesforce/DiverseSumm)

## 🎯 Purpose and Intended Users

**Goal**: To advance the evaluation of models on diverse multi-document summarization tasks through a richly structured dataset.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-document Summarization

**Limitations**: Despite efforts to curate a large dataset, it remains a small fraction of all available news content.

## 💾 Data

**Source**: News stories collected from Google News, comprising multiple articles per story.

**Size**: 245 news stories with 10 articles each

**Format**: JSON

**Annotation**: Validated by human annotators through a structured question-answering method.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Coverage

**Calculation**: Metrics are calculated based on human judgment in terms of faithfulness and coverage of generated summaries.

**Interpretation**: High scores indicate better alignment with diverse information from all involved articles.

**Validation**: Human evaluations conducted to ensure high-quality annotations and accurate evaluations of generated summaries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset aims to capture a variety of perspectives, but demographic breakdowns are not explicitly defined.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Measures are taken to ensure the anonymity of data annotation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants allowed to withdraw from the project at any time without repercussions.

**Compliance With Regulations**: Complies with ethical standards for data annotation.
