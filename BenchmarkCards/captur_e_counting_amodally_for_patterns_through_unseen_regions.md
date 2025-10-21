# CAPTUR E (Counting Amodally for Patterns Through Unseen REgions)

## 📊 Benchmark Details

**Name**: CAPTUR E (Counting Amodally for Patterns Through Unseen REgions)

**Overview**: CAPTUR E tests vision-language models (VLMs) on occlusion reasoning, pattern recognition, and counting of both visible and occluded objects through amodal counting, where models are prompted to count occluded objects by inferring how the pattern continues behind an occluder.

**Data Type**: image-object pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/atinpothiraj/CAPTURe)

## 🎯 Purpose and Intended Users

**Goal**: To measure VLMs' ability to form a robust world model and use that model for visual reasoning skills under occlusion.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Counting

**Limitations**: N/A

## 💾 Data

**Source**: FSC-147 dataset filtered for images containing identifiable and regular patterns of objects.

**Size**: 924 real images, 1250 synthetic images

**Format**: N/A

**Annotation**: Manual annotations through filtering and overlaying occluding boxes.

## 🔬 Methodology

**Methods**:
- Evaluation of models on specific counting prompts
- Use of oracle information to test model performance

**Metrics**:
- sMAPE

**Calculation**: sMAPE = 100 * (1/n) * Σ(|yi - ŷi| / (|yi| + |ŷi|))

**Interpretation**: Lower sMAPE values indicate better performance in counting accurately.

**Baseline Results**: Humans completed the task with an sMAPE of 3.79% on CAPTUR Ereal and 0.92% on CAPTUR Esynthetic.

**Validation**: Manual validation of model outputs and oracle experiments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
