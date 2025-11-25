# GREEK BARBENCH

## 📊 Benchmark Details

**Name**: GREEK BARBENCH

**Overview**: GREEK BARBENCH is a benchmark that evaluates LLMs on legal questions across five different legal areas from the Greek Bar exams, requiring citations to statutory articles and case facts. It features a three-dimensional scoring system combined with an LLM-as-a-judge approach.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- Greek

**Similar Benchmarks**:
- LexGLUE
- LEXTREME
- LegalBench

**Resources**:
- [Resource](https://huggingface.co/datasets/AUEB-NLP/greek-bar-bench)
- [GitHub Repository](https://github.com/nlpaueb/greek-bar-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the reasoning capabilities of LLMs on challenging legal questions.

**Target Audience**:
- Legal Professionals
- NLP Researchers
- Model Developers

**Tasks**:
- Legal Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Greek Bar exam papers.

**Size**: 310 examples

**Format**: JSON

**Annotation**: Manually annotated by legal experts.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge evaluation
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Scores are calculated based on three dimensions: Facts, Cited Articles, and Analysis.

**Interpretation**: Higher scores reflect better answers in terms of identifying facts, citing legal articles, and providing a legal analysis.

**Baseline Results**: Top models outperform average expert performance but fall short of the 95th percentile of experts.

**Validation**: Systematic evaluation of LLM judges against human expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
