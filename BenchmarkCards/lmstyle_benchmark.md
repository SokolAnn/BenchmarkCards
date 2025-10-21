# LMStyle Benchmark

## 📊 Benchmark Details

**Name**: LMStyle Benchmark

**Overview**: LMStyle Benchmark is a novel evaluation framework for chat-style text style transfer (C-TST) that measures the quality of style transfer for LLMs, considering both conventional style strength metrics and a new metric called appropriateness.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standard evaluation paradigm for chat-style text style transfer (C-TST) tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Style Transfer

**Limitations**: The evaluation of style strength may bottleneck the overall effectiveness.

## 💾 Data

**Source**: Daily Dialog and Blended Skill Talk datasets

**Size**: 1,000 examples from each dataset

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Appropriateness
- Style strength

**Calculation**: Metrics are calculated based on correlations with human judgments using Pearson and Kendall's Tau correlation methods.

**Interpretation**: Appropriateness and style strength scores indicate how well models can transfer text styles.

**Validation**: Evaluated against human assessments for various model outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
