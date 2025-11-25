# GLoRE (General Logical Reasoning Evaluation)

## 📊 Benchmark Details

**Name**: GLoRE (General Logical Reasoning Evaluation)

**Overview**: GLoRE is a benchmark designed to assess instruction-tuned large language models on various logical reasoning tasks. It consolidates diverse datasets into a unified format suitable for evaluating LLMs on zero-shot and few-shot scenarios.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- GLUE
- Super-GLUE

**Resources**:
- [Resource](https://arxiv.org/abs/2310.09107)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating the logical reasoning capabilities of large language models across multiple reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-choice Reading Comprehension
- Natural Language Inference
- True-or-False Questions

**Limitations**: N/A

## 💾 Data

**Source**: GLoRE contains data from 12 different datasets including LogiQA, ReClor, and others, focusing on various logical reasoning tasks.

**Size**: 72,848 instances

**Format**: N/A

**Annotation**: The data is collected from existing logical reasoning datasets.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy scores were computed based on model output compared to ground truth answers.

**Interpretation**: Higher accuracy indicates better reasoning performance of language models.

**Baseline Results**: N/A

**Validation**: GLoRE has been tested against various large language models, including GPT-4, OpenAI's o1 mini, and several open-source models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
