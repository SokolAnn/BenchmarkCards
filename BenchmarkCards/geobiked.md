# GeoBiked

## 📊 Benchmark Details

**Name**: GeoBiked

**Overview**: GeoBiked is a dataset designed to advance Deep Generative Models (DGMs) in engineering design, featuring 4,355 bicycle images annotated with structural and technical features, aimed at enabling researchers to automate data labeling and perform generative tasks.

**Data Type**: image

**Domains**:
- Engineering Design
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- BIKED

**Resources**:
- [GitHub Repository](https://github.com/Phillip-M97/GeoBIKED)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundation to apply DGMs in engineering design processes and facilitate the experimentation of developers with domain-specific applications.

**Target Audience**:
- Researchers
- Practitioners
- Engineers

**Tasks**:
- Image Generation
- Data Annotation

**Limitations**: N/A

## 💾 Data

**Source**: Composed of bicycle images extracted and curated from BIKED dataset, with additional structural annotations.

**Size**: 4,355 images

**Format**: image files

**Annotation**: Annotated with geometric features and technical descriptors.

## 🔬 Methodology

**Methods**:
- Automated Annotation with Vision-Language Models
- Geometric Feature Detection

**Metrics**:
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

**Calculation**: Calculated as pixel-wise distances between predicted locations and ground-truth locations.

**Interpretation**: Lower MAE and MSE values indicate better accuracy in geometric point predictions.

**Baseline Results**: N/A

**Validation**: Validated through experiments comparing annotations from a subset of the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
