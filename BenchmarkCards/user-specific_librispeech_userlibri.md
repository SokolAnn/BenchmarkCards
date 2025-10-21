# User-Specific LibriSpeech (UserLibri)

## 📊 Benchmark Details

**Name**: User-Specific LibriSpeech (UserLibri)

**Overview**: We release this User-Specific LibriSpeech (UserLibri) dataset to aid future personalization research. UserLibri is a re-formatting of LibriSpeech containing paired audio-transcripts grouped by user and extra text-only personalized data from Project Gutenberg, intended to enable personalization of ASR via personalized language models trained on text-only data.

**Data Type**: audio-transcript pairs and text-only sentences

**Domains**:
- Natural Language Processing
- Speech Recognition

**Languages**:
- English

**Similar Benchmarks**:
- LibriSpeech
- Multilingual LibriSpeech

**Resources**:
- [Resource](https://www.kaggle.com/datasets/google/userlibri)
- [Resource](https://arxiv.org/abs/2207.00706)
- [Resource](https://www.openslr.org/12)
- [Resource](https://www.gutenberg.org)

## 🎯 Purpose and Intended Users

**Goal**: Aid future personalization research by providing a dataset containing user-specific paired audio-transcripts and extra text-only personalized data to enable ASR personalization using text-only data.

**Target Audience**:
- Personalization researchers
- Automatic speech recognition researchers

**Tasks**:
- Speech Recognition
- Language Modeling
- Language Model Personalization

**Limitations**: Focuses on the English LibriSpeech corpus; only users found in LibriSpeech test-clean and test-other are considered; some book text sources appear across LibriSpeech splits (train/dev/test), which may cause overlap of text across splits.

## 💾 Data

**Source**: Re-formatting of LibriSpeech: paired audio-transcript data from LibriSpeech (recordings of Project Gutenberg e-books) combined with additional text-only data from the remainder of the corresponding Project Gutenberg books; users are formed by combining audio examples from chapters of the same book read by the same speaker.

**Size**: LibriSpeech: 970 hours of paired audio-transcript data. UserLibri: Test-Clean: 55 users; total LM train text sentences 377,049; average # audio-transcript utterances per user 47.1 (median 46); max audio utterances for one user 108. Test-Other: 52 users; total LM train text sentences 444,520; average # audio-transcript utterances per user 56.5 (median 52); max audio utterances for one user 144. LM train text per-user averages: 6,855 (Test-Clean) and 8,548 (Test-Other); max LM sentences for one user 54,306 (Test-Clean) and 38,498 (Test-Other).

**Format**: LibriSpeech audio files and metadata; LM training text as processed UTF-8 sentence-separated text files (book boilerplate removed, sentences uppercased and tokenized).

**Annotation**: Paired audio-transcript data from LibriSpeech (original LibriSpeech transcripts) and text sentences extracted from Project Gutenberg books processed programmatically (boilerplate removal, sentence-splitting, punctuation trimming, uppercasing).

## 🔬 Methodology

**Methods**:
- Automated evaluation using Word Error Rate (WER)
- Model-based evaluation: shallow fusion of external RNN language models with ASR models (streaming and nonstreaming)
- Hyperparameter sweeps for beam search and LM fusion weights
- 5-fold cross validation for speech personalization experiments
- Bootstrap sampling to compute 95% confidence intervals

**Metrics**:
- Word Error Rate (WER)
- 95% confidence intervals (CIs) computed via bootstrap

**Calculation**: Average per-user WER is reported. 95% confidence intervals are calculated using the bootstrap technique by sampling per-user WERs with replacement 10,000 times.

**Interpretation**: Lower WER indicates better ASR performance. The paper compares average per-user WER across conditions (no fusion baseline, fusion with general LM, fusion with personalized LMs) and reports improvements when using personalized LMs, with larger LMs and streaming models showing greater absolute improvements.

**Baseline Results**: Baselines reported include: Streaming No Fusion (BL1) Test-Clean average WER 6.0% [5.3;6.7], Test-Other 11.2% [9.6;13.0]. Streaming Gen 10M LM (BL2) Test-Clean 5.4% [4.8;6.0], Test-Other 9.7% [8.3;11.1]. Nonstreaming No Fusion (BL1) Test-Clean 2.5% [2.1;2.8], Test-Other 6.8% [5.6;8.1]. With personalized LM fusion, examples: Streaming 25M p13n Test-Other 8.7% [7.4;10.2]; Nonstreaming 25M p13n All Users 3.2% [2.7;3.8]. (See Tables 2 and 3 in the paper for full results and CIs.)

**Validation**: Validated by comparing to baselines (no fusion and fusion with a general 10M LM trained on LibriSpeech LM data). For speech personalization experiments, per-user ASR personalization used 5-fold cross validation for the 102 users with at least 10 audio-transcript pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: Detecting and mitigating performance disparities across users (bias where model performance on certain users/classes may be much worse than others).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Paper highlights on-device personalization approaches that can train on user data on-device without sending raw user data to a central server; no additional anonymization procedures are specified for the released dataset.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
