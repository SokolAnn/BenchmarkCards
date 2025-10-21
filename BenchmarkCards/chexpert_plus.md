# CHEXPERT PLUS

## 📊 Benchmark Details

**Name**: CHEXPERT PLUS

**Overview**: CHEXPERT PLUS serves as a new collection of radiology data sources, made publicly available to enhance the scaling, performance, robustness, and fairness of models for all subsequent machine learning tasks in the field of radiology. It comprises 223,228 unique pairs of radiology reports and chest X-rays with accompanying demographic data and pathology labels.

**Data Type**: image and text pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://stanfordaimi.azurewebsites.net/datasets/5158c524-d3ab-4e02-96e9-6ee9efc110a1)
- [GitHub Repository](https://github.com/Stanford-AIMI/chexpert-plus)

## 🎯 Purpose and Intended Users

**Goal**: The goal of CHEXPERT PLUS is to provide a comprehensive dataset that enhances the development of AI models in radiology for improved performance, robustness, and fairness.

**Target Audience**:
- ML Researchers
- Medical Practitioners

**Tasks**:
- Radiology report generation
- Image classification
- Pathology detection

**Limitations**: The focus was put on collecting reports with detailed impression sections, at the cost of having lots of findings.

## 💾 Data

**Source**: Publicly released dataset combining chest X-ray images, radiology reports, and demographic data.

**Size**: 223,228 images and 187,711 reports

**Format**: DICOM and PNG for images; structured text for reports

**Annotation**: Annotations include pathology labels and RadGraph annotations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 scores were computed using labeled datasets to assess the performance of pathology detection.

**Interpretation**: Higher F1 scores indicate better performance in pathology detection tasks.

**Baseline Results**: F1 Score of 0.93 achieved using CheXbert-impression labels against the text-based test set.

**Validation**: The dataset underwent a rigorous de-identification process to ensure compliance with ethical standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Includes demographic data for improved fairness in model training.

**Potential Harm**: ['Potential bias based on demographics in downstream applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: A thorough de-identification process was performed to remove PHI from all reports.

**Data Licensing**: Dataset available for research purposes only, not for commercial use.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
