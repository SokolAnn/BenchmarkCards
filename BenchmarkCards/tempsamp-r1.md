# TempSamp-R1

## 📊 Benchmark Details

**Name**: TempSamp-R1

**Overview**: This paper introduces TempSamp-R1, a reinforcement fine-tuning framework designed to improve the effectiveness of adapting multimodal large language models (MLLMs) to video temporal grounding tasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Charades-STA
- ActivityNet Captions
- QVHighlights

**Resources**:
- [GitHub Repository](https://github.com/HVision-NKU/TempSamp-R1)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the capability of MLLMs in temporal video grounding and highlight detection tasks by integrating off-policy guidance with a new reinforcement fine-tuning framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Temporal Grounding
- Highlight Detection

**Limitations**: The framework currently relies on the availability of high-quality off-policy supervision (e.g., ground-truth timestamps).

## 💾 Data

**Source**: Charades-STA, ActivityNet Captions, QVHighlights datasets.

**Size**: 12,400 examples (Charades-STA), 37,421 examples (ActivityNet Captions), 10,148 examples (QVHighlights)

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- A/B Testing

**Metrics**:
- Recall@1
- mAP

**Calculation**: Metrics are calculated based on Intersection-over-Union (IoU) thresholds.

**Interpretation**: Higher values of Recall@1 and mAP indicate better temporal grounding performance.

**Baseline Results**: TempSamp-R1 outperforms GRPO-based baselines on all evaluated datasets.

**Validation**: Results are validated against established benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Non-commercial use license for Charades-STA; Attribution-NonCommercial-ShareAlike 4.0 International for QVHighlights.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
