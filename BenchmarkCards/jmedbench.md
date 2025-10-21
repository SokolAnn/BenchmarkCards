# JMedBench

## 📊 Benchmark Details

**Name**: JMedBench

**Overview**: We propose a new benchmark including eight LLMs across four categories and 20 Japanese biomedical datasets across five tasks to evaluate Japanese biomedical language models.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Japanese

**Similar Benchmarks**:
- BLURB
- MMLU
- JMMLU
- DrBenchmark
- MMedBench

**Resources**:
- [Resource](https://huggingface.co/datasets/Coldog2333/JMedBench)

## 🎯 Purpose and Intended Users

**Goal**: To construct a benchmark for evaluating Japanese biomedical LLMs.

**Target Audience**:
- ML Researchers
- Biomedical Researchers
- Model Developers

**Tasks**:
- Multi-Choice Question Answering
- Named Entity Recognition
- Machine Translation
- Document Classification
- Semantic Text Similarity

**Limitations**: Due to budget limitations, we only translated several datasets of MCQA and NER and evaluated models with 7B/8B parameters.

## 💾 Data

**Source**: 20 Japanese biomedical datasets including translations from English and original datasets.

**Size**: 38,130 samples

**Format**: JSON

**Annotation**: Translations by Machine Translation and manual adjustments for dataset quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- Pearson Correlation

**Calculation**: Calculated based on the results from various prompt templates across multiple runs.

**Interpretation**: Higher scores indicate better performance in the respective tasks.

**Baseline Results**: Varied model performances across tasks reported in tables.

**Validation**: Extensive validation through multiple prompt templates and evaluation metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misinterpretation of medical terms due to translation inaccuracies.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets mainly adhere to MIT or CC-BY-4.0 licenses, with specific datasets under non-commercial licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
