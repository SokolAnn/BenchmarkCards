# Cross-Lingual Consistency Framework

## 📊 Benchmark Details

**Name**: Cross-Lingual Consistency Framework

**Overview**: The Cross-Lingual Consistency Framework evaluates the multilingual performance profiles of large language models (LLMs) by assessing their consistency when responding to the same queries in different languages, using a 'Translate then Evaluate' method.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Bengali
- Czech
- German
- Greek
- Spanish
- Persian
- French
- Gujarati
- Hindi
- Indonesian
- Italian
- Hebrew
- Japanese
- Kannada
- Korean
- Malayalam
- Dutch
- Punjabi
- Polish
- Portuguese
- Romanian
- Russian
- Tamil
- Telugu
- Thai
- Turkish
- Urdu
- Vietnamese
- Chinese

**Similar Benchmarks**:
- MMLU
- HellaSwag
- WinoGrande

**Resources**:
- [GitHub Repository](https://github.com/anonymized)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the consistency of large language models' responses across multiple languages.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Open-ended Generation
- Information Consistency
- Empathy Consistency

**Limitations**: The framework relies on high-quality translation systems for evaluating low-resource languages.

## 💾 Data

**Source**: Custom prompts curated from MMLU for evaluating LLM performance across multiple languages.

**Size**: 150 prompts

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Translation
- Empathy Classification

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: The consistency score is calculated as the expected compatibility score between translated and original responses.

**Interpretation**: Higher consistency scores indicate better alignment of responses across languages.

**Baseline Results**: N/A

**Validation**: The methodology is validated through empirical evaluation and human assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
