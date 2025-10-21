# ContextASR-Bench

## 📊 Benchmark Details

**Name**: ContextASR-Bench

**Overview**: ContextASR-Bench is a comprehensive benchmark designed to assess the linguistic competence of Automatic Speech Recognition (ASR) systems using corpora that feature numerous named entities across multiple domains. It encompasses up to 40,000 data entries with more than 300,000 named entities across over 10 domains.

**Data Type**: audio-text pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Education
- Entertainment
- Technical domains

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- THCHS-30
- Librispeech
- AISHELL-1
- Common Voice

**Resources**:
- [GitHub Repository](https://github.com/MrSupW/ContextASR-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the linguistic capabilities of ASR models in recognizing named entities across diverse domains.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Speech Recognition
- Named Entity Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Generated data from large audio language models leveraging named entity recognition datasets.

**Size**: 40,000 test pairs

**Format**: audio and transcription files

**Annotation**: Automatically generated using LLM-driven text generation and Zero-Shot TTS systems.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Word Error Rate (WER)
- Named Entity Word Error Rate (NE-WER)
- Named Entity False Negative Rate (NE-FNR)

**Calculation**: Metrics are calculated based on the comparison between transcription outputs and ground-truth text.

**Interpretation**: Lower WER, NE-WER, and NE-FNR indicate better ASR performance in recognizing speech and named entities.

**Validation**: The benchmark has been validated through comprehensive evaluations of existing ASR models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
