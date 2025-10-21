# ˙ıFinder

## 📊 Benchmark Details

**Name**: ˙ıFinder

**Overview**: ˙ıFinder is a structured semantic grounding framework designed for zero-shot analysis of dash-cam videos, improving reasoning accuracy and transparency in video-based driving scenarios.

**Data Type**: multimodal

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MM-AU (Multi-Modal Accident Video Understanding)
- SUTD (Traffic Question Answering)
- LingoQA
- Nexar

**Resources**:
- [Resource](https://arxiv.org/abs/2509.19552)

## 🎯 Purpose and Intended Users

**Goal**: To provide accurate and interpretable reasoning for dash-cam videos using structured visual information.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Safety Analysts
- Model Developers

**Tasks**:
- Accident Reasoning
- Traffic Event Analysis
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Public dash-cam video datasets for evaluation.

**Size**: 1,953 ego-view accident videos in MM-AU dataset; 4,111 real-world driving videos in SUTD dataset

**Format**: JSON

**Annotation**: Automatically generated using pre-trained vision models.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Performance calculated based on correct predictions across multiple driving scenarios.

**Interpretation**: Higher accuracy indicates better reasoning by the model over accident scenarios.

**Validation**: Evaluated on four public benchmarks: MM-AU, SUTD, LingoQA, and Nexar.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Output bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
