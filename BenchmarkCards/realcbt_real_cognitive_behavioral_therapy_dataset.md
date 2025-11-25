# RealCBT (Real Cognitive Behavioral Therapy Dataset)

## 📊 Benchmark Details

**Name**: RealCBT (Real Cognitive Behavioral Therapy Dataset)

**Overview**: RealCBT is a dataset of authentic cognitive behavioral therapy dialogues collected from public video-sharing platforms. It allows for a comparative analysis of emotional arcs between real and LLM-generated therapy sessions, highlighting the emotional dynamics that characterize these interactions.

**Data Type**: dialogue text

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- CACTUS (CBT-augmented Counseling Chat Corpus)

**Resources**:
- [Resource](https://gitlab.com/xiaoyi.wang/realcbt-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To establish an empirical benchmark for comparing emotional dynamics in real vs. synthetic therapy dialogues.

**Target Audience**:
- ML Researchers
- Mental Health Practitioners

**Tasks**:
- Dialogue Generation
- Emotional Dynamics Analysis

**Limitations**: RealCBT is limited in size and exhibits subgroup imbalance due to the difficulties in collecting authentic therapy dialogues.

## 💾 Data

**Source**: Collected from public video-sharing platforms, specifically CBT-based counseling sessions.

**Size**: 76 dialogues

**Format**: MP4 and transcribed text

**Annotation**: Manual transcription and automated annotation of metadata using language models.

## 🔬 Methodology

**Methods**:
- Comparative emotional arc analysis
- Utterance Emotion Dynamics framework

**Metrics**:
- Emotion Mean
- Emotion Variability
- Emotion Rise Rate
- Emotion Recovery Rate

**Calculation**: Metrics are computed from sequences of utterances using NRC Valence, Arousal, and Dominance (VAD) Lexicon.

**Interpretation**: Higher values in emotional metrics indicate greater emotional engagement, variability, and recovery.

**Baseline Results**: Comparative analysis primarily against synthetic dialogues from the CACTUS dataset.

**Validation**: Systematic statistical analysis using the Mann–Whitney U test to confirm significance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: The dataset reflects demographic patterns relating to client gender and therapist-client interactions.

**Potential Harm**: The synthesis of therapy dialogues could mislead users regarding the emotional fidelity of synthetic conversations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data collected from public domains ensuring no personal identifiers were included.

**Data Licensing**: Not Applicable

**Consent Procedures**: All data sourced from publicly accessible content.

**Compliance With Regulations**: Not Applicable
