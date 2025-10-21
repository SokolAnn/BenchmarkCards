# CliMedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models in Clinical Scenarios

## 📊 Benchmark Details

**Name**: CliMedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models in Clinical Scenarios

**Overview**: CliMedBench is a comprehensive benchmark with 14 expert-guided core clinical scenarios designed to assess the medical ability of LLMs across seven dimensions, comprising 33,735 questions derived from real-world medical reports of top-tier tertiary hospitals and authentic examination exercises.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MedQA
- MedMCQA
- CMExam
- CMB
- MLEC-QA
- MedBench

**Resources**:
- [GitHub Repository](https://github.com/Optifine-TAT/CliMedBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of CliMedBench is to provide a standardized evaluation benchmark to scrutinize the capabilities and limitations of medical LLMs.

**Target Audience**:
- ML Researchers
- Medical Practitioners

**Tasks**:
- Clinical Question Answering
- Knowledge Application
- Reasoning
- Information Retrieval
- Summarization
- Hallucination Detection
- Toxicity Assessment

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is derived from real-world Electronic Health Records (EHRs) of top-tier tertiary hospitals in China, supplemented with examination exercises and clinical consultation data.

**Size**: 33,735 questions

**Format**: N/A

**Annotation**: Expert-guided annotation by medical professionals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Kendall's Tau
- ROUGE-1

**Calculation**: Metrics are calculated based on LLMs' responses to questions in various scenarios.

**Interpretation**: Higher scores indicate better performance in clinical reasoning and knowledge application.

**Validation**: The benchmark was validated through expert assessments and iterative feedback from medical professionals.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All EHRs were doubly de-identified to ensure patient privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: The project was conducted in collaboration with relevant medical centers with proper approval.

**Compliance With Regulations**: Not Applicable
