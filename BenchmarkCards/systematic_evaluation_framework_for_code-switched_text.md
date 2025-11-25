# Systematic Evaluation Framework for Code-Switched Text

## 📊 Benchmark Details

**Name**: Systematic Evaluation Framework for Code-Switched Text

**Overview**: This paper presents a systematic evaluation framework that generates linguistically grounded code-switched variants of established benchmarks in reading comprehension, multi-domain knowledge, and natural language inference to assess the performance of Large Language Models (LLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- German
- French
- Chinese

**Similar Benchmarks**:
- MMLU
- Belebele
- XNLI

**Resources**:
- [GitHub Repository](https://github.com/amr-mohamedd/Lost-in-the-Mix.git)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM comprehension under code-switching and to fill gaps in assessing deeper reasoning and semantic understanding in mixed-language settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Reading Comprehension
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Generated code-switched variants of existing benchmarks

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Weighted Average Accuracy

**Calculation**: Accuracy is defined as a function of the number of correct predictions over total predictions on the benchmark dataset.

**Interpretation**: Positive accuracy delta indicates improvement under code-switching; lower accuracy indicates processing challenges.

**Baseline Results**: N/A

**Validation**: Evaluation utilizes a set of benchmark tasks adapted to include code-switching.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
