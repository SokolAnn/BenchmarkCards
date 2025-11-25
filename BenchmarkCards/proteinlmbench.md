# ProteinLMBench

## 📊 Benchmark Details

**Name**: ProteinLMBench

**Overview**: ProteinLMBench is the first benchmark dataset consisting of 944 manually verified multiple-choice questions for assessing the protein understanding capabilities of LLMs. It incorporates protein-related details and sequences in multiple languages, establishing a new standard for evaluating LLMs’ abilities in protein comprehension.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing
- Biotechnology

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/datasets/tsynbio/ProteinLMBench)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the LLMs’ proficiency to comprehend protein sequences.

**Target Audience**:
- ML Researchers
- Biotechnology Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Manually verified multiple-choice questions from various protein-related topics.

**Size**: 944 questions

**Format**: JSON

**Annotation**: Manually verified and annotated for clarity and correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the proportion of correctly answered questions.

**Interpretation**: A higher accuracy score indicates better comprehension of protein sequences by LLMs.

**Baseline Results**: InternLM2-7B model achieved an accuracy of 62.18% on the benchmark.

**Validation**: Questions were validated through a two-round verification process involving human annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Apache License 2.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
