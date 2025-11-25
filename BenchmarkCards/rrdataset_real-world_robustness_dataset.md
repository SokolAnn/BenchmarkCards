# RRDataset (Real-World Robustness Dataset)

## 📊 Benchmark Details

**Name**: RRDataset (Real-World Robustness Dataset)

**Overview**: RRDataset is introduced for comprehensive evaluation of AI-generated image detection models across various real-world scenarios, internet transmission robustness, and re-digitization aspects.

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- GenImage
- Fake2M
- WildFake
- Chameleon

**Resources**:
- [Resource](https://zenodo.org/records/14963880)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark the performance of AI-generated image detection methods under challenging real-world conditions.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Image Detection

**Limitations**: N/A

## 💾 Data

**Source**: Images collected from diverse scenarios, including War & Conflict, Disasters & Accidents, Political & Social Events, Medical & Public Health, Culture & Religion, and Labor & Production.

**Size**: 12,000 images

**Format**: JPEG

**Annotation**: Manually annotated based on image content and categorization.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the detection accuracy of real and AI-generated images.

**Interpretation**: Higher accuracy indicates better detection capability under varied conditions.

**Baseline Results**: The best accuracy achieved was 89.59%.

**Validation**: Evaluated across multiple transmission and re-digitization conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
