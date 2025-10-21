# Dense360-Bench

## 📊 Benchmark Details

**Name**: Dense360-Bench

**Overview**: Dense360-Bench is the first benchmark for evaluating and advancing research on MLLMs in omnidirectional captioning and grounding tasks.

**Data Type**: entity-grounded panoramic scene descriptions, entity-level captions, referring expressions

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate MLLMs on omnidirectional captioning and grounding tasks, facilitating a comprehensive framework for advancing visual-language understanding in panoramic settings.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Captioning
- Grounding

**Limitations**: N/A

## 💾 Data

**Source**: Automated generation from omnidirectional panoramas

**Size**: 160,000 panoramas, 5 million dense entity-level captions, 1 million unique referring expressions, 100,000 entity-grounded panoramic scene descriptions

**Format**: N/A

**Annotation**: Automated annotation with reliability-scored captions

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Mask Intersection over Union (IoU)
- Recall rate

**Calculation**: Evaluates grounding performance using mask IoU and captioning performance using recall of key phrases.

**Interpretation**: Higher recall and IoU indicate better MLLM understanding of omnidirectional panoramas.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
