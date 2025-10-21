# SOK-Bench (Situated Open-World Commonsense Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: SOK-Bench (Situated Open-World Commonsense Reasoning Benchmark)

**Overview**: SOK-Bench aims to evaluate situated and open-world commonsense reasoning in videos through a benchmark of over 44K questions, linking them with situated commonsense knowledge graphs derived from 10K dynamic situations.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://www.bobbywu.com/SOKBench)

## 🎯 Purpose and Intended Users

**Goal**: To advance AI's ability to comprehend and reason within dynamic, real-world contexts through situated commonsense reasoning evaluation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Question Answering
- Commonsense Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated from videos of the YouCook2 and HOMAGE datasets.

**Size**: 44,000 questions with answers and 10,000 video clips

**Format**: JSON

**Annotation**: Automated generation and manual reviews for quality assurance

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- BLEU Score
- BERT Score
- Accuracy

**Calculation**: BLEU scores calculated between model output and the correct answer in both multiple-choice and direct-answer settings.

**Interpretation**: Higher scores indicate better performance in commonsense reasoning tasks.

**Baseline Results**: Various LLMs and MLLMs evaluated, with GPT4v showing superior performance overall.

**Validation**: Human annotators validated the quality of question-answer pairs, with a 93.08% validity rate.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
