# LongV ALE (Vision-Audio-Language Event Benchmark Towards Time-Aware Omni-Modal Perception of Long Videos)

## 📊 Benchmark Details

**Name**: LongV ALE (Vision-Audio-Language Event Benchmark Towards Time-Aware Omni-Modal Perception of Long Videos)

**Overview**: LongV ALE is the first omni-modality long video benchmark, providing precise temporal boundaries and detailed relation-aware captions for 105K omni-modal events within 8.4K high-quality long videos. It aims to enhance cross-modal learning and fine-grained temporal understanding.

**Data Type**: omni-modal events with temporal boundaries and captions

**Domains**:
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://ttgeng233.github.io/LongVALE/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for fine-grained omni-modal video understanding.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Omni-modal Temporal Video Grounding
- Omni-modal Dense Video Captioning
- Omni-modal Segment Captioning

**Limitations**: N/A

## 💾 Data

**Source**: Derived from the ACA V-100M dataset, filtered for high-quality video content.

**Size**: 8,411 videos with 105,730 omni-modal events

**Format**: N/A

**Annotation**: Automated annotation pipeline for high-quality temporal boundaries and captions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Recall
- Mean Intersection over Union (mIoU)
- CIDEr
- METEOR

**Calculation**: Metrics calculated based on the comparison of predicted event boundaries and captions against ground truth values.

**Interpretation**: Higher scores indicate better performance in correctly identifying temporal boundaries and generating accurate captions.

**Validation**: Manual checks and corrections for the test set to ensure accuracy in annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: We used Gemini’s safety mechanism to block harmful responses and removed individual names to protect privacy.

**Data Licensing**: Data sourced from ACA V-100M under MIT license; annotations will be under CC BY-NC-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
