# MedAlign

## 📊 Benchmark Details

**Name**: MedAlign

**Overview**: MedAlign is a benchmark dataset of 983 natural language instructions for electronic health record (EHR) data, curated by clinicians, to address the documentation burdens faced by healthcare providers. It includes clinician-written responses and allows for evaluation of large language models (LLMs) on realistic text generation tasks.

**Data Type**: instruction-response pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedQA
- MMLU

**Resources**:
- [Resource](https://medalign.stanford.edu)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark dataset for evaluating LLMs on clinician-relevant tasks utilizing EHRs.

**Target Audience**:
- ML Researchers
- Healthcare Professionals

**Tasks**:
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Curated from natural language instructions provided by clinicians across various specialties paired with EHRs.

**Size**: 983 instructions

**Format**: JSON

**Annotation**: Clinicians wrote reference responses based on instruction-EHR pairs.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- COMET
- BERTScore

**Calculation**: Metrics are calculated based on the correctness of LLM responses compared to clinician-generated gold standard answers.

**Interpretation**: Higher scores indicate better performance in following clinician instructions and generating appropriate responses.

**Baseline Results**: GPT-4 (32k) achieved 60.1% accuracy in its responses.

**Validation**: Evaluated by clinicians ranking LLM responses against reference answers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Subset of data analyzed for potential biases in LLM performance across different demographic factors.

**Potential Harm**: LLM errors could lead to poor clinical decision-making and compromise patient safety.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was de-identified using a ‘hiding in plain sight’ protocol.

**Data Licensing**: Not Applicable

**Consent Procedures**: Patients provided consent for their medical records to be used for research.

**Compliance With Regulations**: Conducted in accordance with HIPAA and institutional review board guidelines.
