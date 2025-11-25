# VoiceBBQ

## 📊 Benchmark Details

**Name**: VoiceBBQ

**Overview**: VoiceBBQ is a spoken extension of the BBQ (Bias Benchmark for Question answering) that evaluates social bias in Spoken Language Models (SLMs) by analyzing the effects of content and acoustic characteristics on model bias.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BBQ

**Resources**:
- [Resource](https://huggingface.co/datasets/bgnkim/VoiceBBQ)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the effects of content and acoustic characteristics on social bias in Spoken Language Models.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Bias Evaluation

**Limitations**: Our analysis focused on only two models for examining bias and did not propose mitigation techniques.

## 💾 Data

**Source**: Adapted from BBQ dataset; speech synthesized using Kokoro-TTS.

**Size**: 935,872 audio samples

**Format**: WAV

**Annotation**: Automated mapping of model outputs to structured answer choices.

## 🔬 Methodology

**Methods**:
- Comparative bias evaluation
- Statistical analysis via McNemar’s test

**Metrics**:
- Bias score
- Accuracy

**Calculation**: Bias scores computed based on model responses to ambiguous and disambiguated questions in the BBQ dataset.

**Interpretation**: A bias score close to zero indicates minimal bias, with the sign suggesting preference for biased options.

**Baseline Results**: Baseline bias evaluation metrics derived from BBQ.

**Validation**: Confidence checks on synthesized speech were performed using gender and accent classifiers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: Not performed but suggested as a future exploration.

**Potential Harm**: ['Social bias in AI interactions']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
