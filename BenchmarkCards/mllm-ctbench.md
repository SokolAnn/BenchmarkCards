# MLLM-CTBench

## 📊 Benchmark Details

**Name**: MLLM-CTBench

**Overview**: MLLM-CTBench is a comprehensive benchmark designed for evaluating continual instruction tuning of multimodal large language models (MLLMs). It curates a dataset consisting of seven tasks across six diverse domains to assess continual learning ability.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision
- Medicine
- Economics
- Arts
- Science
- Mathematics

**Languages**:
- English

**Similar Benchmarks**:
- EMT
- CITB
- CoIN

**Resources**:
- [Resource](https://huggingface.co/datasets/yueluoshuangtian/MLLM-CITBench)
- [Resource](https://anonymous.4open.science/r/MLLM-CTBench-5E56/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate continual instruction tuning of multimodal large language models, enabling fine-grained analysis of learning algorithms.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Mathematics Question Answering
- Medical Question Answering
- Art Visual Question Answering
- Economics Question Answering
- Science Visual Question Answering
- General Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from 16 public datasets covering various reasoning-intensive domains.

**Size**: 70,000 instances

**Format**: N/A

**Annotation**: High-quality Chain-of-Thought (CoT) annotations are generated tailored to each benchmark task.

## 🔬 Methodology

**Methods**:
- Automated Metrics
- Human Evaluation
- Chain-of-Thought Evaluation

**Metrics**:
- Final Answer Accuracy
- CoT Reasoning Quality

**Calculation**: Metrics are calculated based on the performance of models on various tasks, combining final answer correctness with reasoning quality.

**Interpretation**: A higher score indicates better performance in retaining knowledge and reasoning ability.

**Baseline Results**: Comparative analysis included results from various continual learning algorithms across tasks.

**Validation**: Extensive testing was conducted across different model architectures and task orders.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
