# V ACT (Video Automatic Causal Testing)

## 📊 Benchmark Details

**Name**: V ACT (Video Automatic Causal Testing)

**Overview**: V ACT is an automated framework for modeling, evaluating, and measuring the causal understanding of video generation models (VGMs) in real-world scenarios. It combines causal analysis techniques with language model assistance to assess model behaviors without human intervention.

**Data Type**: causal testing scenarios and video data

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- VideoPhy
- PhyGenBench

**Resources**:
- [Resource](https://arxiv.org/abs/2503.06163)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to systematically evaluate the causal learning capabilities of video generation models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Causal Reasoning Evaluation
- Video Generation Assessment

**Limitations**: N/A

## 💾 Data

**Source**: 60 causal systems generated through automatic means, validated through crowd experiments.

**Size**: 60 causal systems

**Format**: JSON

**Annotation**: Automatically generated using a language model and validated through crowd-sourced human annotations.

## 🔬 Methodology

**Methods**:
- Automatic evaluation using language models
- Intervention experiments for causal testing

**Metrics**:
- Text Consistency
- Generation Consistency
- Rule Consistency

**Calculation**: Metrics are computed based on the ratio of correct outcomes produced by video generation models against the expected causal outcomes.

**Interpretation**: Higher scores indicate better causal understanding and alignment with real-world expectations.

**Baseline Results**: N/A

**Validation**: Validation through human comparison against automatically generated causal systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures ensured by not using identifiable personal data in the generated scenarios.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
