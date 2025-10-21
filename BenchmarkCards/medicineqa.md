# MedicineQA

## 📊 Benchmark Details

**Name**: MedicineQA

**Overview**: MedicineQA is a multi-round dialogue benchmark that simulates the real-world medication consultation scenario and requires LLMs to answer with retrieved evidence from the medicine database.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLMs in medication consultation scenarios.

**Target Audience**:
- ML Researchers
- Healthcare Professionals

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Crawled data from medical consultation websites, curated by physicians.

**Size**: 300 multi-round question-answering pairs

**Format**: N/A

**Annotation**: Curated and revised by a panel of board-certified physicians.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Evidence retrieval accuracy
- Elo rating

**Calculation**: The Elo rating system adjusts a model's rating based on the outcome of its performance compared to other models.

**Interpretation**: A higher Elo rating indicates better performance in the context of evidence retrieval and response generation.

**Baseline Results**: Comparisons made with other LLMs and commercial products in medical consultations.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
