# CROSS (Cultural Reasoning Over Multimodal Scenes for Safety Evaluation)

## 📊 Benchmark Details

**Name**: CROSS (Cultural Reasoning Over Multimodal Scenes for Safety Evaluation)

**Overview**: CROSS is designed to assess the cultural safety reasoning capabilities of large vision-language models (LVLMs) with 1,284 multilingual visually grounded queries sourced from 16 countries, focusing on culturally relevant everyday domains and contexts.

**Data Type**: image-query pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Mandarin Chinese
- Spanish
- Arabic
- Persian
- Hindi
- Japanese
- Thai
- Indonesian
- Portuguese
- Russian
- Amharic
- French

**Similar Benchmarks**:
- MSSBench
- SafeBench
- MM-SafetyBench

**Resources**:
- [GitHub Repository](https://github.com/haoyiq114/CROSS)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the cultural safety of vision-language systems across diverse global contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Cultural Sensitivity Evaluation
- Image-Query Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from visual and cultural norms curated in text-only datasets SafeWorld and CASA, paired with real-world images.

**Size**: 1,284 image-query pairs

**Format**: JSON

**Annotation**: Manually validated by human annotators with diverse backgrounds to ensure cultural relevance and appropriateness.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Cultural Awareness
- Cultural Education
- Cultural Compliance
- Helpfulness

**Calculation**: Metrics are evaluated based on a scoring system from 0 to 1 across four cultural safety dimensions.

**Interpretation**: Scores reflect levels of awareness, educational value, compliance with cultural norms, and helpfulness in guiding safe decision-making.

**Baseline Results**: Performance evaluated against 21 leading LVLMs, revealing significant gaps in cultural safety adherence.

**Validation**: Human evaluations alongside automated scoring by pretrained models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
