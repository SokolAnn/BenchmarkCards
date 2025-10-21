# IsoBench

## 📊 Benchmark Details

**Name**: IsoBench

**Overview**: IsoBench is a benchmark dataset containing problems from four major areas: math, science, algorithms, and games. Each example is presented with multiple isomorphic representations of inputs, such as visual, textual, and mathematical presentations.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Science
- Mathematics
- Games

**Languages**:
- English

**Resources**:
- [Resource](https://isobench.github.io)
- [Resource](https://huggingface.co/datasets/isobench/IsoBench)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark multimodal foundation models by assessing their performance across different input modalities.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Function Analysis
- Algorithmic Problem Solving
- Science Question Answering
- Chess Game Strategy

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset including real-world tasks with multimodal inputs.

**Size**: 1,887 examples

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the performance of multimodal models across varied tasks.

**Interpretation**: Higher accuracy indicates better model performance in understanding and processing multiple input modalities.

**Baseline Results**: N/A

**Validation**: Tested through performance comparison among multiple multimodal models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
