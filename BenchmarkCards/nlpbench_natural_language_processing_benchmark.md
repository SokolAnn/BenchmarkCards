# NLPBench (Natural Language Processing Benchmark)

## 📊 Benchmark Details

**Name**: NLPBench (Natural Language Processing Benchmark)

**Overview**: NLPBench is a novel benchmarking dataset consisting of 378 college-level NLP questions from Yale University’s final exams, aimed at evaluating the ability of large language models (LLMs) to solve NLP-related problems through various question formats.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LinxinS97/NLPBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the problem-solving capabilities of large language models (LLMs) on college-level NLP questions, focusing on their performance in multi-turn interactions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 378 college-level NLP questions sourced from Yale University's final exams.

**Size**: 378 questions

**Format**: JSON

**Annotation**: Manually curated and reviewed by experts to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the models' final answers disregarding intermediary steps.

**Interpretation**: Higher scores indicate better alignment of the generated answers with ground truth.

**Validation**: Evaluated using multiple models including GPT-3.5, GPT-4, and LLAMA-2.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
