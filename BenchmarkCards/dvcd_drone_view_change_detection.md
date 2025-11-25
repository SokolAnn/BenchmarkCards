# DVCD (Drone View Change Detection)

## 📊 Benchmark Details

**Name**: DVCD (Drone View Change Detection)

**Overview**: The DVCD dataset is a drone-based change detection dataset consisting of 13,800 image pairs of building changes in diverse urban and rural scenarios collected from urban areas in Guangdong Province, reflecting typical changes such as new construction, demolition, and expansion during rapid urban development. It includes fine-grained textual descriptions to guide the model to focus on semantic change features.

**Data Type**: image pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- WHU-CD
- DSIFN-CD
- CDD

**Resources**:
- [GitHub Repository](https://github.com/Yu-Zhouz/SegChange-R1)

## 🎯 Purpose and Intended Users

**Goal**: The purpose of the DVCD dataset is to enhance the model's understanding of semantic changes and explore the role of text in building change detection.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Change Detection

**Limitations**: N/A

## 💾 Data

**Source**: Drone orthophotos collected from urban areas in Guangdong Province.

**Size**: 13,800 image pairs

**Format**: N/A

**Annotation**: Fine-grained textual descriptions integrated with image data.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- F1 Score
- IoU
- Overall Accuracy

**Calculation**: Metrics are calculated based on the comparison of predicted segmentation masks with ground truth.

**Interpretation**: Higher F1 Score, IoU, and Overall Accuracy indicate better change detection performance.

**Baseline Results**: SegChange-R1 demonstrated superior performance with F1 Score: 0.988 on the DVCD dataset.

**Validation**: Performance validated through comparative experiments across existing datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
