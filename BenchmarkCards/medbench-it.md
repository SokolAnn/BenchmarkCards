# MedBench-IT

## 📊 Benchmark Details

**Name**: MedBench-IT

**Overview**: MedBench-IT is the first comprehensive benchmark designed to evaluate large language models on Italian medical university entrance examinations, comprising 17,410 expert-written multiple-choice questions across six subjects and three difficulty levels.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Italian

**Similar Benchmarks**:
- MedQA
- PubMedQA
- GLUE
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/ruggsea)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation tool for assessing large language models on Italian medical entrance examinations.

**Target Audience**:
- Italian NLP Community
- EdTech Developers
- Practitioners

**Tasks**:
- Question Answering

**Limitations**: The benchmark relies exclusively on multiple-choice questions, limiting depth of understanding compared to open-ended formats.

## 💾 Data

**Source**: Expert-written multiple-choice questions sourced from Edizioni Simone, a leading Italian publisher of medical entrance exam preparatory materials.

**Size**: 17,410 questions

**Format**: N/A

**Annotation**: Expert-authored to accurately reflect official Italian medical admission exam style, content, and difficulty.

## 🔬 Methodology

**Methods**:
- Standard Prompt (Direct Answering)
- Reasoning-Eliciting Prompt

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the percentage of correct answers out of the total number of questions evaluated.

**Interpretation**: Higher accuracy indicates better model performance in answering the questions.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
