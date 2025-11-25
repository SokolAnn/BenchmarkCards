# DZEN (Dzongkha-English Benchmark)

## 📊 Benchmark Details

**Name**: DZEN (Dzongkha-English Benchmark)

**Overview**: DZEN is a dataset of parallel Dzongkha and English test questions covering over 5K scientific questions from Bhutan's national curriculum for middle and high school exams. It allows for direct LLM performance comparison and exposes structural weaknesses in low-resource language proficiency.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Dzongkha
- English

**Similar Benchmarks**:
- MMLU
- IndoMMLU

**Resources**:
- [GitHub Repository](https://github.com/kraritt/llm_dzongkha_evaluation)

## 🎯 Purpose and Intended Users

**Goal**: To assess the performance of large language models (LLMs) in Dzongkha and enhance their proficiency through a benchmarking dataset.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset primarily consists of text-based questions, omitting figure-based questions which may require more complex reasoning.

## 💾 Data

**Source**: Dataset of parallel questions was created from Bhutan's national curriculum and national board examinations, ensuring bilingual availability in Dzongkha and English.

**Size**: 5,161 questions

**Format**: JSON

**Annotation**: Digitized and verified by proficient typists in Dzongkha and English, with parallelism checks conducted by native speakers.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Model outputs were compared against ground truth answers from the dataset to determine correctness based on accuracy of final answers.

**Interpretation**: An answer is deemed correct if it matches the ground truth, regardless of the correctness of intermediate reasoning steps.

**Validation**: Results were validated through manual examination and statistical analysis of model performance across various subjects.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark allows for cross-linguistic analysis, exposing performance gaps across different demographics, particularly in low-resource settings.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
