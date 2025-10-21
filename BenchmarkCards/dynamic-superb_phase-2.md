# Dynamic-SUPERB Phase-2

## 📊 Benchmark Details

**Name**: Dynamic-SUPERB Phase-2

**Overview**: Dynamic-SUPERB Phase-2 is an open and evolving benchmark for the comprehensive evaluation of instruction-based universal speech models, featuring a total of 180 tasks contributed by the global research community.

**Data Type**: question-answering pairs, audio samples

**Domains**:
- Natural Language Processing
- Music
- Audio

**Languages**:
- English

**Similar Benchmarks**:
- SUPERB
- MARBLE
- HEAR

**Resources**:
- [GitHub Repository](https://github.com/dynamic-superb/dynamic-superb)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for universal spoken language models across diverse tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Speech Recognition
- Emotion Recognition
- Music Classification
- Sound Event Detection
- Speaker Verification

**Limitations**: Despite its extensive task coverage, Dynamic-SUPERB Phase-2 lacks comprehensive speech generation tasks.

## 💾 Data

**Source**: Contributions from the global research community, incorporating tasks from various speech and audio datasets.

**Size**: 180 tasks

**Format**: N/A

**Annotation**: Crowdsourced and contributed by researchers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Evaluation by LLMs

**Metrics**:
- Accuracy
- LLM Classification

**Calculation**: Derived from comparison of model outputs against ground truth using automated evaluation pipelines.

**Interpretation**: Scores represent the percentage of task completions aligned with expected results, leveraging LLMs for final evaluations.

**Baseline Results**: Not explicitly stated, comparison to specific models like Whisper-LLaMA is included.

**Validation**: Continuous task incorporation based on community contributions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Dynamic-SUPERB Phase-2 inherits biases present in the contributed datasets.

**Data Licensing**: Tasks derived from datasets with licenses permitting remixing and redistribution, maintained on the official GitHub page.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
