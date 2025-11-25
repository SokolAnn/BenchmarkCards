# FORMOSAN BENCH

## 📊 Benchmark Details

**Name**: FORMOSAN BENCH

**Overview**: FORMOSAN BENCH is the first benchmark for evaluating LLMs on low-resource Austronesian languages, specifically covering three endangered Formosan languages: Atayal, Amis, and Paiwan, across three core NLP tasks: machine translation, automatic speech recognition, and text summarization.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Atayal
- Amis
- Paiwan

**Similar Benchmarks**:
- IrokoBench

**Resources**:
- [Resource](https://anonymous.4open.science/r/FormosanBench-DB43/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models on low-resource Formosan languages across several NLP tasks and to underscore the need for more effective NLP technologies for endangered languages.

**Target Audience**:
- ML Researchers
- NLP Practitioners
- Linguists

**Tasks**:
- Machine Translation
- Automatic Speech Recognition
- Text Summarization

**Limitations**: The current study presents results for only a limited number of Formosan languages, and incorporating additional NLP tasks is constrained by substantial human effort for data annotation and validation.

## 💾 Data

**Source**: Datasets were sourced from the Taiwan Indigenous Languages E-Dictionary and the Klok¯a Digital Platform, curated from Wikipedia articles, and designed for machine translation, ASR, and summarization tasks.

**Size**: 5,000 sentence pairs for machine translation; various counts for ASR and summarization datasets.

**Format**: JSON

**Annotation**: Datasets were manually curated and verified for quality and accuracy prior to release.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU Score
- Word Error Rate (WER)
- ROUGE-L

**Calculation**: Metrics were calculated to evaluate the performance of models across translation, speech recognition, and summarization tasks based on standard evaluation techniques.

**Interpretation**: BLEU scores provide precision in translation tasks, while WER and ROUGE assess the accuracy of speech recognition and summarization outputs, respectively.

**Baseline Results**: No explicit baseline results were detailed in the paper.

**Validation**: Datasets underwent task-specific quality control to ensure meaningful training and evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Performance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Analysis of demographic factors is not explicitly discussed.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
