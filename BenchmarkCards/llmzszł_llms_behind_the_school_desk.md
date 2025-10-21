# LLMzSzŁ (LLMs Behind the School Desk)

## 📊 Benchmark Details

**Name**: LLMzSzŁ (LLMs Behind the School Desk)

**Overview**: This article introduces the first comprehensive benchmark for the Polish language at this scale: LLMzSzŁ (LLMs Behind the School Desk). It is based on a coherent collection of Polish national exams, including both academic and professional tests extracted from the archives of the Polish Central Examination Board.

**Data Type**: closed-ended questions

**Domains**:
- Natural Language Processing

**Languages**:
- Polish

**Similar Benchmarks**:
- MMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/amu-cai/llmzszl-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating LLMs' abilities in the Polish language and to analyse their performance against human examinees.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: As any competence test that is not designed to test the notion of intelligence in isolation, the presented benchmark intermixes to some extent the measurement of the reasoning capabilities of the model with the assessment of its ability to memorize factual knowledge.

## 💾 Data

**Source**: Polish national exams from the archives of the Polish Central Examination Board.

**Size**: 19,000 questions

**Format**: PDF

**Annotation**: Questions and answers were cleaned and matched manually, with data extracted using automated techniques where feasible.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The accuracy is calculated by comparing the model's predicted answer with the correct answer based on the probabilities given by language models.

**Interpretation**: Higher accuracy indicates better performance of the model relative to human results.

**Validation**: The benchmark was validated through the performance of various LLMs against established human exam scores.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark includes a stratification of exams by difficulty level and type.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
