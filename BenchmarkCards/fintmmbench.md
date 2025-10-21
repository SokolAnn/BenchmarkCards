# FinTMMBench

## 📊 Benchmark Details

**Name**: FinTMMBench

**Overview**: FinTMMBench is the first comprehensive benchmark for evaluating temporal-aware multi-modal Retrieval-Augmented Generation (RAG) systems in finance, comprising 5,676 questions spanning financial tables, news articles, daily stock prices, and visual technical charts, designed to assess a model's ability to retrieve and reason over temporal financial information.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Similar Benchmarks**:
- FinTextQA
- AlphaFin
- OmniEval
- FinanceBench

**Resources**:
- [GitHub Repository](https://github.com/lijunfeng99/FinTMMBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate temporal-aware multi-modal Retrieval-Augmented Generation (RAG) systems in finance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Information Extraction
- Trend Analysis
- Sentiment Analysis
- Event Detection

**Limitations**: N/A

## 💾 Data

**Source**: Financial data of NASDAQ-100 companies from various modalities including financial tables, news articles, daily stock prices, and visual technical charts.

**Size**: 5,676 questions and 36,100 raw data items

**Format**: JSON

**Annotation**: Automatically generated from templates with human review for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- Accuracy

**Calculation**: EM, F1 Score, and Accuracy against ground-truth answers.

**Interpretation**: Higher scores indicate better retrieval and reasoning performance.

**Baseline Results**: F1 score of 31.41 with the proposed TMMHybridRAG method.

**Validation**: Iterative process combining automatic revision and human review to ensure a verification accuracy exceeding 85%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
