# HiBench

## 📊 Benchmark Details

**Name**: HiBench

**Overview**: HiBench is the first framework designed to evaluate the hierarchical reasoning capabilities of large language models (LLMs), encompassing six scenarios and 30 tasks with a total of 39,519 queries. It systematically assesses how LLMs organize, process, and reason with multi-level information through various capability dimensions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://arxiv.org/abs/2503.00912)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic framework for assessing LLMs' hierarchical reasoning capabilities across multiple dimensions and scenarios, focusing on fundamental and practical aspects.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Hierarchical Structure Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed through a hierarchical dataset generator that creates structured data for benchmarking the reasoning capabilities of LLMs.

**Size**: 39,519 queries

**Format**: JSON

**Annotation**: Automatically generated and manual annotations for complex tasks in the Paper scenario.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is defined as the ratio of correct answers to total queries.

**Interpretation**: Higher accuracy indicates better hierarchical reasoning capability of LLMs across the evaluated tasks.

**Validation**: Results validated through extensive evaluation of 20 LLMs across various tasks within the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
