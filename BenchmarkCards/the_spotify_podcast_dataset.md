# The Spotify Podcast Dataset

## 📊 Benchmark Details

**Name**: The Spotify Podcast Dataset

**Overview**: We present the Spotify Podcast Dataset, a set of approximately 100K podcast episodes comprised of raw audio files along with accompanying ASR transcripts. This represents over 47,000 hours of transcribed audio (dataset section reports 50,000 hours) and is intended to enable research in spoken document retrieval, segmentation, and summarization for the Information Retrieval and Natural Language Processing communities.

**Data Type**: audio and text (raw audio files with ASR transcripts and word-level timestamps)

**Domains**:
- Natural Language Processing
- Information Retrieval
- Speech Processing

**Languages**:
- English

**Similar Benchmarks**:
- Podcast Summaries data set
- Dataset collated by Yang et al. (2019)
- ATIS
- TIMIT
- CALLHOME
- Santa Barbara Corpus of Spoken American English
- TED talks corpus

**Resources**:
- [Resource](https://trec.nist.gov/pubs/call2020.html)
- [Resource](https://pypi.org/project/langid/)
- [Resource](https://cloud.google.com/speech-to-text/docs/video-model)
- [Resource](https://www.aclweb.org/anthology/2020.coling-main.519)

## 🎯 Purpose and Intended Users

**Goal**: To provide the first large-scale corpus of podcast audio data with full transcripts to encourage research in the podcast medium for speech and text processing tasks such as information retrieval and summarization.

**Target Audience**:
- Information Retrieval researchers
- Natural Language Processing researchers
- Speech Processing researchers
- Researchers interested in spoken document retrieval and summarization

**Tasks**:
- Spoken Document Retrieval
- Segmentation
- Summarization

**Limitations**: Dataset is limited to English in the current version; RSS header metadata may contain noise or inaccurate episode-level information; ASR transcripts are automatically generated (manual evaluation reports non-zero error rates).

## 💾 Data

**Source**: Approximately 100,000 podcast episodes randomly sampled from episodes published between January 1, 2019 and March 1, 2020, drawn from a variety of creators (including Spotify Studios, Parcast, Gimlet, Anchor). For each episode the dataset provides raw audio, ASR transcripts, and RSS header HTML snapshots with show- and episode-level metadata.

**Size**: 100,000 podcast episodes; 50,000 hours of audio and accompanying transcripts

**Format**: Raw audio files; ASR transcripts with word-level timestamps, speaker diarization, casing, and punctuation (as produced by Google Cloud Speech-to-Text API); RSS header HTML snapshots

**Annotation**: Transcripts automatically generated using Google Cloud Platform's Cloud Speech-to-Text API. A manual evaluation set of 1,600 English episodes was used to assess transcription quality.

## 🔬 Methodology

**Methods**:
- Automatic speech-to-text transcription using Google Cloud Platform Cloud Speech-to-Text API
- Manual evaluation of a held-out set (1,600 episodes)
- Dataset sampling and filtering based on metadata language tags, language identification on descriptions, episode length heuristics, streaming threshold, and speech detection classifier

**Metrics**:
- Word Error Rate (WER)
- Named Entity Recognition accuracy

**Calculation**: Metrics are reported from a manual evaluation on a heterogeneous test set of 1,600 English episodes; the paper reports a word error rate of 18.1% and a named entity recognition accuracy of 81.8%. Detailed calculation formulas are not specified beyond these reported results.

**Interpretation**: Reported WER and NER accuracy are used to quantify ASR transcript quality; the authors state that GCP-ASR showed robustness across differences in audio data quality and regional accents as evidenced by the reported metrics.

**Baseline Results**: On the 1,600-episode manual evaluation set, Google Cloud Platform ASR achieved a word error rate of 18.1% and a named entity recognition accuracy of 81.8%.

**Validation**: Manual evaluation on 1,600 English episodes selected to cover a variety of domains, numbers of speakers, regional accents, levels of formality, and audio quality.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
