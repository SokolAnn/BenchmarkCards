# Audio Dialogues

## 📊 Benchmark Details

**Name**: Audio Dialogues

**Overview**: Audio Dialogues is a multi-turn dialogue dataset containing 163.8k samples for general audio sounds and music, designed to enhance audio understanding through interactive dialogue.

**Data Type**: multi-turn dialogue pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://audiodialogues.github.io/LLMs)

## 🎯 Purpose and Intended Users

**Goal**: To enhance audio understanding within the context of multi-turn dialogues for general sounds and music.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Dialogue Generation
- Audio Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Generated using a prompting-based approach leveraging caption annotations from existing datasets such as AudioSet and MusicCaps.

**Size**: 163,800 samples

**Format**: N/A

**Annotation**: Generated using GPT-4 with a data filtration strategy to enhance quality.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- CIDEr
- BLEU Score
- ROUGE-L

**Calculation**: Metrics are calculated based on the generated responses evaluated against reference answers.

**Interpretation**: Higher scores indicate better quality of responses in terms of content relevancy and coherence across dialogues.

**Baseline Results**: Results from audio understanding models such as LTU, Qwen-Audio, and Audio Flamingo are evaluated on this dataset.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
