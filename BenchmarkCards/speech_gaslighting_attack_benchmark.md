# Speech Gaslighting Attack Benchmark

## 📊 Benchmark Details

**Name**: Speech Gaslighting Attack Benchmark

**Overview**: This paper presents a systematic and comprehensive evaluation benchmark that probes the robustness of Speech LLMs against Gaslighting attack prompts, spanning both linguistic and acoustic modalities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MELD
- MMAU
- MMSU
- OpenBookQA
- VocalSound

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the robustness of Speech LLMs against gaslighting attacks and to construct a behavior-aware benchmark.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Emotion Recognition
- Speech Transcription
- Vocal Sound Classification
- Spoken Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Derived from five speech-related benchmark datasets including MELD, MMAU, MMSU, VocalSound, and OpenBookQA.

**Size**: 10,740 examples

**Format**: N/A

**Annotation**: Annotated with model misbehavior signals such as incorrect answers, unsolicited apologies, and refusal responses.

## 🔬 Methodology

**Methods**:
- Adversarial prompting
- Behavioral response annotation
- Controlled acoustic ablation

**Metrics**:
- Accuracy
- Contradiction rate

**Calculation**: Metrics calculated based on the percentage of correct predictions that are reversed after exposure to gaslighting prompts.

**Interpretation**: Higher accuracy indicates better model robustness against gaslighting attacks.

**Baseline Results**: N/A

**Validation**: Evaluated across five state-of-the-art Speech LLMs under both clean and gaslighting conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
