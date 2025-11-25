# EventSTR

## 📊 Benchmark Details

**Name**: EventSTR

**Overview**: EventSTR is a large-scale benchmark dataset for event stream based scene text recognition, containing 9,928 high-definition event samples involving both Chinese and English characters. It was constructed to address challenging factors such as low illumination, motion blur, and cluttered backgrounds.

**Data Type**: event samples

**Domains**:
- Computer Vision

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- MJ
- ST
- WordArt
- IC15

**Resources**:
- [GitHub Repository](https://github.com/Event-AHU/EventSTR)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a novel event-based scene text recognition task and to provide a benchmark dataset for evaluating various scene text recognition algorithms.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Scene Text Recognition

**Limitations**: The model heavily relies on a large-scale pre-trained LLM, which demands significant computational resources, making it less suitable for real-time applications.

## 💾 Data

**Source**: Event samples collected using the Prophesee HD event camera.

**Size**: 9,928 event samples

**Format**: N/A

**Annotation**: Annotated to identify all characters occurring in the scene, matching the text as it appears.

## 🔬 Methodology

**Methods**:
- Baseline comparisons with multiple state-of-the-art scene text recognition algorithms.

**Metrics**:
- BLEU-1
- BLEU-2
- BLEU-3
- BLEU-4

**Calculation**: BLEU scores are calculated by segmenting characters for Chinese text and by words (case-insensitive) for English text.

**Interpretation**: Higher BLEU scores indicate better performance in accurately recognizing text.

**Baseline Results**: SimC-ESTR achieved BLEU scores of 0.638, 0.583, 0.500, and 0.430 for BLEU-1, BLEU-2, BLEU-3, and BLEU-4 respectively.

**Validation**: Extensive experiments conducted on the EventSTR dataset and comparisons with other benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
