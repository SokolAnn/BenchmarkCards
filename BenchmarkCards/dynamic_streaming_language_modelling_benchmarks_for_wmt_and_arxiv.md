# Dynamic Streaming Language Modelling Benchmarks for WMT and ARXIV

## 📊 Benchmark Details

**Name**: Dynamic Streaming Language Modelling Benchmarks for WMT and ARXIV

**Overview**: We will publicly release our dynamic, streaming language modelling benchmarks for WMT and ARXIV to facilitate language model evaluation that takes temporal dynamics into account.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/deepmind/deepmind-research/tree/master/pitfalls_static_language_models)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate language models on their generalization ability to future data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available datasets including WMT News Crawl and arXiv abstracts.

**Size**: 395.59GB

**Format**: text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Dynamic evaluation
- Perplexity evaluation

**Metrics**:
- Perplexity
- Accuracy

**Calculation**: Perplexity is calculated based on the negative log probability of the model outputs conditional on its inputs.

**Interpretation**: Models should demonstrate lower perplexity values indicating better predictive performance.

**Validation**: Dynamic evaluation updates model parameters based on new data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
