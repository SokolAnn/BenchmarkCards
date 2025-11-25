# MedChain

## 📊 Benchmark Details

**Name**: MedChain

**Overview**: MedChain is a comprehensive clinical decision-making benchmark designed to simulate real-world scenarios in healthcare, comprising 12,163 clinical cases that cover five key stages of clinical workflow.

**Data Type**: clinical cases and medical images

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MedQA
- PubMedQA
- MedMCQA

**Resources**:
- [GitHub Repository](https://github.com/ljwztc/MedChain)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of LLM-based agents in clinical decision-making by providing a realistic benchmark that incorporates personalization, interactivity, and sequentiality.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- AI Developers

**Tasks**:
- Diagnosis
- Treatment Planning
- History Taking
- Specialty Referral

**Limitations**: The dataset derived from a single source may limit generalizability; future work aims to incorporate diverse data sources.

## 💾 Data

**Source**: Chinese medical website 'iiYi', which provides validated clinical cases.

**Size**: 12,163 clinical cases

**Format**: N/A

**Annotation**: Validated by professional physicians and de-identified to ensure patient privacy.

## 🔬 Methodology

**Methods**:
- Multiple-agent collaboration
- Feedback mechanisms
- Dynamic information gathering

**Metrics**:
- Accuracy
- Intersection over Union (IoU)

**Calculation**: Scores are based on the correctness of decisions through a multi-stage evaluation process.

**Interpretation**: Higher scores indicate better performance in clinical decision-making tasks.

**Baseline Results**: MedChain-Agent framework demonstrates significant improvements over existing approaches.

**Validation**: Performed by a panel of senior physicians ensuring data integrity and clinical relevance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data has been de-identified to protect patient privacy.

**Data Licensing**: Formal permission obtained for data use from the site administrators.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
