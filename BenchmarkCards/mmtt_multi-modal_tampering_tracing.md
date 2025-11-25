# MMTT (Multi-Modal Tampering Tracing)

## 📊 Benchmark Details

**Name**: MMTT (Multi-Modal Tampering Tracing)

**Overview**: The MMTT dataset focuses on facial images manipulated using deepfake techniques, comprising 128,303 image-text pairs to enhance forgery localization and interpretability.

**Data Type**: image-text pairs

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2412.19685)

## 🎯 Purpose and Intended Users

**Goal**: To develop interpretable image forgery localization and enhance the interpretability of forgery analysis through detailed annotations.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Forgery Localization
- Forgery Interpretation

**Limitations**: N/A

## 💾 Data

**Source**: CelebA-HQ and Flickr-Faces-HQ datasets.

**Size**: 128,303 samples

**Format**: image and text

**Annotation**: Human annotation with detailed descriptions of manipulated regions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- CIDEr
- BLEU
- IoU

**Calculation**: Metrics are calculated based on the predictions of the forged localization and interpretive reports generated.

**Interpretation**: Higher scores in metrics indicate better generation of interpretive text related to forgery localization.

**Validation**: Dataset is validated through rigorous human annotation processes and quality control.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
