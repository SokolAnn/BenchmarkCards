# BENCH HUB (A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation)

## 📊 Benchmark Details

**Name**: BENCH HUB (A Unified Benchmark Suite for Holistic and Customizable LLM Evaluation)

**Overview**: BENCH HUB is a dynamic benchmark repository that empowers researchers and developers to evaluate LLMs more effectively by aggregating and automatically classifying benchmark datasets from diverse domains, covering a total of 303K questions from 38 benchmarks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Korean

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- MixEval
- Chatbot Arena

**Resources**:
- [Resource](https://huggingface.co/BenchHub)
- [GitHub Repository](https://github.com/rladmstn1714/BenchHub)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified benchmark suite for holistic and customizable evaluation of large language models across multiple domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Knowledge Retrieval
- Reasoning

**Limitations**: Incomplete English Dataset Coverage: Due to the vast amount of English-language data, not all relevant datasets could be included.

## 💾 Data

**Source**: Aggregated from 38 existing benchmark datasets.

**Size**: 303,000 questions

**Format**: N/A

**Annotation**: Automated categorization using a fine-tuned model.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are derived from evaluating model performance across categorized subsets.

**Interpretation**: Results are interpreted based on domain-specific performance.

**Baseline Results**: Results from model evaluations across benchmarks.

**Validation**: Statistical validation through various sampling strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The whole dataset is released under CC BY-NC-ND 4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
