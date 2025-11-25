# CoPESD (Co-Pilot of Endoscopic Submucosal Dissection)

## 📊 Benchmark Details

**Name**: CoPESD (Co-Pilot of Endoscopic Submucosal Dissection)

**Overview**: CoPESD is a multi-level surgical motion dataset designed for training large vision-language models as the co-pilot for Endoscopic Submucosal Dissection (ESD). This dataset contains detailed annotations across various levels of surgical motion granularity.

**Data Type**: images with motion annotations

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/gkw0010/CoPESD)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a comprehensive dataset for training LVLMs to support surgical automation and instruction-following during ESD.

**Target Audience**:
- ML Researchers
- Medical Practitioners
- Robotic Surgeons

**Tasks**:
- Motion Prediction
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: The dataset is constructed from over 35 hours of ESD videos collected using in-vivo porcine models utilizing both robot-assisted and conventional ESD techniques.

**Size**: 17,679 images with 32,699 bounding boxes and 88,395 multi-level motions

**Format**: N/A

**Annotation**: Annotated by trained medical professionals with a focus on multi-level surgical motion granularity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Mean Intersection over Union (mIoU)

**Calculation**: Metrics are calculated based on the performance of LVLMs in predicting surgical motions and their corresponding bounding boxes against ground truth.

**Interpretation**: Higher scores represent better performance in predicting the robotic motions required during surgical procedures.

**Validation**: The benchmark includes thorough evaluations using state-of-the-art LVLMs on a set of diverse surgical tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No confidential or sensitive data is included in the dataset.

**Data Licensing**: CC BY 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
