# PalmX 2025 Shared Task

## 📊 Benchmark Details

**Name**: PalmX 2025 Shared Task

**Overview**: PalmX 2025 is the first shared task designed to benchmark the cultural competence of Large Language Models (LLMs) in Arabic and Islamic cultures through multiple-choice questions on various cultural topics.

**Data Type**: multiple-choice questions (MCQs)

**Domains**:
- Natural Language Processing

**Languages**:
- Arabic

**Resources**:
- [Resource](https://palmx.dlnlp.ai/)
- [GitHub Repository](https://github.com/UBC-NLP/palmx_2025)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate and compare the cultural competence of LLMs in understanding Arabic and Islamic cultures.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Cultural Competence Evaluation
- Question Answering

**Limitations**: There are inherent dataset imbalances and an evaluation design that limits the assessment to multiple-choice questions in Modern Standard Arabic, which may not capture broader aspects of cultural and linguistic competence.

## 💾 Data

**Source**: Data collected from various cultural and Islamic sources, including web crawls and human-created questions.

**Size**: 8,000 questions total (2,000 training, 500 dev, 2,000 test for General Arabic Culture; 600 training, 300 dev, 1,000 test for General Islamic Culture)

**Format**: JSON

**Annotation**: Questions were created and annotated by language experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The model's predicted label is compared against the ground-truth label for each question, with overall accuracy calculated as the percentage of correctly answered questions.

**Interpretation**: Accuracy measures how well the model predicts the correct answer among multiple choices.

**Baseline Results**: Baseline accuracy for Subtask 1 was 67.55% and for Subtask 2 was 75.12% using the NileChat-3B model without fine-tuning.

**Validation**: The evaluation is blind, ensuring that participants had no prior access to the test data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis of cultural representation across 22 Arab countries, with attention to representation imbalances.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data sources used are publicly available or properly licensed with no personal information collected.

**Data Licensing**: N/A.

**Consent Procedures**: N/A.

**Compliance With Regulations**: N/A.
