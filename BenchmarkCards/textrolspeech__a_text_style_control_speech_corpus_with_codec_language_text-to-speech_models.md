# TextrolSpeech: A Text Style Control Speech Corpus with Codec Language Text-to-Speech Models

## 📊 Benchmark Details

**Name**: TextrolSpeech: A Text Style Control Speech Corpus with Codec Language Text-to-Speech Models

**Overview**: TextrolSpeech is the first large-scale speech emotion dataset annotated with rich text attributes, consisting of 236,220 pairs of style prompt in natural text descriptions with five style factors and corresponding speech samples.

**Data Type**: speech-emotion pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://sall-e.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To drive the development of text controllable TTS systems through a comprehensive dataset enriched with diverse and natural text descriptions.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Text-to-Speech

**Limitations**: N/A

## 💾 Data

**Source**: TextrolSpeech dataset is created from a combination of previous TTS datasets and additional emotional datasets.

**Size**: 330 hours

**Format**: Audio files

**Annotation**: Annotated with five style factors: gender, pitch, speaking speed, volume, and emotion.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Mean Opinion Score (MOS)

**Calculation**: Metrics are calculated based on classification accuracy for several speech style factors and subjective evaluations via MOS.

**Interpretation**: Higher accuracy indicates better performance in style recognition; MOS evaluates quality and similarity of generated speech to prompts.

**Baseline Results**: PromptTTS accuracy for style factors: Gender: 92.5%, Pitch: 82.5%, Speed: 83%, Volume: 82%, Emotion: 71.5%. Salle achieves higher accuracy rates across all factors.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
