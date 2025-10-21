# MDVP-Bench

## 📊 Benchmark Details

**Name**: MDVP-Bench

**Overview**: MDVP-Bench is a challenging benchmark designed to evaluate a model’s ability to understand visual prompting instructions, encompassing a variety of tasks including point-level and region-level captioning, inter-relationship analysis, and complex reasoning.

**Data Type**: image-visual prompt-text triplets

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VQA
- TextVQA
- DocVQA

**Resources**:
- [Resource](https://draw-and-understand.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a solid foundation for future research in the field of visual prompting and multimodal models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Point-level Captioning
- Region-level Captioning
- Inter-relationship Analysis
- Complex Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: MDVP-Instruct-Data, curated from existing datasets with additional data generated using GPT-4V.

**Size**: 1.2 million image-visual prompt-text triplets

**Format**: JSONL

**Annotation**: Annotated using a combination of existing datasets and GPT-4V generated content.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance scores in tasks such as point-level and region-level captioning.

**Interpretation**: Higher scores indicate better model performance when understanding and generating responses to visual prompting instructions.

**Validation**: Evaluation against state-of-the-art models in various visual prompting tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
