# ImageCLEFmedical 2023

## 📊 Benchmark Details

**Name**: ImageCLEFmedical 2023

**Overview**: ImageCLEFmedical 2023 is a dataset designed for Diagnostic Captioning (DC), containing 71,355 medical images with gold tags and diagnostic captions, aimed at providing automated diagnostic reports from medical images.

**Data Type**: image-caption pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/nlpaueb/dmmcs)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for developing and evaluating Diagnostic Captioning systems that generate medical reports from images.

**Target Audience**:
- ML Researchers
- Medical Professionals
- Data Scientists

**Tasks**:
- Image Captioning

**Limitations**: The dataset is limited to specific conditions, regions, and language (English).

## 💾 Data

**Source**: The dataset consists of medical images, gold tags, and gold diagnostic captions sourced from the ImageCLEF and MIMIC-CXR projects.

**Size**: 71,355 images

**Format**: N/A

**Annotation**: Gold tags and captions provided with the images.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- BLEU
- BLEURT

**Calculation**: Performance metrics are calculated based on comparisons between generated captions and gold captions.

**Interpretation**: Higher BLEU and BLEURT scores indicate better alignment with gold captions.

**Baseline Results**: Standard beam search decoding performance serves as baseline comparisons.

**Validation**: The dataset was split into training, validation, and test sets (75%-10%-15% split).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Concerns regarding biomedical data privacy due to the sensitive nature of medical data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
