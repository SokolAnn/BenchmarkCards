# RoMath: A Mathematical Reasoning Benchmark in Romanian

## 📊 Benchmark Details

**Name**: RoMath: A Mathematical Reasoning Benchmark in Romanian

**Overview**: RoMath is a Romanian mathematical reasoning benchmark suite comprising three subsets: Baccalaureate, Competitions, and Synthetic, covering a range of mathematical domains and difficulty levels, aiming to improve non-English language models and promote multilingual AI development.

**Data Type**: mathematical problem statements

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Similar Benchmarks**:
- MATH
- GSM8k

**Resources**:
- [GitHub Repository](https://github.com/cosmaadrian/romath)
- [Resource](https://huggingface.co/datasets/cosmadrian/romath)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark suite for mathematical reasoning in Romanian and to stimulate the development of non-English language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available PDFs from country-wide mathematics competitions and questions from the Romanian baccalaureate exam.

**Size**: 76,910 problem statements

**Format**: JSON

**Annotation**: Semi-automatically annotated using foundational LLMs for structured output.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: For verifiable problems, correctness is checked through direct string comparison after solution normalization; for proof problems, an LLM-as-a-judge is employed.

**Interpretation**: Accuracy and F1 Score indicate the performance of language models on mathematical reasoning tasks.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through performance testing of various open-weight language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
