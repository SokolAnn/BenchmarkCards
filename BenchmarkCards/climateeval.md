# ClimateEval

## 📊 Benchmark Details

**Name**: ClimateEval

**Overview**: ClimateEval is a comprehensive benchmark designed to evaluate natural language processing models across a broad range of tasks related to climate change, aggregating existing datasets along with a newly developed news classification dataset.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ClimaBench

**Resources**:
- [GitHub Repository](https://github.com/NLP-RISE/ClimateEval)
- [Resource](https://huggingface.co/datasets/NLP-RISE/guardian_climate_news_corpus)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate NLP research by providing an accessible setup enabling comprehensive assessment of LLMs in climate change-related applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text Classification
- Question Answering
- Information Extraction

**Limitations**: Limited to English, which restricts applicability to multilingual climate discourse.

## 💾 Data

**Source**: ClimateEval benchmark comprises 25 tasks based on 13 datasets, including a new dataset called Guardian Climate News Corpus.

**Size**: 40,173 articles

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated per task, including accuracy and macro-averaged F1 for classification tasks, and entity recognition metrics for NER tasks.

**Interpretation**: Macro F1 averages scores across all classes equally to ensure a balanced assessment.

**Validation**: The benchmark allows for efficient and standardized evaluation across diverse models and tasks implemented using the LM Evaluation Harness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
