# VisuLogic

## 📊 Benchmark Details

**Name**: VisuLogic

**Overview**: VisuLogic is a benchmark of 1,000 human-verified problems designed to evaluate the visual reasoning capabilities of multimodal large language models (MLLMs) without mixing vision-based reasoning with text-based reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://visulogic-benchmark.github.io/VisuLogic)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of VisuLogic is to rigorously evaluate the visual reasoning capabilities of multimodal large language models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Visual Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available online resources with a systematic scraping for question-answer pairs.

**Size**: 1,000 examples

**Format**: JSONL

**Annotation**: Each question is manually verified and categorized based on the targeted reasoning competency.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated using the proportion of correct answers out of total questions.

**Interpretation**: A higher accuracy indicates better visual reasoning capabilities.

**Baseline Results**: Humans achieved 51.4% accuracy while MLLMs generally scored below 30%.

**Validation**: A comprehensive evaluation and systematic analysis of current models' performance on the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
