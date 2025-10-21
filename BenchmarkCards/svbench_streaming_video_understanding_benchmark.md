# SVBench (Streaming Video Understanding Benchmark)

## 📊 Benchmark Details

**Name**: SVBench (Streaming Video Understanding Benchmark)

**Overview**: SVBench is a pioneering benchmark with temporal multi-turn question-answering chains specifically designed to thoroughly assess the capabilities of streaming video understanding of current Large Vision-Language Models (LVLMs). It features 49,979 question-answer pairs across 1,353 streaming videos, evaluating models on long-context scenarios and temporal reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- TVQA
- ActivityNet-QA
- MovieChat

**Resources**:
- [Resource](https://yzy-bupt.github.io/SVBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive and in-depth analysis of current LVLMs' capabilities in streaming video understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from diverse publicly available datasets, including YT-Temporal-1B, YouCook2, ActivityNet, MovieChat, Panda-70M, and Ego4D.

**Size**: 49,979 question-answer pairs and 1,353 videos

**Format**: Varied formats dependent on video content

**Annotation**: Semi-automated annotation pipeline utilizing LLMs and professional annotators for quality assurance.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Semantic Accuracy
- Contextual Coherence
- Logical Consistency
- Temporal Understanding
- Informational Completeness

**Calculation**: Aggregate scores based on predefined criteria for evaluation.

**Interpretation**: Scores indicate reliability and performance of LVLMs in understanding streaming video content.

**Baseline Results**: N/A

**Validation**: Extensive evaluations were conducted with various LVLMs across dialogue and streaming settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
