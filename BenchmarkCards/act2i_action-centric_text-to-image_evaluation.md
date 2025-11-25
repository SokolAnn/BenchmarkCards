# AcT2I (Action-centric Text-to-Image Evaluation)

## 📊 Benchmark Details

**Name**: AcT2I (Action-centric Text-to-Image Evaluation)

**Overview**: AcT2I is a benchmark designed to evaluate the performance of Text-to-Image models in generating images from action-centric prompts, addressing the challenges in accurately depicting complex interactions and nuanced attributes within action scenarios.

**Data Type**: text prompts

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- T2I-CompBench
- GenEval

**Resources**:
- [Resource](https://vatsal-malaviya.github.io/AcT2I/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of T2I models to generate images from textual prompts that describe actions.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Image Generation

**Limitations**: N/A

## 💾 Data

**Source**: Animal Kingdom dataset (Ng et al., 2022)

**Size**: 125 prompts

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with 25 annotators rating each image.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Acceptance Rate

**Calculation**: Acceptance rate is defined as the proportion of images receiving a 'Yes' from a majority of annotators.

**Interpretation**: An acceptance rate above 50% indicates successful representation of the action in images.

**Baseline Results**: The highest acceptance rate observed was 48% for Stable Diffusion 3.5 Large.

**Validation**: Evaluation was performed across 5 state-of-the-art T2I models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential misuse of realistic imagery and propagation of biases present within the training data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset involves animal subjects with no personal data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: The generated images are free of sensitive human information, ensuring compliance with ethical research guidelines.
