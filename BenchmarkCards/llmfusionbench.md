# LLMFusionBench

## 📊 Benchmark Details

**Name**: LLMFusionBench

**Overview**: LLMFusionBench is a large-scale benchmark for LLM fusion that spans 14 tasks across five domains, providing responses from 20 open-source LLMs (8B–671B) totaling 103M tokens, enabling comprehensive studies on LLM fusion.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision
- Education
- Healthcare
- Finance

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/hiyouga/LLaMA-Factory)

## 🎯 Purpose and Intended Users

**Goal**: To support comprehensive studies on the fusion of large language models (LLMs) using multi-LLM log data.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Text Classification
- Question Answering
- Commonsense Reasoning
- Mathematical Problem Solving
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Data from 20 open-source LLMs generating responses across 14 tasks.

**Size**: 103M tokens

**Format**: JSON

**Annotation**: Responses gathered from LLMs using distinct prompts for both direct and reasoning-based outputs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Cost
- LLM Judge Score

**Calculation**: Metrics calculated based on performance evaluation across various tasks using specific task metrics.

**Interpretation**: A higher LLM Judge Score indicates more informative answers, while accuracy reflects the correctness based on ground truth.

**Baseline Results**: N/A

**Validation**: Validation through comprehensive analysis of responses from varied model sizes and evaluation against ground truths.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
