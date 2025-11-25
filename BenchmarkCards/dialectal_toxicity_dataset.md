# Dialectal Toxicity Dataset

## 📊 Benchmark Details

**Name**: Dialectal Toxicity Dataset

**Overview**: We create a multi-dialect dataset through synthetic transformations and human-assisted translations, covering 10 language clusters and 60 varieties, to evaluate LLMs on their ability to assess toxicity across multilingual, dialectal, and LLM-human consistency.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic
- Bengali
- Chinese
- Finnish
- Kurdish
- Norwegian
- Latvian
- Sotho-Tswana
- Common Turkic
- English

**Similar Benchmarks**:
- ToxiGen

**Resources**:
- [GitHub Repository](https://github.com/ffaisal93/dialect_toxicity_llm_judge)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive toxicity evaluation framework for LLMs across dialectal variations.

**Target Audience**:
- ML Researchers
- Toxicity detection specialists
- Language model developers

**Tasks**:
- Toxicity Detection

**Limitations**: Primarily consists of synthetic and machine-translated dialectal varieties, with limited real-world dialectal examples.

## 💾 Data

**Source**: Synthetic transformations and human-assisted translations from various dialects and languages.

**Size**: Approximately 60 varieties with diverse example counts.

**Format**: N/A

**Annotation**: Human annotations for toxicity intent combined with synthetic transformations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: F1 scores were calculated for model performance across language clusters, while consistency metrics were assessed based on LLM-human agreement.

**Interpretation**: Higher accuracy and F1 scores indicate better performance in toxicity detection across dialects.

**Baseline Results**: Models evaluated include NeMo, Phi-3, and Aya-23 with comparative F1 scores.

**Validation**: Evaluation across diverse dialectal forms with thorough metrics of consistency.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
