# HalluDial

## 📊 Benchmark Details

**Name**: HalluDial

**Overview**: HalluDial is the first comprehensive large-scale benchmark for automatic dialogue-level hallucination evaluation, including both spontaneous and induced hallucination scenarios, covering factuality and faithfulness hallucinations.

**Data Type**: Dialogue

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HaluEval
- TruthfulQA

**Resources**:
- [GitHub Repository](https://github.com/FlagOpen/HalluDial)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate hallucinations of large language models in information-seeking dialogues.

**Target Audience**:
- Researchers
- Practitioners in NLP

**Tasks**:
- Hallucination detection
- Hallucination localization
- Providing rationales for hallucinations

**Limitations**: N/A

**Out of Scope Uses**:
- Applications outside of evaluation metrics for hallucination

## 💾 Data

**Source**: Derived from an information-seeking dialogue dataset (Dziri et al., 2022)

**Size**: 146,856 samples

**Format**: Dialogue-based responses

**Annotation**: Automatic hallucination annotation using GPT-4

## 🔬 Methodology

**Methods**:
- Two-step pipeline for spontaneous hallucination: diverse dialogue sampling and automatic annotation
- Induced hallucination using task-specific instructions to guide LLMs

**Metrics**:
- Hallucination detection accuracy
- Hallucination localization capabilities
- Quality of rationales provided for hallucinations

**Calculation**: N/A

**Interpretation**: Values used to measure how well models detect and localize hallucinations compared to ground truth annotations.

**Baseline Results**: Baseline performance results presented for HalluJudge and other LLMs in hallucination detection.

**Validation**: Meta-evaluation of LLMs' hallucination detection abilities using HalluDial dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Hallucination detection challenges
- Potential biases in generated responses
- Misinformation risks in dialogue contexts

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Risk of generating misleading responses that affect user trust.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
