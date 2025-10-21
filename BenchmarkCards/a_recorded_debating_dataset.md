# A Recorded Debating Dataset

## 📊 Benchmark Details

**Name**: A Recorded Debating Dataset

**Overview**: This paper describes an English audio and textual dataset of debating speeches, a unique resource for the growing research field of computational argumentation and debating technologies. We release 60 speeches on various controversial topics, each in five formats corresponding to the different stages in the production of the data. The intention is to allow utilizing this resource for multiple research purposes, be it the addition of in-domain training data for a debate-specific ASR system, or applying argumentation mining on either noisy or clean debate transcripts.

**Data Type**: audio and text (recorded speeches; raw and clean ASR transcripts; manual reference transcripts)

**Domains**:
- Natural Language Processing
- Speech Processing
- Computational Argumentation

**Languages**:
- English

**Similar Benchmarks**:
- Internet Argument Corpus
- ArgRewrite
- Debater Project datasets
- Intelligence Squared transcripts

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide an English audio and textual dataset of debating speeches to support research in computational argumentation and debating technologies, including use as in-domain training data for debate-specific ASR systems and for argumentation mining on noisy or clean debate transcripts.

**Target Audience**:
- Researchers in computational argumentation and debating technologies
- Automatic Speech Recognition researchers
- Natural Language Processing researchers

**Tasks**:
- Automatic Speech Recognition
- Argumentation Mining
- Stance Classification
- Claim and Evidence Detection

**Limitations**: This is a first batch (60 speeches). Currently the list of speakers contains only a single female speaker and the authors are making an effort to recruit more female debaters. There is large variance in WER across recordings and speakers due to mismatch with ASR acoustic and language models.

## 💾 Data

**Source**: 60 speeches recorded specifically for this dataset by 10 speakers on 16 motions (motions from Rinott et al., 2015); each speech processed by an automatic speaker-independent ASR system and manually transcribed/post-edited to produce reference transcripts.

**Size**: 60 speeches; 5 file formats per speech

**Format**: WAV audio files (wav); raw automatic transcripts (asr); clean automatic transcripts (asr.txt); manual transcripts (trs); clean manual/reference transcripts (trs.txt)

**Annotation**: Automatic ASR transcripts produced by a speaker-independent deep neural network ASR system; manual post-editing by trained human transcribers to produce reference transcripts; ASR output further post-processed (timing removal, token cleaning, abbreviation reformatting, automatic punctuation via bi-directional LSTM, truecasing).

## 🔬 Methodology

**Methods**:
- Automatic Speech Recognition (speaker-independent deep neural network ASR)
- Automatic post-processing of ASR output (timing removal, token cleaning, abbreviation reformatting, automatic punctuation and sentence splitting using a bi-directional LSTM, truecasing)
- Manual transcription/post-editing by trained transcribers
- Segmentation by silence thresholds

**Metrics**:
- Word Error Rate (WER)

**Calculation**: WER is computed as the sum of substitution, deletion and insertion error rates.

**Interpretation**: Lower WER indicates better ASR performance. Authors used a pre-defined threshold of 10% WER to accept speaker recordings for inclusion; average ASR WER on released speeches is reported as 8.4%.

**Baseline Results**: The speaker-independent ASR system performs on average at 8.4% WER on the released speeches. Table 2 reports average WER per topic (examples: Topic 1 Violent video games 6 speeches WER 7.4%; Topic 483 Freedom of speech 5 speeches WER 6.7%). Speaker-dependent adaptation using about 15 minutes of a speaker's data reduced WER of an example speech from topic 61 from 12.9% to 8.6%, and from topic 483 from 12.2% to 9.7%.

**Validation**: Gold reference transcripts were created by pair-wise comparison of multiple transcribers' outputs and resolving differences by listening; transcribers were selected after scoring at least 98% accuracy on four test speeches and then further trained by transcribing ten speeches each with feedback. Segmentation was performed by cutting at silences longer than 500ms and further dividing long segments at silences of at least 100ms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: Currently the list of speakers contains only a single female speaker; the authors state they are making an effort to recruit more female debaters.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-ND

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
