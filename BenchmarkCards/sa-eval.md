# SA-Eval

## 📊 Benchmark Details

**Name**: SA-Eval

**Overview**: SA-Eval is a comprehensive benchmark designed to evaluate models on three tasks: audio event classification, audio captioning, and audio question answering, across two levels of difficulty (easy and hard), utilizing speech instructions and acoustic context.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VGGSound
- AudioSet
- FSD50K
- AudioCaps
- Clotho V2
- Clotho-AQA

**Resources**:
- [GitHub Repository](https://github.com/amphionspace/SA-Eval)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SA-Eval is to rigorously evaluate models' abilities to understand and respond to audio-related tasks and speech instructions under various acoustic conditions.

**Target Audience**:
- ML Researchers
- Audio Processing Specialists
- AI Developers

**Tasks**:
- Audio Classification
- Audio Captioning
- Question Answering

**Limitations**: SA-Eval currently focuses only on single-turn dialogues, limiting its ability to assess multi-turn complex dialogues.

## 💾 Data

**Source**: Derived from test sets of widely used datasets such as VGGSound, AudioSet, FSD50K, AudioCaps, Clotho V2, and Clotho-AQA.

**Size**: 4,915,318 pairs

**Format**: N/A

**Annotation**: Annotated through a combination of automated generation and human judgment.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- CIDEr
- SPICE

**Calculation**: Metrics are calculated based on model predictions compared to ground truth, with detailed scoring for accuracy and relevance.

**Interpretation**: Higher metric scores signify better performance of models in understanding and responding to audio tasks effectively.

**Baseline Results**: SOLLA serves as a baseline, with performance compared to other models evaluated on the SA-Eval dataset.

**Validation**: Validation is performed by employing both automated scoring metrics and human raters for the generated outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Incorrect audio comprehension can lead to misunderstandings in real-world applications.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
