# E-chat200

## 📊 Benchmark Details

**Name**: E-chat200

**Overview**: E-chat200 dataset, designed explicitly for emotion-sensitive spoken dialogue.

**Data Type**: tuples of (question text, response, emotion, question speech)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [Resource](https://anonymous-echat.github.io/E-chat/)

## 🎯 Purpose and Intended Users

**Goal**: To enable a dialogue system capable of understanding and responding to various emotional cues in speech.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Spoken Dialogue

**Limitations**: N/A

## 💾 Data

**Source**: Developed specifically for E-chat's requirements, includes tuples of (question text, response, emotion, question speech).

**Size**: 178,000 tuples

**Format**: N/A

**Annotation**: Generated with the aid of GPT-3.5-Turbo and Microsoft's TTS API for high-quality speech.

## 🔬 Methodology

**Methods**:
- Objective evaluation
- Subjective evaluation

**Metrics**:
- Mean Opinion Score (MOS)
- BLEU Score
- Sentence similarity

**Calculation**: Performance is based on comparison with baseline models.

**Interpretation**: Higher MOS indicates better emotional expression and response accuracy.

**Baseline Results**: E-chat exhibited high performance compared to ParalinGPT and GPT-3.5.

**Validation**: E-chat200 dataset allows for a comprehensive evaluation of emotion-sensitive dialogue.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
