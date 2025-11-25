# FD-Bench: A Full-Duplex Benchmarking Pipeline Designed for Full Duplex Spoken Dialogue Systems

## 📊 Benchmark Details

**Name**: FD-Bench: A Full-Duplex Benchmarking Pipeline Designed for Full Duplex Spoken Dialogue Systems

**Overview**: We present a comprehensive FD benchmarking pipeline utilizing LLMs, TTS, and ASR to address the gap in evaluating Full-Duplex Spoken Dialogue Systems (FDSDS) during user interruptions.

**Data Type**: simulated conversations with interruptions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/pengyizhou/FD-Bench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide a comprehensive evaluation method for FDSDS focusing on their capabilities to handle user interruptions and maintain robustness.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Dialogue Management
- Robustness Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Simulated speech conversations generated using LLMs and TTS systems.

**Size**: 40 hours of generated speech

**Format**: Raw audio (24KHz pcm)

**Annotation**: Automatically generated based on simulated dialogues.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Word-Error-Rate (WER)
- Success Replies Rate (SRR)
- Success Interrupts Rate (SIR)
- Early Interrupt Rate (EIR)
- Conditioned Perplexity (C-PPL)

**Calculation**: Metrics are calculated using outputs from the ASR systems and evaluation from LLM scoring.

**Interpretation**: High scores in SRR and SIR indicate better handling of interruptions by the systems.

**Baseline Results**: Results reported for three models: Moshi, Freeze-omni, and VITA-1.5 under various interruption types.

**Validation**: Evaluated in a server-client architecture simulating real-time interactions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Evasion attack, Data poisoning
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
