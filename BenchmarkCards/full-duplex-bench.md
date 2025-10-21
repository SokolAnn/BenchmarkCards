# Full-Duplex-Bench

## 📊 Benchmark Details

**Name**: Full-Duplex-Bench

**Overview**: Full-Duplex-Bench is a benchmark designed to evaluate critical aspects of full-duplex spoken dialogue models, focusing on interaction dimensions such as pause handling, backchanneling, smooth turn-taking, and user interruption management.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DanielLin94144/Full-Duplex-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic and reproducible evaluation framework for full-duplex spoken dialogue models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Turn-Taking
- Backchanneling
- Pause Handling
- User Interruption

**Limitations**: N/A

## 💾 Data

**Source**: Candor and ICC datasets, along with synthetic data generated using GPT-4o.

**Size**: 1,000 examples

**Format**: JSON

**Annotation**: Manually reviewed with dual-channel evidence.

## 🔬 Methodology

**Methods**:
- Automated metrics for evaluation
- Human evaluation for backchanneling dynamics

**Metrics**:
- Takeover Rate (TOR)
- Backchannel Frequency (Freq)
- Jensen-Shannon Divergence (JSD)
- Average Response Latency

**Calculation**: Metrics are computed based on the analysis of time-aligned transcriptions and recorded interactions.

**Interpretation**: Lower TOR indicates better management of user turns, and higher frequencies of backchanneling suggest more engaged dialogue.

**Validation**: The benchmark has been systematically tested against various full-duplex models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
