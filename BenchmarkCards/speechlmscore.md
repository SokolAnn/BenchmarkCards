# SpeechLMScore

## 📊 Benchmark Details

**Name**: SpeechLMScore

**Overview**: An unsupervised metric to evaluate generated speech using a speech language model. SpeechLMScore computes the average log-probability of a speech signal by mapping it into discrete tokens and measuring the average probability of generating the sequence of tokens. It does not require human annotation and is proposed as a scalable framework that correlates with human evaluation scores on voice conversion, text-to-speech, and speech enhancement.

**Data Type**: audio (speech; discrete token sequences)

**Domains**:
- Natural Language Processing
- Speech Processing

**Similar Benchmarks**:
- VoiceMOS challenge
- Deep Noise Suppression challenge 2020
- LibriLight

**Resources**:
- [GitHub Repository](https://github.com/ESPnet/ESPnet)
- [GitHub Repository](https://github.com/facebookresearch/fairseq)

## 🎯 Purpose and Intended Users

**Goal**: Propose SpeechLMScore, an automatic unsupervised metric that measures the likelihood of a speech sample using a pretrained speech-unit language model (average log-probability of discrete tokens) to evaluate speech generation quality without requiring reference speech or human MOS labels.

**Tasks**:
- Voice Conversion
- Text-to-Speech
- Speech Enhancement
- Speech Quality Assessment

**Limitations**: SpeechLMScore has bias towards speech fluency more than pitch characteristics which is the main factor of evaluation in older TTS models. There is scope for further improvement; future extensions are envisioned to use more complex and prosody-rich tokens.

## 💾 Data

**Source**: VoiceMOS challenge dataset (contains speech from voice conversion challenges 2016/2018/2020, ESPnet-trained TTS on LJspeech, and Blizzard challenges), Deep Noise Suppression challenge 2020 noisy reverberant testset, LibriSpeech (used for HuBERT pretraining and clustering models), and LibriLight (used for pretrained uLM and for LSTM language model training).

**Size**: VoiceMOS main track: 7,106 utterances (187 systems, 38 samples per system); VoiceMOS testset: 1,066 files; DNS-challenge-2020 noisy reverberant testset: 150 noisy samples; LibriSpeech: 960 hours (and clean-100 hour subset); pretrained uLM trained on a 6K-hour "clean" subset selected from LibriLight 60K; LSTM language models trained on LibriLight medium segmented set (5.6K hours) and a larger subset (~16.8K hours).

**Format**: Raw audio waveforms (speech), represented as sequences of discrete tokens after tokenization/quantization

**Annotation**: VoiceMOS: For each utterance, 8 human judgments are collected and the average score is used as ground truth human judgement. DNS testset: synthetic noisy speech with varying SNR values. Other training corpora (LibriSpeech/LibriLight) are used as speech-only data without MOS annotations.

## 🔬 Methodology

**Methods**:
- Automated metric: SpeechLMScore computed as average log-probability from a pretrained speech-unit language model (uLM) after tokenizing speech into discrete units
- Train and evaluate LSTM unit language models (with/without repeated tokens) on LibriLight subsets
- Comparison with supervised MOS prediction models (MOSNet, DNSMOS)
- Correlation analysis between SpeechLMScore and human MOS / SNR using LCC, SRCC, KTAU

**Metrics**:
- Average log-probability (SpeechLMScore)
- Linear Correlation Coefficient (LCC)
- Spearman Rank Correlation Coefficient (SRCC)
- Kendall Tau (KTAU)

**Calculation**: SpeechLMScore(d | θ) = (1/T) * sum_{i=1..T} log p(d_i | d_{<i}; θ). Given a waveform x, encode into discrete tokens d = {d1..dT} using a tokenizer (encoder + quantizer), then iteratively compute log-probability of each token given previous tokens using the unit language model and average these log-probabilities. Correlations (LCC, SRCC, KTAU) are computed between SpeechLMScore and human MOS or SNR as reported.

**Interpretation**: Higher SpeechLMScore (higher average log-likelihood / lower perplexity) indicates higher estimated naturalness/quality and should correlate with higher human MOS. Correlation statistics (LCC, SRCC, KTAU) quantify alignment with human judgments or SNR.

**Baseline Results**: Compared to supervised MOS prediction models, MOSNet fine-tuned on the VoiceMOS dataset (MOSNet (ft)) achieves the highest correlation on matched testsets. SpeechLMScore variants generally show higher correlation than DNSMOS in many settings and show encouraging correlations despite being unsupervised. (Specific correlation tables and values are provided in the paper.)

**Validation**: Validated by measuring correlation with human MOS on the VoiceMOS challenge dataset (testset and whole set) and by measuring correlation with signal-to-noise ratio on the Deep Noise Suppression 2020 noisy reverberant testset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
