# AMBER (An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination Evaluation)

## 📊 Benchmark Details

**Name**: AMBER (An LLM-free Multi-dimensional Benchmark for MLLMs Hallucination Evaluation)

**Overview**: AMBER is a multi-dimensional benchmark designed for evaluating hallucinations in Multi-modal Large Language Models (MLLMs). It assesses generative and discriminative tasks involving existence, attribute, and relation hallucinations without requiring additional LLMs.

**Data Type**: image with annotations

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/junyangwang0410/AMBER)

## 🎯 Purpose and Intended Users

**Goal**: To provide a cost-effective and efficient evaluation benchmark for hallucination in MLLMs across various types of hallucination and tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Generative Task
- Discriminative Task

**Limitations**: AMBER offers limited evaluation for attributes and relations because it does not guarantee effective generative descriptions.

## 💾 Data

**Source**: MS-COCO 2014 test set and copyright-free image repositories like UnSplash.

**Size**: 1,004 images

**Format**: N/A

**Annotation**: Manually annotated by multiple groups of annotators covering existence, attributes, and relations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-free evaluation

**Metrics**:
- CHAIR
- Coverage
- Hal
- Cog
- Accuracy
- Precision
- Recall
- F1

**Calculation**: Metrics are calculated based on responses obtained from MLLMs using specific prompt templates designed for evaluation.

**Interpretation**: Lower values in CHAIR and Hal indicate fewer hallucinations. A higher F1 indicates better performance in correctly detecting objects.

**Baseline Results**: 2023 evaluations of GPT-4V and other mainstream models show variation in hallucination scores.

**Validation**: Evaluation tested across multiple MLLMs including GPT-4V, MiniGPT-4, and others.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Existing hallucinations may result in misleading content generation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Images sourced under Creative Commons Zero (CC0) license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
