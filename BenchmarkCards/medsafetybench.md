# MedSafetyBench

## 📊 Benchmark Details

**Name**: MedSafetyBench

**Overview**: MedSafetyBench is the first benchmark dataset designed to measure the medical safety of large language models (LLMs), introduced to evaluate and improve their safety in medical contexts.

**Data Type**: medical safety demonstrations

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/AI4LIFE-GROUP/med-safety-bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the medical safety of large language models (LLMs) in medical settings.

**Target Audience**:
- Researchers
- Medical Professionals
- AI Developers

**Tasks**:
- Safety Evaluation
- Medical Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Developed from a combination of GPT-4 and Llama-2-7b-chat using adversarial techniques.

**Size**: 1,800 demonstrations

**Format**: JSON

**Annotation**: Generated manually and semi-automatically verified for quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- User studies with domain experts

**Metrics**:
- Harmfulness Score

**Calculation**: Calculated based on the willingness of LLMs to comply with harmful requests from the dataset.

**Interpretation**: A lower harmfulness score indicates a safer response.

**Validation**: User study with 25 medical experts validated the dataset's alignment with medical ethics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential medical harm from LLMs failing safety standards']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
