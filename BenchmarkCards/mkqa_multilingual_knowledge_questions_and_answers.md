# MKQA (Multilingual Knowledge Questions and Answers)

## 📊 Benchmark Details

**Name**: MKQA (Multilingual Knowledge Questions and Answers)

**Overview**: MKQA is an open-domain question answering evaluation set comprising 10k question-answer pairs aligned across 26 typologically diverse languages (260k question-answer pairs in total), designed to facilitate fair comparison between various multilingual QA methods.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Spanish
- German
- French
- Italian
- Chinese (Simplified)
- Chinese (Traditional)
- Japanese
- Korean
- Russian
- Vietnamese
- Turkish
- Thai
- Polish
- Hungarian
- Danish
- Vietnamese
- Malay
- Finnish
- Hebrew
- Khmer
- Norwegian
- Portuguese
- Dutch

**Similar Benchmarks**:
- Natural Questions
- MLQA
- XQuAD
- TyDi

**Resources**:
- [GitHub Repository](https://github.com/apple/ml-mkqa)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging, realistic, and linguistically diverse benchmark for evaluating multilingual open-domain question answering methods.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 10k realistic English queries from the Natural Questions dataset translated into 25 additional languages.

**Size**: 260,000 question-answer pairs

**Format**: N/A

**Annotation**: Answers are based on heavily curated, language-independent data representation, with high inter-annotator agreement.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Exact Match

**Calculation**: F1 Score is calculated based on exact match and token overlap for the validated question-answer pairs.

**Interpretation**: An increase in F1 Score indicates better model performance in answering the questions correctly.

**Baseline Results**: Best model obtains only 52.3% F1 in English.

**Validation**: The FKQA dataset is validated by ensuring inter-annotator agreement and through expert review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
