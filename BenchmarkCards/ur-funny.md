# UR-FUNNY

## 📊 Benchmark Details

**Name**: UR-FUNNY

**Overview**: This paper presents a diverse multimodal dataset, called UR-FUNNY, to open the door to understanding multimodal language used in expressing humor. The dataset and accompanying studies present a framework in multimodal humor detection for the natural language processing community.

**Data Type**: multimodal (text, vision, acoustic)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- 16000 One-Liners
- Pun of the Day
- PTT Jokes
- Ted Laughter
- Big Bang Theory

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Introducing the first multimodal language dataset of humor detection named "UR-FUNNY" to enable understanding and modeling humor in a multimodal framework.

**Target Audience**:
- Natural Language Processing community

**Tasks**:
- Humor Detection
- Punchline Detection
- Binary Classification

**Limitations**: We observed that the camera angle and position changes frequently during TED presentations. However, for the majority of time, the camera stays focused on the presenter. Due to the volatile camera work, the only consistently available source of visual information was the speaker’s face.

## 💾 Data

**Source**: TED talks videos and transcripts collected from the TED portal (www.ted.com); audience 'laughter' markers in transcripts used to identify punchlines and construct labels.

**Size**: 1866 videos; total duration 90.23 hours; 16,514 video segments (8,257 humor instances and 8,257 non-humor instances); 1,741 distinct speakers; 417 distinct topics; 63,727 sentences; 965,573 words; 32,995 unique words.

**Format**: N/A

**Annotation**: Positive labels (humor) extracted using audience 'laughter' markers in TED transcripts; negative samples chosen at random intervals from the same videos (last sentence not immediately followed by a laughter marker); forced alignment (P2FA) used to align text, audio and video at word/phoneme/sentence levels.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (Contextual Memory Fusion Network (C-MFN) and variants)
- Automated metrics (binary accuracy)
- Human evaluation (annotator study for human performance estimate)

**Metrics**:
- Binary Accuracy
- Categorical Cross-Entropy (training loss)

**Calculation**: All models are trained using categorical cross-entropy. This measure is calculated between the output of the model and ground-truth labels. Binary accuracy is reported as percent correct on the test fold.

**Interpretation**: The authors state that while a state-of-the-art model can achieve a reasonable level of success in modeling humor, there is still a large gap between human-level performance and state-of-the-art. Thus higher accuracy closer to human performance indicates better modeling; current models leave a substantial gap.

**Baseline Results**: C-MFN (all modalities T+A+V) achieved 65.23% binary accuracy. C-MFN (punchline only) best 64.47% (T+A+V). C-MFN (context only) best 58.45% (T+A+V). Reported human performance on UR-FUNNY is 82.5%. (Results reported in Table 4 of the paper.)

**Validation**: Standard train/validation/test folds are provided and are speaker-independent (no shared speakers across folds). Train: 5,306 humor / 5,292 non-humor instances using 1,166 videos and 1,059 speakers. Validation: 1,313 / 1,313 instances using 300 videos and 294 speakers. Test: 1,638 / 1,652 instances using 400 videos and 388 speakers.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
