# VCRL (Variance-based Curriculum Reinforcement Learning)

## 📊 Benchmark Details

**Name**: VCRL (Variance-based Curriculum Reinforcement Learning)

**Overview**: VCRL is a curriculum reinforcement learning framework that dynamically controls the difficulty of training samples based on the variance of group rewards to improve the learning efficiency of large language models (LLMs) on mathematical reasoning tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AIME-2024
- AIME-2025
- MATH500
- OlympiadBench
- AMC23

**Resources**:
- [Resource](https://huggingface.co/datasets/Maxwell-Jia/AIME_2024)
- [Resource](https://huggingface.co/datasets/yentinglin/aime_2025)
- [Resource](https://huggingface.co/datasets/AI-MO/aimo-validation-amc)
- [Resource](https://huggingface.co/datasets/BytedTsinghua-SIA/DAPO-Math-17k)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of VCRL is to enhance the mathematical reasoning capabilities of large language models through a curriculum learning approach that adjusts sample difficulty based on reward variance.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Mathematical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: DAPO-Math-17K dataset consisting of 17,000 prompts paired with integer answers.

**Size**: 17,000 examples

**Format**: JSON

**Annotation**: Automatically generated rewards based on output responses.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Variance-based Dynamic Sampling
- Memory Bank for Replay Learning

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on performance improvements across different mathematical benchmarks.

**Interpretation**: Higher performance values are interpreted as better reasoning capabilities of the model.

**Validation**: Extensive experiments on five mathematical benchmarks validate the performance of VCRL.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
