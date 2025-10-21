# VGBench

## 📊 Benchmark Details

**Name**: VGBench

**Overview**: VGBench is a comprehensive benchmark for evaluating Large Language Models (LLMs) on vector graphics understanding and generation across diverse tasks and prompting techniques.

**Data Type**: question-answering pairs, vector graphics code

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://vgbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: The goal of VGBench is to evaluate LLMs' vector graphics processing capabilities, including both understanding and generation aspects across various vector graphics formats.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Visual Understanding
- Visual Generation

**Limitations**: The paper acknowledges limitations in assessing closed-source models and suggests that more evaluations can be conducted.

## 💾 Data

**Source**: Vector graphics samples were collected from existing datasets and the Internet including SVG, TikZ, and Graphviz formats.

**Size**: 4,279 understanding samples, 5,845 generation samples

**Format**: N/A

**Annotation**: QA pairs are curated through a semi-automated process with human filtering.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- CLIP Score
- Fréchet Inception Distance (FID)

**Calculation**: Accuracy is calculated based on the correctness of chosen options against ground-truth answers.

**Interpretation**: Performance is interpreted based on accuracy across various tasks and graphics formats.

**Validation**: Evaluation for both understanding and generation tasks is conducted under multiple LLMs including comparison with VLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
