# DFIR-Metric (Digital Forensics and Incident Response Metric)

## 📊 Benchmark Details

**Name**: DFIR-Metric (Digital Forensics and Incident Response Metric)

**Overview**: DFIR-Metric is a benchmark with three components: Knowledge Assessment with 700 expert-reviewed multiple-choice questions, Realistic Forensic Challenges with 150 CTF-style tasks, and Practical Analysis with 500 disk and memory forensics cases from the NIST Computer Forensics Tool Testing Program.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GLUE
- SQuAD

**Resources**:
- [GitHub Repository](https://github.com/DFIR-Metric)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the theoretical knowledge and practical proficiency of LLMs in the domain of Digital Forensics and Incident Response.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Multiple-Choice Question Evaluation
- CTF-style Forensic Challenges
- NIST String Search Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Expert-reviewed questions sourced from industry-standard certifications and official documentation, forensic challenges based on real-world scenarios, and practical cases derived from the NIST CFTT.

**Size**: 700 multiple-choice questions, 150 CTF-style challenges, 500 analysis cases

**Format**: JSON, CSV

**Annotation**: Human-verified and expert-reviewed multiple-choice questions and solutions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Task Understanding Score (TUS)
- Confidence Index
- Reliability Score

**Calculation**: Metrics are calculated by assessing task performance across multiple attempts to ensure reliability.

**Interpretation**: High scores indicate better understanding and accuracy in completing forensic tasks.

**Baseline Results**: Highest scores achieved by models like GPT-4.1 in the DFIR context.

**Validation**: The benchmark's components were validated through repeated testing by multiple evaluators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All questions derived from publicly accessible sources with measures taken to avoid direct association with certification material.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
