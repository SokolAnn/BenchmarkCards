# CableInspect-AD (An Expert-Annotated Anomaly Detection Dataset)

## 📊 Benchmark Details

**Name**: CableInspect-AD (An Expert-Annotated Anomaly Detection Dataset)

**Overview**: CableInspect-AD is a high-quality, publicly available dataset created and annotated by domain experts for visual anomaly detection in power line cables, featuring 4,798 high-resolution images with 6,023 annotated anomalies across three types of cables.

**Data Type**: image

**Domains**:
- Robotics

**Languages**:
- N/A

**Similar Benchmarks**:
- MVTec AD
- VisA
- MVTec LOCO AD

**Resources**:
- [Resource](https://mila-iqia.github.io/cableinspect-ad/)
- [GitHub Repository](https://github.com/mila-iqia/cableinspect-ad-code)

## 🎯 Purpose and Intended Users

**Goal**: To enable research on industrial anomaly detection for robotic power line cable inspection.

**Target Audience**:
- ML Researchers
- Industrial Practitioners
- Domain Experts

**Tasks**:
- Anomaly Detection
- Anomaly Segmentation

**Limitations**: The dataset may not encompass every possible anomaly found on a cable in real-world settings due to inherent complexity.

## 💾 Data

**Source**: Images acquired from powered line cables with a focus on identifying various types of anomalies.

**Size**: 4,798 images

**Format**: COCO format

**Annotation**: Annotations are provided at the image level with bounding boxes, types, and grades for anomalies.

## 🔬 Methodology

**Methods**:
- k-fold cross-validation
- Threshold-dependent evaluation metrics

**Metrics**:
- F1 Score
- AUROC
- AUPR

**Calculation**: Metrics are calculated based on model predictions during cross-validation.

**Interpretation**: Higher F1 Score indicates better model performance in detecting anomalies.

**Validation**: Evaluation is conducted using k-fold cross-validation strategy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: The dataset includes various grades of anomaly severities.

**Potential Harm**: Deployment of underperforming models may miss critical anomalies, compromising safety.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
