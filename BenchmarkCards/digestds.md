# DigestDS

## 📊 Benchmark Details

**Name**: DigestDS

**Overview**: DigestDS is a novel dataset comprised of practical medical records from experienced experts in digestive system diseases, created to address the scarcity of high-quality clinical datasets for predicting Traditional Chinese Medicine (TCM) prescriptions.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- Chinese

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To develop a high-quality prescription dataset for predicting herbal prescriptions in Traditional Chinese Medicine using large language models.

**Target Audience**:
- Researchers
- Healthcare Professionals

**Tasks**:
- Prescription Prediction
- Dosage Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Clinical medical records collected from TCM specialists in digestive system disorders.

**Size**: 16,896 samples for training, 2,057 samples for testing

**Format**: N/A

**Annotation**: Data was cleaned and filtered for essential information by experts.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Low-rank adaptation (LoRA)

**Metrics**:
- Precision
- Recall
- F1 Score
- Normalized Mean Square Error (NMSE)

**Calculation**: Metrics are calculated based on herbal prediction and dosage accuracy compared to actual prescriptions.

**Interpretation**: Higher precision, recall, and F1 scores indicate better model performance in predicting herbs and dosages.

**Baseline Results**: TCM-FTP achieved an F1-score of 0.8031 and a NMSE of 0.0604.

**Validation**: Evaluated using expert assessments and quantitative comparison against baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Patient data was anonymized and irrelevant information was removed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
