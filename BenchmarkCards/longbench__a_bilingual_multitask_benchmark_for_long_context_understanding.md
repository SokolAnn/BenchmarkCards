# LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

## 📊 Benchmark Details

**Name**: LongBench: A Bilingual, Multitask Benchmark for Long Context Understanding

**Overview**: LongBench, the first bilingual, multi-task benchmark for long context understanding, enables rigorous evaluation of long context capabilities of large language models. It comprises 21 datasets across 6 task categories in English and Chinese, focusing on key long-text application areas such as QA, summarization, and code completion.

**Data Type**: question-answering pairs, summaries, code completion tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- ZeroSCROLLS
- L-Eval
- AgentBench

**Resources**:
- [GitHub Repository](https://github.com/THUDM/LongBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that evaluates long context understanding of large language models across different languages and task types.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Single-Document Question Answering
- Multi-Document Question Answering
- Summarization
- Few-shot Learning
- Synthetic Tasks
- Code Completion

**Limitations**: N/A

## 💾 Data

**Source**: Composed of 21 datasets from various sources including NarrativeQA, HotpotQA, GovReport, DuReader, and more, specifically adapted for long context evaluation.

**Size**: 4,750 test instances

**Format**: N/A

**Annotation**: Datasets captured from original studies, with some datasets manually annotated by experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation through LLMs

**Metrics**:
- F1 Score
- ROUGE-L

**Calculation**: Metrics were calculated based on the similarity of model outputs to groundtruth.

**Interpretation**: Higher scores indicate better long context understanding capability of the models.

**Validation**: The benchmark was validated through comprehensive evaluation across different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
