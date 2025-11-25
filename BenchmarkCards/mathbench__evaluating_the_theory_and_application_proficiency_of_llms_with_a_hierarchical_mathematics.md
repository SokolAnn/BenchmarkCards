# MathBench: Evaluating the Theory and Application Proficiency of LLMs with a Hierarchical Mathematics Benchmark

## 📊 Benchmark Details

**Name**: MathBench: Evaluating the Theory and Application Proficiency of LLMs with a Hierarchical Mathematics Benchmark

**Overview**: MathBench is a new benchmark that rigorously assesses the mathematical capabilities of large language models across various mathematical disciplines, providing a detailed evaluation of both theoretical understanding and practical problem-solving skills.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GSM8k
- MathQA
- MATH

**Resources**:
- [GitHub Repository](https://github.com/open-compass/MathBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLMs’ mathematical proficiency, covering a wide range of subject areas and topics across educational stages.

**Target Audience**:
- ML Researchers
- Educators
- AI Developers

**Tasks**:
- Mathematical Reasoning
- Problem Solving
- Question Answering

**Limitations**: The current benchmark may be subject to data contamination and lacks detailed reasoning paths for each question.

## 💾 Data

**Source**: Self-collected from a variety of educational materials and open-source datasets.

**Size**: 3,709 questions

**Format**: JSON

**Annotation**: Semi-automated vetting process with manual reviews to ensure quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of models across different stages and types of questions in the benchmark.

**Interpretation**: Higher scores indicate better mathematical understanding and problem-solving capabilities in language models.

**Validation**: Validation of model performance conducted through Circular Evaluation (CE) and Perplexity (PPL) metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Assessment of performance across different languages (Chinese and English) and educational stages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures included the avoidance of personally identifiable information during data collection and processing.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
