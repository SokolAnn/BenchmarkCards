# HeQ (Hebrew QA)

## 📊 Benchmark Details

**Name**: HeQ (Hebrew QA)

**Overview**: HeQ is a Hebrew Machine Reading Comprehension (MRC) dataset designed for extractive Question Answering, featuring 30,147 diverse question-answer pairs derived from Hebrew Wikipedia articles and Israeli tech news.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Hebrew

**Similar Benchmarks**:
- SQuAD

**Resources**:
- [GitHub Repository](https://github.com/NNLP-IL/Hebrew-Question-Answering-Dataset)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of HeQ is to enable further research into Hebrew natural language understanding by providing a benchmark for machine reading comprehension tasks.

**Target Audience**:
- NLP Researchers
- Machine Learning Practitioners

**Tasks**:
- Machine Reading Comprehension
- Question Answering

**Limitations**: Despite its high quality, HeQ has a relatively smaller number of instances compared to well-established English MRC datasets like SQuAD.

## 💾 Data

**Source**: HeQ was created by combining two distinct data sources, namely, Hebrew Wikipedia and Geektime, an Israeli technology newspaper.

**Size**: 30,147 examples

**Format**: CSV

**Annotation**: The data was annotated by native Hebrew speakers through a controlled crowdsourcing protocol.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score
- Token-Level Normalized Levenshtein Similarity (TLNLS)

**Calculation**: TLNLS is calculated using a hybrid metric derived from F1 and Levenshtein similarity.

**Interpretation**: A higher TLNLS score indicates better model performance on extraction tasks, reflecting how well the model matches answer spans in the context.

**Validation**: The dataset was validated through manual checking of the test and development sets, ensuring high accuracy and quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes various demographic factors derived from the source texts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
