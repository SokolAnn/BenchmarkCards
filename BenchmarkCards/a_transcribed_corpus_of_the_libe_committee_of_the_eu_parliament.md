# a transcribed corpus of the LIBE committee of the EU parliament

## 📊 Benchmark Details

**Name**: a transcribed corpus of the LIBE committee of the EU parliament

**Overview**: We present a transcribed corpus of the LIBE committee of the EU parliament, totalling 3.6 Million running words. We investigated the most appropriate Automatic Speech Recognition (ASR) model to create an accurate text transcription of the audio recordings of the meetings in order to make their content available for research and analysis. We focused on the unsupervised domain adaptation of the ASR pipeline. Building on the transformer-based Wav2vec2.0 model, we experimented with multiple acoustic models, language models and the addition of domain-specific terms. We release the resulting corpus and our analysis pipeline for future research.

**Data Type**: text (transcribed parliamentary speech / speech-to-text segments)

**Domains**:
- Natural Language Processing
- Political Science

**Languages**:
- English

**Similar Benchmarks**:
- Europarl corpus
- ParlaMint
- VoxPopuli

**Resources**:
- [GitHub Repository](https://github.com/hdvos/EUParliamentASRDataAndCode)
- [Resource](https://arxiv.org/abs/2304.08137v1)
- [Resource](https://www.europarl.europa.eu/committees/en/meetings/webstreaming)

## 🎯 Purpose and Intended Users

**Goal**: To create an accurate text transcription of the audio recordings of the LIBE committee meetings in order to make their content available for research and analysis.

**Target Audience**:
- Political Scientists
- Linguists
- Researchers

**Tasks**:
- Automatic Speech Recognition (speech-to-text)
- Named Entity Recognition / hotword/entity recognition
- Topic Modeling
- Downstream political text analysis / information retrieval for political entities

**Limitations**: Audio is not always aligned with metadata; manual transcribed data for training was small (100 segments, 4,893 words) and therefore insufficient for substantial fine-tuning; diarization was not performed (pilot was inaccurate and outside scope); use of hotwords improved named entity recall but increased overall Word Error Rate and was not used for the released corpus.

## 💾 Data

**Source**: Audio recordings of the LIBE committee meetings (EU Parliament webstreaming service) and meeting agendas/minutes downloaded from the EU Parliament website; transcriptions produced via ASR (Wav2Vec2.0 experiments) and a manually transcribed evaluation set.

**Size**: Resulting corpus: 3,584,150 words. Audio downloaded: 332 files (mean length 152.63 minutes, sd 60.50; shortest 9.18 minutes, longest 289.43 minutes). After splitting: 128,918 segments (average length 21.64 seconds, sd 5.72). Manually transcribed evaluation set: 100 segments (4,893 words; total 36 minutes 18 seconds).

**Format**: Audio: 16 kHz 16-bit PCM WAV (converted from mp4). Transcriptions: text segmented into ~10-30 second segments.

**Annotation**: Automatic ASR-generated transcriptions (Wav2Vec2.0 based pipelines). A manually transcribed evaluation set of 100 segments (4,893 words) was created and used only for evaluation and cross-validation (not for training/fine-tuning).

## 🔬 Methodology

**Methods**:
- Automatic Speech Recognition evaluation using Wav2Vec2.0
- Domain adaptation / replacement of acoustic model (wav2vec2-base-960h vs wav2vec2-base-10k-voxpopuli-ft-en)
- Language model decoding using pyctcdecode with KenLM (3-gram and 5-gram)
- Hotwords boosting (meeting-specific hotword lists extracted from agendas/minutes with SpaCy)
- Custom audio splitting algorithm to create 10-30s segments
- 5-fold cross validation on the manually transcribed evaluation set
- Topic modeling (LDA) for corpus exploration

**Metrics**:
- Word Error Rate (WER)
- Precision (hotwords)
- Recall (hotwords)
- F1 Score (hotwords)
- Topic coherence (word2vec based coherence metric)

**Calculation**: WER computed as (S + D + I) / N, where S=substitutions, D=deletions, I=insertions, N=number of words in reference. WER computed per sentence using the jiwer package and averaged over all sentences. Hotwords metrics (precision, recall, F1) computed at token level per meeting: True Positives = entities correctly transcribed and present in hotword list and reference; False Positives = entities in hotword list and ASR output but not in reference; False Negatives = entities in hotword list and reference but not in ASR output. Topic coherence computed using a word2vec-based coherence metric.

**Interpretation**: Lower WER indicates better ASR quality ("lower is better" as reported). Domain-specific acoustic model (VoxPopuli) and using a language model improved WER; hotwords boosting increased named-entity recall but could increase overall WER due to false positives. The authors chose voxpopuli + 3-gram language model (without hotwords) as the settings to create the released corpus.

**Baseline Results**: Baseline 1 (Google Cloud API): WER 73.46. Baseline 2 (wav2vec2.0 base zero-shot): WER 28.22. Experiment 1 (wav2vec2.0 voxpopuli): WER 21.42. Experiment 2 (wav2vec2.0 voxpopuli + language model): WER 17.95. Experiment 3 (wav2vec2.0 voxpopuli + language model + hotwords): WER 25.53.

**Validation**: Hyperparameters (e.g., alpha and beta for CTC decoding, hotword weight) tuned with 5-fold cross validation on the manually transcribed evaluation set (100 segments split into 5 folds of 20 segments each).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
