# PSYDIAL (Personality-based Synthetic Dialogue Generation)

## 📊 Benchmark Details

**Name**: PSYDIAL (Personality-based Synthetic Dialogue Generation)

**Overview**: PSYDIAL is the first Korean dialogue dataset focused on personality-based dialogues, created through an end-to-end personality-based synthetic dialogue data generation pipeline.

**Data Type**: dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Korean

**Resources**:
- [GitHub Repository](https://github.com/jiSilverH/psydial)

## 🎯 Purpose and Intended Users

**Goal**: To generate personality-driven synthetic dialogues to enhance conversational AI.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation
- Personality-based Dialogue Generation

**Limitations**: The ability of CHATGPT to generate Korean dialogues leaves room for improvement; certain phrases may seem unnatural.

## 💾 Data

**Source**: Synthetically generated using Large Language Models through a five-step pipeline.

**Size**: 2,900 dialogues

**Format**: JSON

**Annotation**: Automatically generated with filtering by LLMs.

## 🔬 Methodology

**Methods**:
- Synthetic dialogue generation
- Automated filtering

**Metrics**:
- BLEU
- ROUGE
- Perplexity
- Personality Accuracy

**Calculation**: Metrics such as BLEU and ROUGE measure text similarity, while Perplexity assesses fluency.

**Interpretation**: Higher BLEU and ROUGE scores indicate better quality and similarity to human dialogue.

**Baseline Results**: Models fine-tuned with PSYDIAL show significant improvements in generating personality-reflective dialogues.

**Validation**: Iterative filtering and regeneration of dialogues to ensure quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis on personality dimensions used in the dataset.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
