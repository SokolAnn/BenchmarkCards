# IOR-Bench (Intelligent Outpatient Referral Benchmark)

## 📊 Benchmark Details

**Name**: IOR-Bench (Intelligent Outpatient Referral Benchmark)

**Overview**: IOR-Bench provides a systematic framework for assessing the performance of models in outpatient referral scenarios through static and dynamic evaluation methods in the context of healthcare.

**Data Type**: static classification and dynamic dialogue data

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- MedBench (Medical Benchmark)
- CMB (Comprehensive Medical Benchmark)

**Resources**:
- [GitHub Repository](https://github.com/FreedomIntelligence/IOR-Bench.git)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to evaluate large language models' capabilities in outpatient referral tasks using a dual framework for static and dynamic evaluations.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Static Classification
- Dynamic Questioning

**Limitations**: N/A

## 💾 Data

**Source**: The IOR dataset comprises real patient interactions sourced from hospitals in China, with careful ethical considerations and privacy compliance during data collection.

**Size**: 1,476 cases

**Format**: CSV

**Annotation**: Data was manually annotated by medical professionals following strict guidelines, ensuring accuracy and compliance.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated by comparing the predicted department to the ground truth annotated by medical professionals.

**Interpretation**: Higher accuracy indicates better model performance in correctly directing patients to the appropriate departments during outpatient referrals.

**Baseline Results**: BERT-Base-Chinese achieved an accuracy of 76.00% in static evaluation tasks, with human doctors achieving up to 87.24%.

**Validation**: The framework has been validated through both automated methods and human evaluations with participating medical staff.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The benchmark allows for demographic breakdowns based on patient data within the dataset.

**Potential Harm**: ['Misleading medical recommendations due to inaccurate model predictions.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All patient data has been anonymized and de-identified to protect privacy.

**Data Licensing**: Not Applicable

**Consent Procedures**: The study received ethical approval from the relevant committees before conducting data collection.

**Compliance With Regulations**: Not Applicable
