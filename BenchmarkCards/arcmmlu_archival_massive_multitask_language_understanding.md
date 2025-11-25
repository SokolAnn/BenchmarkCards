# ArcMMLU (Archival Massive Multitask Language Understanding)

## 📊 Benchmark Details

**Name**: ArcMMLU (Archival Massive Multitask Language Understanding)

**Overview**: ArcMMLU is a specialized benchmark tailored for the Library & Information Science (LIS) domain in Chinese, aimed at measuring the knowledge and reasoning capability of large language models (LLMs) across four key sub-domains: Archival Science, Data Science, Library Science, and Information Science.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- MMLU
- CMMLU

**Resources**:
- [GitHub Repository](https://github.com/stzhang-patrick/ArcMMLU)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive LLM evaluation benchmark specifically designed for the Chinese Library & Information Science (LIS) domain.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark is built from real-world questions of past postgraduate entrance exams, professional exams, course quizzes, and academic competitions.

**Size**: 6,210 questions

**Format**: N/A

**Annotation**: Manual annotation with quality checks and filtering

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated as the proportion of correct answers out of the total questions.

**Interpretation**: Higher accuracy indicates better performance of LLMs on the benchmark.

**Baseline Results**: Randomly initialized models have a baseline performance of around 25%.

**Validation**: The benchmark was validated through extensive evaluations of mainstream LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
