# VLT-MI (Visual Language Tracking with Multi-modal Interaction)

## 📊 Benchmark Details

**Name**: VLT-MI (Visual Language Tracking with Multi-modal Interaction)

**Overview**: VLT-MI introduces multi-round interaction into the Visual Language Tracking task for the first time. It generates diverse, multi-granularity texts for interaction and proposes a new interaction paradigm for improved tracking performance.

**Data Type**: multi-modal interaction data with bounding boxes and textual descriptions

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- OTB99_Lang
- LaSOT
- TNL2K
- MGIT

**Resources**:
- [Resource](https://arxiv.org/abs/2409.08887)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust framework for evaluating and enhancing the capabilities of Visual Language Tracking systems through multi-round, multi-modal interactions.

**Target Audience**:
- ML Researchers
- Computer Vision Practitioners
- Model Developers

**Tasks**:
- Object Tracking

**Limitations**: N/A

## 💾 Data

**Source**: Generated based on existing VLT benchmarks and DTLLM-VLT.

**Size**: 3,619 videos with a total of 6.60M frames

**Format**: N/A

**Annotation**: Automatically generated textual descriptions based on video content.

## 🔬 Methodology

**Methods**:
- Comparative experiments
- Multi-round interaction testing

**Metrics**:
- Precision
- Success Rate
- Average Multi-modal Interaction Number (AMI)
- Average Maximum Tracking Success Length (AMSL)

**Calculation**: Metrics are calculated based on tracking performance across different datasets, considering the number of interactions and tracking successes.

**Interpretation**: Higher metrics indicate better tracking performance and robustness of the tracker.

**Validation**: Performance validated through comparative analysis with existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination
- **Robustness**: Prompt injection attack

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
