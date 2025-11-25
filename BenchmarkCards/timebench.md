# TIMEBench

## 📊 Benchmark Details

**Name**: TIMEBench

**Overview**: TIMEBench is a novel benchmark designed to evaluate temporal understanding in video models, comprehensively assessing the temporal reasoning capabilities across five dimensions: Dynamic, Reasoning, Duration, Location, and Order. It rigorously filters out potential data shortcuts to provide a more accurate measure.

**Data Type**: multiple-choice questions

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MVBench
- TempCompass
- AutoEval-Video
- Video-MME
- ActivityNet-QA

**Resources**:
- [Resource](https://arxiv.org/abs/2503.09994v2)

## 🎯 Purpose and Intended Users

**Goal**: To rigorously evaluate the performance of video-LLMs in understanding temporal aspects of videos.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: The benchmark utilizes data collected and filtered from diverse video datasets.

**Size**: 34,000 samples

**Format**: N/A

**Annotation**: Questions generated for both open-ended and multiple-choice formats.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy calculated based on the proportion of correct answers provided by models during evaluation.

**Interpretation**: Higher accuracy indicates better temporal reasoning capabilities in video-LLMs.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through extensive experimental comparisons with other benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
