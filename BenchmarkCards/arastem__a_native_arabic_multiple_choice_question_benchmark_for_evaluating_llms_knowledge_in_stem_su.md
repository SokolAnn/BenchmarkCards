# AraSTEM: A Native Arabic Multiple Choice Question Benchmark for Evaluating LLMs Knowledge In STEM Subjects

## 📊 Benchmark Details

**Name**: AraSTEM: A Native Arabic Multiple Choice Question Benchmark for Evaluating LLMs Knowledge In STEM Subjects

**Overview**: AraSTEM is a new Arabic multiple-choice question dataset aimed at evaluating LLMs knowledge in STEM subjects including Math, Science, Physics, Biology, Chemistry, Computer Science, and Medicine. It contains 11,637 questions across elementary to professional levels, requiring a deep understanding of scientific Arabic.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Arabic

**Similar Benchmarks**:
- Multilingual Massive Multitask Language Understanding (MMMLU)
- ArabicMMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/AraSTEM)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating the knowledge of Large Language Models (LLMs) in the Arabic language across STEM subjects.

**Target Audience**:
- ML Researchers
- Language Model Developers
- Educators

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Multiple sources including scraping from MCQ websites, manual extraction from books, and LLM extraction from PDF files.

**Size**: 11,637 questions

**Format**: N/A

**Annotation**: Questions were manually annotated and sourced from credible educational materials.

## 🔬 Methodology

**Methods**:
- Zero-shot evaluation
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered questions by the models across different subjects.

**Interpretation**: Models are expected to demonstrate an understanding of scientific concepts in Arabic, with a higher accuracy indicating better performance.

**Baseline Results**: The best-performing model achieved an accuracy of 56% on average.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
