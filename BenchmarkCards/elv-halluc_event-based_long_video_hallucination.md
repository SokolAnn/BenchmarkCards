# ELV-Halluc (Event-based Long Video Hallucination)

## 📊 Benchmark Details

**Name**: ELV-Halluc (Event-based Long Video Hallucination)

**Overview**: ELV-Halluc is the first benchmark dedicated to long-video hallucination, enabling a systematic investigation of Semantic Aggregation Hallucinations (SAH) by quantifying semantic complexity through event-based videos and categorizing hallucination aspects.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VideoHallucer
- EventHallusion
- VidHalluc

**Resources**:
- [GitHub Repository](https://github.com/hlsv02/ELV-Halluc)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and analyze Semantic Aggregation Hallucinations in long videos and improve model robustness against hallucination.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The dataset scale is limited due to high annotation costs.

## 💾 Data

**Source**: 500 curated Event-by-Event videos from YouTube.

**Size**: 8K adversarial QA pairs

**Format**: JSON

**Annotation**: Semi-automated captioning followed by human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- SAH Ratio

**Calculation**: SAH Ratio = (OutAcc - InAcc) / (1 - InAcc) where OutAcc and InAcc denote the accuracy on out-of-video and in-video hallucination pairs, respectively.

**Interpretation**: Higher SAH Ratio indicates more severe Semantic Aggregation Hallucination.

**Validation**: Tested through experiments on various open-source and closed-source MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
