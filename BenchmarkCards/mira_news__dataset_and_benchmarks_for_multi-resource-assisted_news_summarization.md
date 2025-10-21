# MIRA NEWS: Dataset and Benchmarks for Multi-Resource-Assisted News Summarization

## 📊 Benchmark Details

**Name**: MIRA NEWS: Dataset and Benchmarks for Multi-Resource-Assisted News Summarization

**Overview**: MIRA NEWS introduces a new task, Multi-Resource-Assisted News summarization, along with a novel dataset that collects multiple assisting news articles to mitigate extrinsic hallucinations in single-document summarization.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/XinnuoXu/MiRANews)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and benchmark for evaluating the effectiveness of multi-resource-assisted news summarization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Collected from newser.com, which aggregates news articles with assisting documents.

**Size**: 150,000 examples

**Format**: N/A

**Annotation**: Automatically collected and structured data from news articles.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- ROUGE
- BertScore
- SFweights

**Calculation**: Metrics are calculated based on generated summaries compared to ground truth summaries, and the presence of extrinsic facts is assessed using SFweights.

**Interpretation**: Higher ROUGE scores indicate better alignment with human-authored summaries, while SFweights scores indicate lower levels of extrinsic hallucinations.

**Baseline Results**: BART and HT models with various configurations show varying performance on benchmark tasks.

**Validation**: Performance evaluated by comparing to baseline results and human-authored summaries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Hallucination

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
