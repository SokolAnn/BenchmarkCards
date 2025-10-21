# NOVA: A Benchmark for Anomaly Localization and Clinical Reasoning in Brain MRI

## 📊 Benchmark Details

**Name**: NOVA: A Benchmark for Anomaly Localization and Clinical Reasoning in Brain MRI

**Overview**: NOVA establishes a new benchmark for evaluating, detecting, and reasoning on unexpected abnormalities in clinical brain MRI. It includes ~900 brain MRI scans spanning 281 rare and diverse pathologies, with rich clinical narratives and expert annotations for anomaly localization, visual captioning, and diagnostic reasoning.

**Data Type**: brain MRI scans

**Domains**:
- Healthcare

**Languages**:
- N/A

**Similar Benchmarks**:
- BraTS
- ATLAS
- ISLES

**Resources**:
- [Resource](https://huggingface.co/datasets/Ano-2090/Nova)

## 🎯 Purpose and Intended Users

**Goal**: To establish a rigorous testbed for advancing models capable of detecting, localizing, and reasoning about unknown anomalies in medical imaging.

**Target Audience**:
- ML Researchers
- Healthcare Professionals
- Model Developers

**Tasks**:
- Anomaly Localization
- Image Captioning
- Diagnostic Reasoning

**Limitations**: The dataset is sourced from a European radiology teaching repository, which may introduce geographic or demographic biases.

## 💾 Data

**Source**: Cases from Eurorad, a peer-reviewed educational platform.

**Size**: 906 brain MRI scans

**Format**: PNG images and CSV metadata files

**Annotation**: Annotated by at least two radiologists with bounding boxes and clinical narratives.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Average Precision (mAP)
- F1 Score
- BLEU Score

**Calculation**: Metrics are computed based on standard performance evaluation techniques in object detection and text generation.

**Interpretation**: Higher scores indicate better performance in anomaly localization, image captioning, and diagnostic reasoning.

**Baseline Results**: Baseline results showed significant performance drops compared to standard image benchmarks.

**Validation**: Evaluation conducted in a zero-shot setting, requiring models to generalize without prior exposure.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset complies with the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license.

**Data Licensing**: Creative Commons Attribution-NonCommercial-ShareAlike 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
