# Referencing Evaluation for Long-context Language Models (Ref-Long)

## 📊 Benchmark Details

**Name**: Referencing Evaluation for Long-context Language Models (Ref-Long)

**Overview**: Ref-Long is a novel benchmark designed to assess the long-context referencing capability of Long-context Language Models (LCLMs). It requires LCLMs to identify document indexes that reference a specific key within long-context data, emphasizing contextual relationships over simple retrieval.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Long-Bench
- L-Eval
- NOCHA
- Needle-in-a-Haystack
- Counting-stars
- RULER

**Resources**:
- [GitHub Repository](https://github.com/wujunjie1998/Ref-Long)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LCLMs' long-context referencing capabilities and to highlight challenges faced by these models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Retrieval
- Information Extraction

**Limitations**: Existing findings are based on a limited set of LCLMs and may not generalize across all long-context scenarios.

## 💾 Data

**Source**: Constructed from synthetic datasets and realistic scenarios, including specific citation tasks from arXiv papers.

**Size**: 1,800 tasks for Ref-Long-A, 2,100 tasks for Ref-Long-F, and 100 tasks for Ref-Long-Paper

**Format**: JSON

**Annotation**: Tasks require LCLMs to identify document indexes that reference specified keys.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match Accuracy (Ex Acc)
- F1 Score

**Calculation**: Metrics are calculated based on the exactness of the document indexes identified by LCLMs against the ground truth.

**Interpretation**: Higher scores in both metrics indicate better performance in referencing tasks.

**Validation**: Experimental results were validated through comprehensive analyses, including human evaluations and error analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
