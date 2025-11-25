# MiLiC-Eval

## 📊 Benchmark Details

**Name**: MiLiC-Eval

**Overview**: MiLiC-Eval is a benchmark designed for minority languages in China, featuring 24K instances across 9 tasks to systematically track the progress of large language models on these underrepresented languages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Tibetan
- Uyghur
- Kazakh
- Mongolian

**Resources**:
- [GitHub Repository](https://github.com/luciusssss/MiLiC-Eval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive framework for benchmarking the performance of LLMs on low-resource languages, focusing on multilingual LLMs for minority languages in China.

**Target Audience**:
- NLP Researchers
- Language Model Developers
- Benchmark Developers

**Tasks**:
- Vocabulary Understanding
- Topic Classification
- Reading Comprehension
- Response Selection
- Title Generation
- Machine Translation
- Math Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from translations of data in high-resource languages and original texts in minority languages.

**Size**: 24,000 instances

**Format**: N/A

**Annotation**: Translated by native speakers and verified by other annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- ROUGE-L
- chrF++

**Calculation**: Metrics are computed based on the model's output compared to the ground truth in each task.

**Interpretation**: Scores indicate the model's performance relative to best practices in LRL adaptation and evaluation tasks.

**Validation**: The benchmark uses a systematic task setup for evaluating LLM performance across a range of abilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The benchmark includes evaluations across different scripts and minority populations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
