# AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments

## 📊 Benchmark Details

**Name**: AgentClinic: a multimodal agent benchmark to evaluate AI in simulated clinical environments

**Overview**: AgentClinic introduces a multimodal agent benchmark for evaluating LLMs in simulated clinical environments that include patient interactions, multimodal data collection under incomplete information, and the usage of various tools.

**Data Type**: text and images

**Domains**:
- Healthcare

**Languages**:
- English
- Chinese
- Hindi
- Korean
- Spanish
- French
- Persian

**Similar Benchmarks**:
- MedQA
- MIMIC-IV
- PubMedQA
- MedMCQA

**Resources**:
- [Resource](https://agentclinic.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of AI language models in simulated clinical decision-making environments, assessing their abilities in the context of patient care.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- AI Developers

**Tasks**:
- Diagnostic Accuracy Evaluation
- Bias Impact Assessment
- Multimodal Data Interaction

**Limitations**: N/A

## 💾 Data

**Source**: Derived from clinical cases and real-world electronic health records.

**Size**: 260 patient cases from 9 medical specialties and 749 cases from 7 languages

**Format**: JSON

**Annotation**: Structured data created from clinical scenarios and validated through expert review.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Diagnostic Accuracy
- Patient Compliance
- Consultation Ratings

**Calculation**: Metrics are calculated based on the responsiveness and accuracy of the language models during simulated clinical interactions.

**Interpretation**: Higher scores indicate better diagnostic ability and engagement with patient interactions.

**Validation**: Results compared against ground truth diagnoses provided by clinical experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Potential Harm**: ['Inaccurate patient assessment', 'Disparities in treatment']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
