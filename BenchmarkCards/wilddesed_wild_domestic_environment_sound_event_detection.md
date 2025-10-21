# WildDESED (Wild Domestic Environment Sound Event Detection)

## 📊 Benchmark Details

**Name**: WildDESED (Wild Domestic Environment Sound Event Detection)

**Overview**: The WildDESED dataset is an extension to the DESED dataset, crafted to reflect diverse acoustic variability and complex noises in home settings, enhancing the robustness of sound event detection systems in dynamic domestic environments.

**Data Type**: audio

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- DESED

**Resources**:
- [GitHub Repository](https://github.com/swagshaw/WildDESED)

## 🎯 Purpose and Intended Users

**Goal**: To advance sound event detection (SED) research by providing a dataset representing complex acoustic environments in homes.

**Target Audience**:
- Research Community
- Sound Event Detection Researchers
- Machine Learning Practitioners

**Tasks**:
- Sound Event Detection

**Limitations**: N/A

## 💾 Data

**Source**: WildDESED dataset synthesized using LLMs and a curated selection of audio noises from AudioSet.

**Size**: 10,000 audio clips

**Format**: Audio files (WAV)

**Annotation**: Strong annotations provided for sound events.

## 🔬 Methodology

**Methods**:
- Curriculum Learning
- Automated metrics evaluation

**Metrics**:
- Polyphonic Sound Event Detection Scores (PSDS)

**Calculation**: PSDS scores calculated based on sound event detection performance.

**Interpretation**: Higher PSDS scores indicate better SED performance under varying noise conditions.

**Validation**: The effectiveness of models was validated on noise levels using PSDS scores, with comparisons to baseline models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
