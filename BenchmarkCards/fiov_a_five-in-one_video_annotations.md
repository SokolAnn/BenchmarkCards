# FIOV A (Five-In-One Video Annotations)

## 📊 Benchmark Details

**Name**: FIOV A (Five-In-One Video Annotations)

**Overview**: FIOV A is a human-centric benchmark designed to evaluate the video captioning capabilities of large vision-language models (LVLMs). It consists of 3,002 real-world videos, each annotated independently by five annotators, enabling the modeling of semantic diversity and inter-subjective agreement.

**Data Type**: video-caption pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huuuuusy.github.io/fiova/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standard evaluation framework for assessing the alignment of LVLM-generated video captions with human understanding.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Video Captioning

**Limitations**: N/A

## 💾 Data

**Source**: A collection of 3,002 videos annotated by five human annotators each, capturing diverse real-world scenarios.

**Size**: 3,002 videos

**Format**: N/A

**Annotation**: Annotated independently by five annotators focusing on visual content only.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Event-level cognitive evaluation

**Metrics**:
- BLEU
- METEOR
- GLEU
- F1
- Recall
- Precision

**Calculation**: Metrics were calculated using traditional text-matching methods as well as through a new cognitively weighted event-level metric (FIOV A-DQ).

**Interpretation**: Higher scores indicate better alignment with human-generated descriptions.

**Baseline Results**: N/A

**Validation**: Extensive human evaluation with expert rankings and cognitive validation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential for the amplification of biases present in training data and risks associated with content hallucination.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Videos are sourced from copyright-compliant public platforms.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
