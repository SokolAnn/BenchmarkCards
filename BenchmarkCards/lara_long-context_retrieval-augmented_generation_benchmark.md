# LaRA (Long-context Retrieval-Augmented Generation Benchmark)

## 📊 Benchmark Details

**Name**: LaRA (Long-context Retrieval-Augmented Generation Benchmark)

**Overview**: LaRA is a novel benchmark specifically designed to rigorously compare Retrieval-Augmented Generation (RAG) and Long-Context (LC) Large Language Models (LLMs), encompassing 2326 test cases across four practical QA task categories and three types of naturally occurring long texts.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ZeroSCROLLS
- LongBench
- BAMBOO
- Loong
- ∞-bench

**Resources**:
- [GitHub Repository](https://github.com/Alibaba-NLP/LaRA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for comparing Retrieval-Augmented Generation and Long-Context models, leading to actionable guidelines for practitioners.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: LaRA dataset and test cases created for the benchmark.

**Size**: 2,326 test cases

**Format**: N/A

**Annotation**: QA pairs constructed using a combination of human annotation and LLM-assisted generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Evaluation of model performance based on defined metrics using both automated and human evaluations.

**Interpretation**: Accuracy measurements reflect how well models perform on tasks within the LaRA benchmark.

**Validation**: Cohen’s Kappa coefficient computed to assess consistency between LLM and human evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack, Prompt injection attack
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
