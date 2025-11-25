# Fermi Problems (FP)

## 📊 Benchmark Details

**Name**: Fermi Problems (FP)

**Overview**: Fermi Problems (FPs) are a new reasoning challenge that requires approximating the answers to complex questions that cannot be precisely computed. We present two datasets: 1k real-world FPs and 10k synthetic FPs, both designed to drive progress in AI reasoning systems.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://allenai.org/data/fermi)

## 🎯 Purpose and Intended Users

**Goal**: To propose Fermi Problems as a task to drive progress in AI reasoning systems, specifically assessing their ability to make reasonable abstractions, creatively decompose questions, and employ commonsense reasoning.

**Target Audience**:
- ML Researchers
- AI Practitioners

**Tasks**:
- Reasoning Challenge

**Limitations**: N/A

## 💾 Data

**Source**: A collection of real-world Fermi Problems from quizzes, Olympiads, and a synthetic dataset generated with templates.

**Size**: 11,000 questions

**Format**: JSON

**Annotation**: Expert annotation for real-world problems and template-based generation for synthetic problems.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Answer accuracy
- Validity of program output

**Calculation**: Measured via a scoring metric based on orders of magnitude compared to reference answers.

**Interpretation**: A score close to 1 indicates a correct estimate, while a score of 0 indicates an estimate that is far off.

**Baseline Results**: Models are found to be off by two orders of magnitude on average.

**Validation**: Test split contains real-world Fermi Problems with a majority of questions reserved for evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
