# CLongEval (Chinese Benchmark for Evaluating Long-Context Large Language Models)

## 📊 Benchmark Details

**Name**: CLongEval (Chinese Benchmark for Evaluating Long-Context Large Language Models)

**Overview**: CLongEval is a comprehensive Chinese benchmark for evaluating long-context LLMs, consisting of 7 tasks and 7,267 examples, designed to assess key capabilities such as information acquisition and reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/zexuanqiu/CLongEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for long-context large language models in the Chinese language.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Long Story QA
- Long Conversation Memory
- Long Story Summarization
- Stacked News Labeling
- Stacked Typo Detection
- Key-Passage Retrieval
- Table Querying

**Limitations**: CLongEval is specifically crafted for the evaluation of Chinese long-context LLMs, making it inapplicable to LLMs primarily focused on other languages.

## 💾 Data

**Source**: The data is constructed from various public datasets and annotations, including human annotations and GPT-4 annotations.

**Size**: 7,267 examples

**Format**: JSON

**Annotation**: Human annotation by experts, GPT-4 annotation, and reconstruction from public datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- F1 Score
- ROUGE-L
- Average Accuracy
- Edit Score
- Exact Match

**Calculation**: Metrics are calculated based on the comparison between model outputs and reference outputs for each task.

**Interpretation**: Higher scores indicate better model performance in understanding and generating outputs based on long-context inputs.

**Validation**: The benchmark is validated through evaluations of multiple long-context LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark aims to address performance across different demographic representations in Chinese LLMs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
