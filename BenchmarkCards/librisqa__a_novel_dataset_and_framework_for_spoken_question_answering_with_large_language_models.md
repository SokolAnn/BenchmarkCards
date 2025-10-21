# LibriSQA: A Novel Dataset and Framework for Spoken Question Answering with Large Language Models

## 📊 Benchmark Details

**Name**: LibriSQA: A Novel Dataset and Framework for Spoken Question Answering with Large Language Models

**Overview**: LibriSQA is a novel free-form and open-ended Spoken Question Answering (SQA) dataset composed of 214k SQA pairs, focusing on interactions between speech and text modalities and optimized for Large Language Models (LLMs).

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ZihanZhaoSJTU/LibriSQA)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in the perception and understanding of speech leveraging Large Language Models (LLMs) for Spoken Question Answering tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Spoken Question Answering
- Automatic Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is developed using the LibriSpeech dataset, specifically extracted audio segments, annotated with questions and answers generated via ChatGPT.

**Size**: 214,000 question-answer pairs

**Format**: JSON

**Annotation**: Questions and answers generated through ChatGPT with manual filtration for relevance.

## 🔬 Methodology

**Methods**:
- End-to-end framework without relying on ASR modules
- Evaluation using BLEU, ROUGE, BERT similarity, macro accuracy, and F1 scores

**Metrics**:
- Accuracy
- F1 Score
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on model predictions versus reference answers, following standard evaluation metrics.

**Interpretation**: Higher scores indicate better alignment and comprehension of the spoken content and contextual understanding.

**Validation**: The framework is validated through empirical performance metrics on the ASR and SQA tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
