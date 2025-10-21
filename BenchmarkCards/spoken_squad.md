# Spoken SQuAD

## 📊 Benchmark Details

**Name**: Spoken SQuAD

**Overview**: We propose a new listening comprehension task - Spoken SQuAD. On the new task, we found that speech recognition errors have catastrophic impact on machine comprehension, and several approaches are proposed to mitigate the impact.

**Data Type**: question-answering pairs (audio documents with text questions and answer spans)

**Domains**:
- Natural Language Processing
- Spoken Language Understanding

**Languages**:
- English

**Similar Benchmarks**:
- SQuAD (Stanford Question Answering Dataset)
- TOEFL listening comprehension test

**Resources**:
- [GitHub Repository](https://github.com/chiahsuan156/Spoken-SQuAD)

## 🎯 Purpose and Intended Users

**Goal**: To propose the Spoken SQuAD task, an extraction-based spoken question answering (SQA) task with a new evaluation approach; to measure the impact of ASR errors on machine comprehension; and to propose approaches (subword unit embeddings, training on ASR transcriptions, dropout) to mitigate ASR errors.

**Tasks**:
- Question Answering
- Spoken Question Answering

**Limitations**: The synthesized speech makes the task easier than its real application, and study on real speech recording is left as future work.

## 💾 Data

**Source**: Derived from SQuAD: articles synthesized by Google text-to-speech and transcribed using CMU Sphinx ASR. SQuAD training set used to generate Spoken SQuAD training set; SQuAD development set used to generate Spoken SQuAD testing set. Question-answer pairs whose answers did not exist in the ASR transcriptions were removed.

**Size**: 37,111 question-answer pairs (training), 5,351 question-answer pairs (testing).

**Format**: Audio files (synthesized speech) and ASR transcriptions (text) with word-level timestamps (used to compute answer time spans).

**Annotation**: Uses original SQuAD human-written question-answer pairs; time spans for answers obtained by forced-aligning the spoken document with its reference transcription; question-answer pairs removed when the answer did not exist in ASR transcription.

## 🔬 Methodology

**Methods**:
- Automated metrics (Exact Match and F1 on text answers)
- Audio Overlapping Score (AOS) for predicted audio time spans
- Comparative evaluation of models trained on text documents vs. ASR transcriptions
- Ablation experiments with subword unit embeddings (phoneme, syllable, character) and dropout

**Metrics**:
- Exact Match (EM)
- F1 Score
- Audio Overlapping Score (AOS)
- Word Error Rate (WER)

**Calculation**: Exact Match (EM): 1 if predicted text answer exactly equals the ground-truth answer, otherwise 0. F1: based on word-level precision and recall between predicted and ground-truth answers. AOS: computed between predicted answer time interval and ground-truth time interval as an overlap score (rewards overlap and penalizes overly long predicted spans). WER reported for audio/transcriptions.

**Interpretation**: EM/F1 evaluate text answer correctness but can penalize correct span selection when ASR misrecognizes words (common for named entities). AOS evaluates the time-span overlap between predicted and ground-truth audio segments and better reflects reasoning capability for SQA when transcription errors exist.

**Baseline Results**: Results on Spoken SQuAD testing set (SpokenS-test) vs SQuAD-dev (reported only on questions present in SpokenS-test): BiDAF — SQuAD-dev EM 58.4 F1 69.9; SpokenS-test EM 37.02 F1 50.9. R-NET — SQuAD-dev EM 66.34 F1 76.20; SpokenS-test EM 44.75 F1 58.68. Mnemonic Reader — SQuAD-dev EM 64.00 F1 73.35; SpokenS-test EM 40.36 F1 52.87. Dr.QA — SQuAD-dev EM 62.84 F1 73.74; SpokenS-test EM 41.16 F1 54.51. FusionNet — SQuAD-dev EM 70.47 F1 79.51; SpokenS-test EM 46.51 F1 60.06. Average across models: SQuAD-dev F1 74.54 vs SpokenS-test F1 55.40. Additional comparisons: training on ASR transcriptions (Spoken) improved SpokenS-test performance (e.g., BiDAF SpokenS-test EM 44.45 F1 57.6 when trained on Spoken training set vs EM 37.02 F1 50.9 when trained on text). Ablation on BiDAF: WORD+CHAR EM 37.02 F1 50.9; WORD+CHAR+Dropout EM 38.83 F1 53.07; WORD+PHONEME+Dropout EM 39.82 F1 53.76; WORD+SYLLABLE+Dropout EM 39.71 F1 53.72. Performance across noise levels and AOS reported in Table 5 of the paper.

**Validation**: Validated by comparing multiple state-of-the-art SQuAD reading-comprehension models trained on SQuAD training set vs Spoken SQuAD training set, and tested on Spoken SQuAD testing set and two noisy variants (different WERs). Forced-alignment used to obtain ground-truth audio time spans; SQuAD-dev subset (questions present in SpokenS-test) used for fair SQuAD vs SpokenS comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Governance**: Unrepresentative risk testing

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
