# Minerva: A Programmable Memory Test Benchmark for Language Models

## 📊 Benchmark Details

**Name**: Minerva: A Programmable Memory Test Benchmark for Language Models

**Overview**: This paper presents a framework for automatically generating a comprehensive set of tests to evaluate models' abilities to use their memory effectively. It includes atomic and composite tests that assess memory utilization capabilities in large language models (LLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/microsoft/minerva_memory_test)

## 🎯 Purpose and Intended Users

**Goal**: To establish a comprehensive benchmark for evaluating memory usage capabilities of large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Information Retrieval
- Memory Recall
- Data Processing
- Comparative Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Tasks are generated using a framework that allows programmable tests to evaluate LLM capabilities.

**Size**: 1110 examples

**Format**: Various formats, including textual prompts based on the specific testing tasks.

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Exact Match
- ROUGE-L
- Jaccard Similarity

**Calculation**: Metrics are calculated to assess model performance against standard evaluation criteria for memory tasks.

**Interpretation**: Higher scores indicate better model capability in context utilization and memory processing.

**Baseline Results**: Performance varies significantly based on the model type, with GPT-4 models exhibiting stronger all-around performance.

**Validation**: The benchmark's effectiveness is tested through multiple evaluations across various models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
