# FHIR-AgentBench

## 📊 Benchmark Details

**Name**: FHIR-AgentBench

**Overview**: FHIR-AgentBench is a benchmark that grounds 2,931 real-world clinical questions in the HL7 FHIR standard, systematically evaluating agentic frameworks in retrieving data and reasoning over it.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MIMICSQL
- EHRSQL
- ICUDATA
- MedAgentBench

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To provide a realistic benchmark for evaluating LLM agents in clinical EHR question answering.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: MIMIC-IV-FHIR patient records and questions from EHRSQL.

**Size**: 2,931 question–context–FHIR resource–answer pairs

**Format**: JSON

**Annotation**: Clinician-sourced questions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Precision
- Recall
- Answer Correctness

**Calculation**: Precision and recall based on the intersection of predicted and true resources. Answer correctness determined by comparison with ground-truth answers.

**Interpretation**: Higher precision and recall indicate effective retrieval. Answer correctness reflects the agent's ability to answer clinical questions accurately.

**Baseline Results**: N/A

**Validation**: Systematic evaluation across different agent architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Open Data Commons Open Database License v1.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
