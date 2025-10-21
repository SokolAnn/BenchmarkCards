# B2NERD (Beyond-Boundary Named Entity Recognition Dataset)

## 📊 Benchmark Details

**Name**: B2NERD (Beyond-Boundary Named Entity Recognition Dataset)

**Overview**: B2NERD is a compact dataset designed to guide large language models' generalization in Open Named Entity Recognition under a universal entity taxonomy, refined from 54 existing datasets.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/UmeanNever/B2NER)

## 🎯 Purpose and Intended Users

**Goal**: To enhance LLMs for Open NER by directly addressing inconsistencies and redundancies in existing training datasets.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Open Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Refined from 54 existing English and Chinese datasets.

**Size**: 51,907 examples

**Format**: N/A

**Annotation**: Manual annotation by experts including conflict detection and standardization.

## 🔬 Methodology

**Methods**:
- Model-based evaluation
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Metrics are calculated based on strict span-based micro-F1.

**Interpretation**: Higher F1 scores indicate better performance at recognizing entities.

**Baseline Results**: Compared against GPT-4, B2NER models showed an improvement of 6.8-12.0 points in F1 on various benchmarks.

**Validation**: Validation procedures include cross-dataset entity validation experiments to identify inconsistencies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
