# MedOmni-45°: A Safety–Performance Benchmark for Reasoning-Oriented LLMs in Medicine

## 📊 Benchmark Details

**Name**: MedOmni-45°: A Safety–Performance Benchmark for Reasoning-Oriented LLMs in Medicine

**Overview**: A benchmark and evaluation workflow explicitly designed to quantify the safety–performance trade-off in LLMs under manipulative hint conditions, containing 1,804 reasoning-focused medical questions across six clinical specialties and three task types.

**Data Type**: multiple-choice medical questions

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MedMCQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To quantify the safety–performance trade-off in reasoning-oriented medical tasks for large language models.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- AI Developers

**Tasks**:
- Medical Question Answering
- Clinical Simulation
- Medical Calculation

**Limitations**: N/A

## 💾 Data

**Source**: Self-constructed dataset based on six medical specialties and 500 items from MedMCQA.

**Size**: 1,804 questions

**Format**: N/A

**Annotation**: Questions are manually verified by medical annotators to ensure accuracy and clinical validity.

## 🔬 Methodology

**Methods**:
- Evaluation across multiple LLMs
- Performance metrics calculation

**Metrics**:
- Accuracy
- CoT-Faithfulness
- Anti-Sycophancy

**Calculation**: Metrics are calculated based on model responses to medical questions under various manipulative hint conditions.

**Interpretation**: Scores across metrics indicate the balance between safety and performance.

**Validation**: Evaluated against baseline standard medical QA benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Potential safety risks from LLMs exhibiting sycophantic tendencies.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
