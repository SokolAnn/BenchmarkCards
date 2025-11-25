# ONERULER

## 📊 Benchmark Details

**Name**: ONERULER

**Overview**: ONERULER is a multilingual benchmark designed to evaluate long-context language models across 26 languages, adapting the English-only RULER benchmark and including seven synthetic tasks focused on retrieval and aggregation.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese
- Czech
- Danish
- Dutch
- Finnish
- French
- German
- Hindi
- Hungarian
- Italian
- Japanese
- Korean
- Norwegian
- Persian
- Polish
- Portuguese
- Russian
- Serbian
- Sesotho
- Spanish
- Swahili
- Swedish
- Tamil
- Ukrainian
- Vietnamese

**Similar Benchmarks**:
- RULER

**Resources**:
- [GitHub Repository](https://github.com/mungg/OneRuler)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ONERULER is to evaluate multilingual long-context language models' retrieval and aggregation capabilities.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Needle-in-a-Haystack Retrieval
- Aggregation

**Limitations**: N/A

## 💾 Data

**Source**: Created through a two-step process involving writing English instructions and translating them into 25 additional languages with the help of native speakers.

**Size**: 5.2K prompts per task per model across four context lengths and 26 languages

**Format**: N/A

**Annotation**: Translation by native speakers with strong English proficiency.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on prompt responses in various languages and contexts.

**Interpretation**: Higher accuracy indicates better model performance on long-context tasks.

**Baseline Results**: Gemini 1.5 Flash showed the best overall performance across models.

**Validation**: Cross-validated using diverse languages and model types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Models may exhibit bias and performance disparities between high-resource and low-resource languages.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
