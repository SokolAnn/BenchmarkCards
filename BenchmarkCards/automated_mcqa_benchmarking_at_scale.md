# Automated MCQA Benchmarking at Scale

## 📊 Benchmark Details

**Name**: Automated MCQA Benchmarking at Scale

**Overview**: We introduce a scalable, modular framework for generating multiple-choice question-answering (MCQA) benchmarks directly from large corpora of scientific papers. As a case study, we generate more than 16,000 MCQs from 22,000 open-access articles in radiation and cancer biology and evaluate small language models on these questions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- ARC
- GPQA
- SciQA
- PaperQA
- MMLU

**Resources**:
- [GitHub Repository](https://github.com/ramanathanlab/distllmstudy)

## 🎯 Purpose and Intended Users

**Goal**: To provide a timely, reproducible, and extensible benchmark for evaluating language models in the domain of radiation and cancer biology.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from 14,115 full-text papers and 8,433 abstracts downloaded via the Semantic Scholar API, focusing on cancer and radiation biology.

**Size**: 16,680 MCQs

**Format**: JSON

**Annotation**: Automated MCQ generation using semantic chunking and quality checks via GPT-4.1.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Calculating accuracy based on the proportion of correct answers out of total questions.

**Interpretation**: Higher accuracy indicates better model performance in understanding and answering domain-specific questions.

**Validation**: Models evaluated under three conditions: baseline, retrieval-augmented generation from chunks, and reasoning trace retrieval.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
