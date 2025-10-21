# TurkishMMLU

## 📊 Benchmark Details

**Name**: TurkishMMLU

**Overview**: TurkishMMLU is the first multitask, multiple-choice Turkish QA benchmark, to evaluate LLMs’ understanding of the Turkish language, including over 10,000 questions across 9 different subjects derived from Turkish high-school education curricula.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- Turkish

**Similar Benchmarks**:
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/ArdaYueksel/TurkishMMLU)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLMs' understanding and reasoning capabilities in the Turkish language through a well-rounded assessment.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: None

## 💾 Data

**Source**: Questions sourced from the Turkish Ministry of Education's online platform for high school education.

**Size**: 10,032 multiple-choice questions

**Format**: N/A

**Annotation**: Questions written and verified by curriculum experts.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Few-shot evaluation
- Chain-of-thought reasoning

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated using lm-evaluation-harness framework, comparing model predictions against ground-truth answers.

**Interpretation**: Higher accuracy indicates better performance in understanding and reasoning for the Turkish language.

**Validation**: Evaluated against a comprehensive leaderboard of over 40 language models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
