# CrossVLAD

## 📊 Benchmark Details

**Name**: CrossVLAD

**Overview**: CrossVLAD is a new benchmark dataset carefully curated from MSCOCO with GPT-4-assisted annotations for systematically evaluating cross-task adversarial attacks on unified vision-language models (VLMs).

**Data Type**: image

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Gwill-Z/CRAFT)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation of cross-task adversarial attacks on unified vision-language models (VLMs).

**Target Audience**:
- ML Researchers
- Security Analysts

**Tasks**:
- Image Captioning
- Object Detection
- Region Categorization
- Object Localization

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the MSCOCO train2017 dataset.

**Size**: 3,000 images

**Format**: N/A

**Annotation**: GPT-4-assisted annotations for generating ground-truth captions.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- CTSR-4 (Cross-Task Success Rate-4)
- CTSR-3 (Cross-Task Success Rate-3)

**Calculation**: CTSR-4 is the percentage of examples that fool all four tasks, while CTSR-3 measures samples that fool at least three tasks.

**Interpretation**: Higher CTSR values indicate better cross-task attack performance.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for adversarial attacks to deceive vision-language models.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
