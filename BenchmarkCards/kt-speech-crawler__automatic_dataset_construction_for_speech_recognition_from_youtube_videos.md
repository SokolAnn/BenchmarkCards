# KT-Speech-Crawler: Automatic Dataset Construction for Speech Recognition from YouTube Videos

## 📊 Benchmark Details

**Name**: KT-Speech-Crawler: Automatic Dataset Construction for Speech Recognition from YouTube Videos

**Overview**: KT-Speech-Crawler: an approach for automatic dataset construction for speech recognition by crawling YouTube videos. The paper outlines several filtering and post-processing steps which extract samples that can be used for training end-to-end neural speech recognition systems.

**Data Type**: audio-transcription pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Wall Street Journal (WSJ)
- TED-LIUM v2
- LibriSpeech
- VoxForge
- Mozilla's Common Voice
- Speech Commands
- YouTube-8M

**Resources**:
- [Resource](http://emnlp-demo.lakomkin.me/)
- [GitHub Repository](https://github.com/EgorLakomkin/KTSpeechCrawler)

## 🎯 Purpose and Intended Users

**Goal**: Provide a crawler that automatically extracts speech samples with transcriptions from YouTube, filter high-quality samples with heuristic measures, and validate usefulness by augmenting training data of benchmark ASR datasets and measuring test performance differences.

**Target Audience**:
- ML Researchers
- Model Developers
- Speech Recognition Researchers

**Tasks**:
- Automatic Speech Recognition
- Dataset construction for Speech Recognition

**Limitations**: N/A

## 💾 Data

**Source**: YouTube videos with user-provided closed captions (English closed captions).

**Size**: Around 150 hours of transcribed speech can be obtained within a day (paper reports using 200 hours (108,617 utterances) and 300 hours in experiments; script to construct a dataset of 500 hours is provided).

**Format**: N/A

**Annotation**: Transcriptions are taken from user-provided YouTube closed captions (automatically used as ground truth); manual verification was performed on a random subset (600 samples) to estimate transcription quality; a web-based demo allows human confirmation/correction of extracted samples.

## 🔬 Methodology

**Methods**:
- Heuristic filtering and post-processing of YouTube closed captions
- Forced alignment using Kaldi
- Automated metrics evaluation (Word Error Rate, Character Error Rate)
- Manual human evaluation of a random subset (600 samples)

**Metrics**:
- Word Error Rate (WER)
- Character Error Rate (CER)
- Levenshtein similarity (used for filtering)

**Calculation**: Word Error Rate (WER) computed as WER = (S + D + I) / (S + D + C), where S = substitutions, D = deletions, I = insertions, C = correct words.

**Interpretation**: Lower WER and CER indicate better ASR performance. The authors report reductions in WER and CER when augmenting benchmark training sets with the collected YouTube samples (see Table 1 for examples).

**Baseline Results**: Table 1 results reported in paper: 
- Train: WSJ, Test: WSJ -> WER 27.4%, CER 7.2%
- Train: WSJ + YouTube (200h), Test: WSJ -> WER 15.8%, CER 4.2%
- Train: YouTube (200h), Test: WSJ -> WER 31.5%, CER 8.3%
- Train: TED, Test: TED -> WER 32.6%, CER 10.4%
- Train: TED + YouTube (300h), Test: TED -> WER 28.1%, CER 8.2%
- Train: YouTube (300h), Test: TED -> WER 36.6%, CER 10.6%

**Validation**: Validation steps include: manual inspection of a random subset of 600 samples estimating a 3.5% word error rate in transcriptions; excluding TED videos from YouTube set by removing videos containing a 'TED' token in title or description; using forced alignment with Kaldi to adjust caption boundaries; applying a Levenshtein similarity threshold of 70% against Google ASR output on three random phrases per video to filter out misaligned or language-mismatched videos.

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
