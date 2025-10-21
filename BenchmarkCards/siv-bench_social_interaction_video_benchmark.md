# SIV-Bench (Social Interaction Video Benchmark)

## 📊 Benchmark Details

**Name**: SIV-Bench (Social Interaction Video Benchmark)

**Overview**: SIV-Bench is a novel video benchmark designed for rigorously evaluating the capabilities of Multimodal Large Language Models (MLLMs) across Social Scene Understanding (SSU), Social State Reasoning (SSR), and Social Dynamics Prediction (SDP).

**Data Type**: video and question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Japanese
- Spanish
- Filipino
- Korean

**Similar Benchmarks**:
- Social-IQ 2.0
- Videovista
- MLVU

**Resources**:
- [Resource](https://kfq20.github.io/sivbench/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate Multimodal Large Language Models' capabilities in understanding and reasoning within social interaction scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Social Scene Understanding
- Social State Reasoning
- Social Dynamics Prediction

**Limitations**: The current scale suggests room for future expansion into a larger training corpus with broader social contexts and more diverse content.

## 💾 Data

**Source**: Videos sourced from TikTok and YouTube.

**Size**: 2,792 video clips and 8,728 question-answer pairs

**Format**: MP4 for videos and JSON for question-answer pairs

**Annotation**: Generated through a human-LLM collaborative pipeline.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Calculated based on the correct answers provided by evaluated models.

**Interpretation**: Higher accuracy indicates better understanding and reasoning by the models.

**Baseline Results**: Results show clear performance differences across the three dimensions.

**Validation**: Validation through human verification and automated filtering steps.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Diverse language content reflecting various cultures.

**Potential Harm**: ['Potential misuse for manipulation or biased outcomes.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
