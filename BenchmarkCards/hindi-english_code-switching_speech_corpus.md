# Hindi-English Code-Switching Speech Corpus

## 📊 Benchmark Details

**Name**: Hindi-English Code-Switching Speech Corpus

**Overview**: We present our first efforts in building a code-switching ASR system in the Indian context by creating a Hindi-English code-switching speech database. The database contains speech utterances with code-switching properties and covers session and speaker variations such as pronunciation, accent, age and gender. The database can be applied in speech signal processing applications such as code-switching automatic speech recognition, language identification, language modeling, and speech synthesis.

**Data Type**: speech utterances (audio) and text transcripts

**Domains**:
- Natural Language Processing
- Speech Processing

**Languages**:
- Hindi
- English

**Similar Benchmarks**:
- CUMIX Cantonese-English code-switching speech corpus
- Mandarin-Taiwanese code-switching speech corpus (Dau-cheng Lyu and Ren-yuan Lyu)
- English-Spanish code-switching speech corpus (Franco and Solorio)
- SEAME
- CECOS
- A small Hindi-English code-switching corpus (Anik Dey and Pascale Fung)
- Sepedi-English code-switching speech corpus
- FAME!
- Malay-English code-switching corpus
- MediaParl
- FACST
- Arabic-English code-switching speech corpus (Injy Hamed et al.)

**Resources**:
- [Resource](https://shoutmehindi.com)
- [Resource](https://notesinhinglish.blogspot.in)
- [Resource](https://www.techyukti.com)
- [Resource](http://www.learncpp.com)

## 🎯 Purpose and Intended Users

**Goal**: To create a Hinglish (Hindi-English code-switching) speech corpus to enable research and development of code-switching ASR systems and related speech processing tasks (language identification, language modeling, speech synthesis).

**Target Audience**:
- Researchers and practitioners in speech signal processing
- Automatic Speech Recognition developers
- Language modeling researchers

**Tasks**:
- Automatic Speech Recognition
- Language Identification
- Language Modeling
- Speech Synthesis

**Limitations**: The collection of the database is still in progress; authors describe the resource as moderate-sized.

## 💾 Data

**Source**: Text transcripts: crawled from blogging websites: https://shoutmehindi.com, https://notesinhinglish.blogspot.in, https://www.techyukti.com, http://www.learncpp.com. Acoustic data: recorded over the telephone from volunteering speakers recruited by a consultant, calling a toll-free number from their mobile phones in various acoustic environments.

**Size**: 7,005 utterances spoken by 71 speakers; 13,071 sentences in the text corpus; training/testing split for ASR evaluation: 5,500 training utterances and 1,505 testing utterances; 11,566 sentences used to train the language model.

**Format**: Audio recorded at 8 kHz sampling frequency and bit rate of 128; text transcripts normalized (extra spaces, special characters, emoticons removed).

**Annotation**: Manual inspection and pruning of speech files; manual phone-level transcription for unique words in the lexicon; text normalized into meaningful sentences for transcripts and language model training.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (ASR) using GMM/DNN acoustic models trained with the Kaldi toolkit
- Language model training (3-gram) using IRSTLM
- Automated metric evaluation (ASR evaluation)

**Metrics**:
- Word Error Rate (Percentage Word Error Rate, %WER)

**Calculation**: Percentage Word Error Rate (%WER) reported on the held-out test set of 1,505 utterances. Language model trained on 11,566 sentences (13071 total sentences minus 1505 test sentences).

**Interpretation**: Authors report %WER and state that the DNN-based acoustic model with 3-gram LM resulted in the best %WER compared to other evaluated models.

**Baseline Results**: Mono (MFCC): 53.51 %WER; Tri1 (MFCC): 33.52 %WER; Tri2 (MFCC + LDA): 32.73 %WER; Tri3 (MFCC + LDA + SAT): 27.20 %WER; DNN (MFCC + LDA + SAT): 25.40 %WER.

**Validation**: The database was validated by developing ASR systems (GMM/DNN acoustic models) and reporting %WER on a held-out test set (1,505 utterances).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Database includes 71 speakers from 21 states of India; geographical distribution: East 40.84%, West 9.85%, North 30.98%, South 18.33%; age range 20 to 64 years; gender distribution: 44 male and 27 female speakers (61.97% male, 38.03% female).

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
