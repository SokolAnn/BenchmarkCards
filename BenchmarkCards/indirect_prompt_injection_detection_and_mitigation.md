# Indirect Prompt Injection Detection and Mitigation

## 📊 Benchmark Details

**Name**: Indirect Prompt Injection Detection and Mitigation

**Overview**: This benchmark focuses on the detection and removal of indirect prompt injection attacks on large language models (LLMs). It assesses current models' performances against these attacks and explores methods for improving robustness.

**Data Type**: Text

**Domains**:
- NLP
- Cybersecurity

**Languages**:
- English

**Similar Benchmarks**:
- Inj-SQuAD
- Inj-TriviaQA

**Resources**:
- [Resource](arXiv:2502.16580v1)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the effectiveness of detection and removal methods for indirect prompt injection attacks.

**Target Audience**:
- AI researchers
- Cybersecurity professionals

**Tasks**:
- Evaluate the effectiveness of detection models
- Assess removal methods for injected instructions
- Establish benchmarks for prompt injection defenses

**Limitations**: None

**Out of Scope Uses**:
- Direct prompt injection attacks
- Generalized NLP tasks not related to prompt injections

## 💾 Data

**Source**: SQuAD and TriviaQA datasets, with additional crafted datasets.

**Size**: 900 samples for each benchmark (Inj-SQuAD and Inj-TriviaQA)

**Format**: Text

**Annotation**: Clean documents paired with injected instructions and probes.

## 🔬 Methodology

**Methods**:
- Detection using existing LLMs
- Training specialized detection models
- Segmentation removal method
- Extraction removal method

**Metrics**:
- True positive rate
- False positive rate
- Removal rate
- Attack success rate (ASR)

**Calculation**: Detection accuracy is calculated using true positive and false positive metrics; removal rate determines if injected instructions are absent post-processing.

**Interpretation**: Higher true positive rates indicate better detection, while lower false positive rates signify fewer misclassified documents.

**Validation**: Models are validated using crafted training datasets specific to indirect prompt injection.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy Risk
- Fairness Risk
- Robustness Risk

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No personal data was used. The crafted injected instructions are not harmful.

**Data Licensing**: Data from SQuAD and TriviaQA datasets is publicly available under the respective licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: All authors adhere to the ACM Code of Ethics and the ACL Code of Conduct.
