# WildSpeech-Bench

## 📊 Benchmark Details

**Name**: WildSpeech-Bench

**Overview**: WildSpeech-Bench is a comprehensive benchmark designed specifically for end-to-end Speech Large Language Models (SpeechLLMs). It evaluates models in realistic spoken interaction scenarios, focusing on diverse user intents and acoustic conditions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VoiceBench
- SD-Eval
- AIR-Bench

**Resources**:
- [GitHub Repository](https://github.com/Tencent/WildSpeech-Bench)
- [Resource](https://huggingface.co/datasets/tencent/WildSpeech-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and comprehensive evaluation framework for end-to-end speech LLMs in natural conversation scenarios, highlighting gaps in existing evaluation methodologies.

**Target Audience**:
- ML Researchers
- Speech Model Developers

**Tasks**:
- Speech Recognition
- Speech Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from real-world conversational data and augmented with diverse speech phenomena.

**Size**: 1,100 queries

**Format**: Raw text files

**Annotation**: Manually curated and validated by human experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Scores are averaged from multiple ASR evaluations to ensure reliability.

**Interpretation**: Scores reflect both linguistic accuracy and adherence to speech-specific criteria such as prosody and clarity.

**Baseline Results**: Average scores of evaluated models on various SpeechLLM tasks.

**Validation**: Manual curation and expert validation of query quality.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
