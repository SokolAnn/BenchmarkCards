# C3B (Comics Cross-Cultural Benchmark)

## 📊 Benchmark Details

**Name**: C3B (Comics Cross-Cultural Benchmark)

**Overview**: C3B is a novel multicultural, multitask and multilingual cultural awareness capabilities benchmark composed of over 2,220 images and over 18,789 QA pairs, designed to evaluate MLLMs' cultural awareness through three progressively difficult tasks.

**Data Type**: image-question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Japanese
- Russian
- Thai
- English
- Spanish

**Similar Benchmarks**:
- CVQA
- CulturalVQA
- GIMMICK

**Resources**:
- [Resource](https://c3b-benchmark.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To advance the cultural awareness capabilities of Multimodal Large Language Models (MLLMs) through comprehensive evaluation.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Recognition
- Cultural Conflict Understanding
- Cultural Content Generation

**Limitations**: N/A

## 💾 Data

**Source**: C3B consists of 2,220 images generated using comic generation technologies and manually selected from culture-representative comics.

**Size**: 2,220 images and 18,789 QA pairs

**Format**: image and question-answer pair format

**Annotation**: Manual QA pair creation and automated cultural conflict detection.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- BLEU Score
- COMET
- BLEURT

**Calculation**: Specific weighting for metrics considering contributions of various tasks.

**Interpretation**: Scores indicate the understanding of cultural contexts and conflicts by MLLMs, with results compared to human performance.

**Baseline Results**: C3B evaluations show a significant performance gap between MLLMs and human evaluators.

**Validation**: Evaluations were conducted across multiple open-source MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
