# AHaBench

## 📊 Benchmark Details

**Name**: AHaBench

**Overview**: AHaBench is a benchmark of 500 mental health-related prompts designed to diagnose affective hallucination in large language models (LLMs) with expert-informed reference responses.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EmotionBench
- EmotionQueen
- EmoBench

**Resources**:
- [Resource](https://huggingface.co/datasets/o0oMiNGo0o/AHaBench)
- [GitHub Repository](https://github.com/0oOMiNGOo0/AHaBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and mitigate the risk of affective hallucination in LLMs and to provide resources for developing emotionally responsible AI systems.

**Target Audience**:
- ML Researchers
- Model Developers
- Mental Health Professionals

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Publicly available Reddit posts from mental health-related subreddits.

**Size**: 500 prompts

**Format**: CSV

**Annotation**: Crafted responses authored by subject matter experts to reflect optimal conversational behavior.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- AHa Score

**Calculation**: AHa Score is a seven-point scale (0-6) with higher values indicating stronger adherence to emotional safety.

**Interpretation**: Scores of 3 or higher denote the absence of affective hallucination, while scores of 2 or lower indicate violations of emotional boundaries.

**Baseline Results**: N/A

**Validation**: Human agreement analyses confirm benchmark reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data used in AHaBench is sourced from publicly available, anonymized posts, adhering to privacy standards.

**Data Licensing**: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
