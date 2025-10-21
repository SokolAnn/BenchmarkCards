# CHiME-5 Challenge

## 📊 Benchmark Details

**Name**: CHiME-5 Challenge

**Overview**: The CHiME-5 Challenge considers the task of distant multi-microphone conversational automatic speech recognition (ASR) in real home environments. Speech material was elicited using a 4-people dinner party scenario recorded by 6 Kinect microphone arrays and 4 binaural microphone pairs in 20 homes. The challenge features a single-array track and a multiple-array track and provides detailed baseline systems for array synchronization, speech enhancement, conventional ASR and end-to-end ASR.

**Data Type**: multimodal (multi-microphone audio: Kinect microphone arrays and binaural recordings; video; reference transcriptions)

**Domains**:
- Natural Language Processing
- Speech and Audio Processing

**Similar Benchmarks**:
- CHiME-1
- CHiME-2
- CHiME-4
- DICIT
- Sweet-Home
- DIRHA
- voiceHome
- ICSI
- CHIL
- AMI
- LLSEC
- COSINE
- Sheffield Wargames corpus
- Santa Barbara Corpus of Spoken American English

**Resources**:
- [GitHub Repository](https://github.com/kaldi-asr/kaldi/tree/master/egs/chime5/s5)
- [Resource](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)
- [GitHub Repository](https://github.com/AdolfVonKleist/Phonetisaurus)
- [Resource](http://www.speech.sri.com/projects/srilm/)
- [GitHub Repository](https://github.com/espnet/espnet)

## 🎯 Purpose and Intended Users

**Goal**: Advance robust ASR by providing a large-scale corpus of real multi-speaker conversational speech recorded via commercially available multi-microphone hardware in multiple homes, and to evaluate systems on distant multi-microphone conversational ASR with standardized tasks, tracks, and baselines.

**Target Audience**:
- ML Researchers
- Speech and Audio Processing Researchers
- ASR System Developers
- Challenge Participants

**Tasks**:
- Automatic Speech Recognition
- Speech Enhancement
- Array Synchronization

**Limitations**: N/A

## 💾 Data

**Source**: Recordings of twenty separate dinner parties in 20 real homes. Each party has four participants and was recorded with six Microsoft Kinect devices (each with a 4-microphone linear array and a camera) and four binaural Soundman OKM II Classic Studio microphones worn by participants. Raw microphone signals and video were recorded; binaural audio was recorded on Tascam DR-05 recorders. Reference transcriptions were produced per speaker using the binaural recordings.

**Size**: Train: 16 parties, 32 speakers, 40:33 hours, 79,980 utterances; Dev: 2 parties, 8 speakers, 4:27 hours, 7,440 utterances; Eval: 2 parties, 8 speakers, 5:12 hours, 11,028 utterances.

**Format**: Raw microphone signals and video; JSON transcription files containing utterance start/end times and metadata.

**Annotation**: Fully manually produced reference transcriptions per speaker using binaural recordings with utterance start and end times; transcriptions may include tags: [noise], [inaudible], [laughs], [redacted].

## 🔬 Methodology

**Methods**:
- Automated metrics (Word Error Rate) reported by participants
- Baseline system evaluations (conventional HMM/GMM and LF-MMI TDNN ASR via Kaldi; end-to-end ASR via ESPnet)
- Submission of Kaldi-format lattices and technical system descriptions for validation and ranking

**Metrics**:
- Word Error Rate (WER)
- WER broken down by session and location

**Calculation**: Word Error Rate (WER) computed on submitted system outputs compared to the provided reference transcriptions. Participants submit Kaldi-format lattices to allow validation of scores.

**Interpretation**: Systems are ranked based on performance (WER) on the evaluation data. Ranking A focuses on systems constrained to conventional acoustic modeling with the supplied official language model; Ranking B includes all other systems (e.g., end-to-end or systems with modified lexicon/language model).

**Baseline Results**: Development set (binaural/oracle): conventional (GMM) WER 72.8; conventional (LF-MMI TDNN) WER 47.9; end-to-end WER 67.2. Development set (reference Kinect array with beamforming): conventional (GMM) WER 91.7; conventional (LF-MMI TDNN) WER 81.3; end-to-end WER 94.7.

**Validation**: Participants must submit Kaldi-format lattices for validation. Dataset is split into disjoint training, development and evaluation sets with no speaker overlap. Development and evaluation transcriptions contain speaker location and reference array for each utterance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Intellectual Property
- Robustness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Intellectual Property**: Copyright infringement

**Potential Harm**: ['Risk of exposing personally identifying information (some personally identifying material was redacted post-recording as part of the consent process)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Some personally identifying material was redacted post-recording as part of the consent process.

**Data Licensing**: Not Applicable

**Consent Procedures**: Some personally identifying material was redacted post-recording as part of the consent process.

**Compliance With Regulations**: Not Applicable
