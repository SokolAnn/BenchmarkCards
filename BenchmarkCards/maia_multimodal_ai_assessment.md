# MAIA (Multimodal AI Assessment)

## 📊 Benchmark Details

**Name**: MAIA (Multimodal AI Assessment)

**Overview**: MAIA is a native-Italian benchmark that assesses the reasoning abilities of visual language models on videos, through two aligned tasks: a visual statement verification task and an open-ended visual question-answering task, evaluating models' consistency and understanding in a culturally representative context.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- Italian

**Similar Benchmarks**:
- AGQA
- MVBench

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the reasoning abilities of visual language models in video contexts, emphasizing the integration of understanding and generation tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Visual Statement Verification
- Open-Ended Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 100 short videos from YouTube Italy reflecting various aspects of Italian culture.

**Size**: 2,400 questions and 19,200 validated responses

**Format**: N/A

**Annotation**: Manually annotated by qualified native speakers, with semi-automatic validation checks.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Aggregate Accuracy

**Calculation**: Aggregate accuracy rewards models for consistent correct responses across both tasks.

**Interpretation**: Higher aggregate accuracy indicates better understanding and generation capabilities in VLMs.

**Baseline Results**: Not specified

**Validation**: Qualitative analysis and revision of the data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
