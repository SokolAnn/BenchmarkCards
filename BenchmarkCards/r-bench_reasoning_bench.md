# R-Bench (Reasoning Bench)

## 📊 Benchmark Details

**Name**: R-Bench (Reasoning Bench)

**Overview**: R-Bench is a graduate-level, multi-disciplinary, multilingual benchmark designed to evaluate complex reasoning capabilities for both language and multimodal models, spanning 1,094 questions across 108 subjects for language model evaluation and 665 questions across 83 subjects for multimodal model testing.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMLU
- MMMU

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To build a reliable complex reasoning benchmark for both large language models (LLMs) and multimodal large language models (MLLMs).

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Complex Reasoning Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Questions curated from graduate college courses across 19 departments at Tsinghua University.

**Size**: 10,270 questions

**Format**: Excel sheets

**Annotation**: Expert-reviewed and digitized with automated verification.

## 🔬 Methodology

**Methods**:
- Expert evaluation
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is measured based on the performance of models on the R-Bench questions.

**Interpretation**: A higher score indicates better reasoning capability of models. R-Bench challenges current models more effectively compared to existing benchmarks.

**Baseline Results**: OpenAI o1 achieved 69.0% accuracy on R-Bench-T and 53.2% on R-Bench-M.

**Validation**: R-Bench was validated through expert scoring and model scoring comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
