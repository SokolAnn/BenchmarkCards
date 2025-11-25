# TELEVAL (A Dynamic Benchmark Designed for Spoken Language Models in Chinese Interactive Scenarios)

## 📊 Benchmark Details

**Name**: TELEVAL (A Dynamic Benchmark Designed for Spoken Language Models in Chinese Interactive Scenarios)

**Overview**: TELEVAL is a dynamic benchmark specifically designed to evaluate Spoken Language Models’ effectiveness as conversational agents in realistic Chinese interactive settings. It categorizes capabilities into three evaluation dimensions: Explicit Semantics, Paralinguistic and Implicit Semantics, and System Abilities.

**Data Type**: text and audio outputs

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- AIR-Bench
- AudioBench
- Dynamic-SUPERB
- MMSU
- VoxEval
- WildSpeech-Bench

**Resources**:
- [GitHub Repository](https://github.com/Tele-AI/TELEVAL)

## 🎯 Purpose and Intended Users

**Goal**: To provide a user-centered evaluation framework that reflects user experiences and contributes to the development of dialogue-oriented spoken language models.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Dialogue Understanding
- Emotion Recognition
- Dialect Comprehension
- Response Generation
- Audio Event Detection
- Chit-chat

**Limitations**: TELEVAL primarily addresses only a subset of natural interaction scenarios in Chinese; models not included in the evaluation may be updated in future releases.

## 💾 Data

**Source**: TELEVAL consists of various tasks built from realistic conversational scenarios using both real human and synthetic speech.

**Size**: 40,000 samples

**Format**: text and audio

**Annotation**: Data synthesized from TTS systems and real human recordings.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- F1 Score
- Emotion Understanding Score
- Human-likeness Score

**Calculation**: Evaluation scores are averaged based on specific criteria tailored to each task.

**Interpretation**: High scores indicate strong capability in producing natural and appropriate responses in conversational contexts.

**Validation**: TELEVAL is validated with multiple evaluation methods, ensuring diverse metrics are utilized.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
