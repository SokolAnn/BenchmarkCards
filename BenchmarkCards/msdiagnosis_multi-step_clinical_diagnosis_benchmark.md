# MSDiagnosis (Multi-Step Clinical Diagnosis Benchmark)

## 📊 Benchmark Details

**Name**: MSDiagnosis (Multi-Step Clinical Diagnosis Benchmark)

**Overview**: MSDiagnosis is a benchmark for evaluating large language models in multi-step clinical diagnosis, consisting of 2,225 cases that cover tasks such as primary diagnosis, differential diagnosis, and final diagnosis.

**Data Type**: medical case records

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Similar Benchmarks**:
- DDx-basic
- DDx-advanced
- CMExam
- AgentClinic-MedQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multi-step diagnostic abilities of large language models in alignment with clinical practice.

**Target Audience**:
- Medical Researchers
- AI Researchers

**Tasks**:
- Primary Diagnosis
- Differential Diagnosis
- Final Diagnosis

**Limitations**: Due to limited data sources, the dataset exhibits an uneven distribution across different departments.

## 💾 Data

**Source**: Chinese medical websites

**Size**: 2,225 medical records

**Format**: N/A

**Annotation**: Manual annotation by a professional medical team

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- BLEU Score
- ROUGE-L
- Macro Recall

**Calculation**: Metrics are calculated based on the comparison between generated diagnoses and reference diagnoses in the dataset.

**Interpretation**: Higher scores indicate better alignment with the clinical diagnosis tasks.

**Baseline Results**: Ours: F1 of 38.76% for Left clavicle fracture and other metrics as per results in Table 3.

**Validation**: Validated against expert medical evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data was anonymized and no protected health information is present.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
