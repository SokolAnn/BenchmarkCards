# MCLM (Multilingual Competition Level Math)

## 📊 Benchmark Details

**Name**: MCLM (Multilingual Competition Level Math)

**Overview**: MCLM is a multilingual math benchmark featuring competition-level problems in 55 languages. It aims to investigate the linguistic generalizability of test-time scaling methods in mathematical reasoning.

**Data Type**: mathematical reasoning problems

**Domains**:
- Natural Language Processing

**Languages**:
- Afrikaans
- Albanian
- Arabic
- Bengali
- Bulgarian
- Catalan
- Chinese (Simplified)
- Chinese (Traditional)
- Croatian
- Czech
- Danish
- Dutch
- Estonian
- Finnish
- French
- German
- Greek
- Gujarati
- Hebrew
- Hindi
- Hungarian
- Indonesian
- Italian
- Japanese
- Kannada
- Korean
- Latvian
- Lithuanian
- Macedonian
- Malayalam
- Marathi
- Nepali
- Norwegian
- Persian
- Polish
- Portuguese
- Punjabi
- Romanian
- Russian
- Slovak
- Slovenian
- Somali
- Spanish
- Swahili
- Swedish
- Tagalog
- Tamil
- Telugu
- Thai
- Turkish
- Ukrainian
- Urdu
- Vietnamese
- Welsh
- English

**Similar Benchmarks**:
- MGSM
- AIME

**Resources**:
- [GitHub Repository](https://github.com/gauss5930/MCLM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark that evaluates the multilingual reasoning capability of models in mathematical contexts.

**Target Audience**:
- ML Researchers
- Model Developers
- Educators

**Tasks**:
- Mathematical Reasoning

**Limitations**: While the benchmark provides high-level competition problems, it does not ensure robust performance across all languages.

## 💾 Data

**Source**: MATH-500 and AIME datasets translated using GPT-4o, along with human-validated mathematical Olympiad questions.

**Size**: 250,000 questions across 55 languages

**Format**: JSON

**Annotation**: Machine-translated and verified human-annotated translations

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Fleiss' Kappa

**Calculation**: Metrics are calculated based on the proportion of correct answers and the consistency across languages.

**Interpretation**: Higher accuracy indicates better overall performance, while higher Fleiss' Kappa suggests better cross-lingual consistency.

**Baseline Results**: Qwen2.5-1.5B achieved a score of 35.8 on MCLM.

**Validation**: Validation conducted through comparing model outputs against verified answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Machine-translated subsets are released under the MIT License; other subsets under a CC BY-NC-ND license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
