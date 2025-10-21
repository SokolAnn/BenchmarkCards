# MLLM-as-a-Judge

## 📊 Benchmark Details

**Name**: MLLM-as-a-Judge

**Overview**: This paper presents MLLM-as-a-Judge, a novel benchmark to assess the judging capabilities of Multimodal Large Language Models (MLLMs) across three critical evaluation settings in the multimodal domain: Scoring Evaluation, Pair Comparison, and Batch Ranking.

**Data Type**: image-instruction pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://mllm-judge.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the efficacy of MLLMs in assisting judges across diverse modalities and to establish a comprehensive benchmark for ongoing research.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Scoring Evaluation
- Pair Comparison
- Batch Ranking

**Limitations**: MLLMs demonstrate notable discrepancies in Scoring Evaluation and Batch Ranking tasks.

## 💾 Data

**Source**: Curated from 14 diverse datasets across tasks, including image captioning, math reasoning, text reading, and infographics understanding.

**Size**: 4,414 image-instruction pairs

**Format**: N/A

**Annotation**: Responses annotated by human evaluators with stringent criteria.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision

**Calculation**: Pearson similarity is computed between MLLMs' judgments and human ratings across different tasks.

**Interpretation**: Responses are evaluated based on their relevance, accuracy, comprehensiveness, creativity, and granularity.

**Baseline Results**: GPT-4V consistently outperforms other models across tasks.

**Validation**: Evaluations conducted with diverse human annotators to ensure reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Bias and hallucination in judgments']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
