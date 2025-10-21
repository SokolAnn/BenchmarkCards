# MMReview

## 📊 Benchmark Details

**Name**: MMReview

**Overview**: MMReview is a comprehensive benchmark for peer review generation that spans multiple disciplines and modalities, including multimodal content and expert-written review comments for 240 papers across 17 research domains within four major academic disciplines: Artificial Intelligence, Natural Sciences, Engineering Sciences, and Social Sciences.

**Data Type**: multimodal (text, images, tables)

**Domains**:
- Natural Language Processing
- Computer Vision
- Artificial Intelligence
- Natural Sciences
- Engineering Sciences
- Social Sciences

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.14146)

## 🎯 Purpose and Intended Users

**Goal**: To establish a comprehensive benchmark for evaluating the capabilities of Large Language Models (LLMs) in academic peer review across different modalities and disciplines.

**Target Audience**:
- ML Researchers
- Academic Institutions
- Industry Practitioners

**Tasks**:
- Review Generation
- Outcome Formulation
- Preference Evaluation
- Robustness Testing

**Limitations**: None

## 💾 Data

**Source**: Academic papers from publicly accessible peer review platforms and open review comments.

**Size**: 240 samples

**Format**: JSON

**Annotation**: Curated peer review comments and outcomes, verified by experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy
- Mean Absolute Error (MAE)

**Calculation**: Computed metrics involved comparing model outputs to human-generated reviews across multiple tasks designed within the benchmark.

**Interpretation**: Model performance is interpreted based on scoring consistency with human reviewers and the quality of generated reviews.

**Validation**: Validated through comprehensive evaluation across various LLMs and review tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack, Evasion attack
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of performance across various research domains and input modalities is included in the benchmark evaluation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
