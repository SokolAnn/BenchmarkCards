# EgoThink

## 📊 Benchmark Details

**Name**: EgoThink

**Overview**: EgoThink is a novel visual question-answering benchmark designed to evaluate the first-person perspective thinking capability of vision-language models (VLMs) across six core capabilities and twelve dimensions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://adacheng.github.io/EgoThink/)
- [GitHub Repository](https://github.com/AdaCheng/EgoThink/)
- [Resource](https://huggingface.co/datasets/EgoThink/EgoThink/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the thinking capability of vision-language models from a first-person perspective.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Selected clips from the Ego4D video dataset, manually annotated with question-answer pairs.

**Size**: 700 examples

**Format**: N/A

**Annotation**: Annotated by six annotators with three additional reviewers ensuring quality.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics using GPT-4 for scoring

**Metrics**:
- Pearson correlation with human evaluation, Accuracy

**Calculation**: Evaluation scores are computed based on outputs compared to reference answers.

**Interpretation**: Scores are derived from a scale of 0 (wrong), 0.5 (partially correct), to 1 (correct).

**Baseline Results**: Performance across various VLMs remains below optimal, with top scores around 60 points.

**Validation**: Comparative evaluations against a broad array of vision-language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
