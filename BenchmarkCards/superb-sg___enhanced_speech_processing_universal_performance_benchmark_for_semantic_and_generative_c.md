# SUPERB-SG : Enhanced Speech processing Universal PERformance Benchmark for Semantic and Generative Capabilities

## 📊 Benchmark Details

**Name**: SUPERB-SG : Enhanced Speech processing Universal PERformance Benchmark for Semantic and Generative Capabilities

**Overview**: We introduce SUPERB-SG, a new benchmark focused on evaluating the semantic and generative capabilities of pre-trained models by increasing task diversity and difficulty over SUPERB. It uses a lightweight methodology that freezes pre-trained model parameters and only trains simple task-specific downstream heads to test robustness of learned representations under domain and quality shifts across diverse speech tasks.

**Data Type**: audio (speech); audio-to-text pairs; audio-to-audio pairs

**Domains**:
- Natural Language Processing
- Speech Processing

**Languages**:
- English
- Spanish (Mexican Spanish)
- Mandarin
- Arabic
- German

**Similar Benchmarks**:
- SUPERB
- LeBenchmark
- Zero Resource Speech Benchmark 2021
- HEAR 2021 Challenge

**Resources**:
- [GitHub Repository](https://github.com/s3prl/s3prl)
- [Resource](https://superbbenchmark.org)
- [Resource](https://arxiv.org/abs/2203.06849)
- [Resource](https://neuralaudio.ai/hear2021-holistic-evaluation-of-audio-representations.html)

## 🎯 Purpose and Intended Users

**Goal**: Evaluate the semantic and generative capabilities of self-supervised pre-trained speech models by adding five new tasks and increasing task diversity and difficulty over SUPERB, while using a lightweight, resource-efficient evaluation methodology.

**Target Audience**:
- ML Researchers
- Model Developers
- Speech and Audio Research Community

**Tasks**:
- Speech Translation
- Out-of-domain Automatic Speech Recognition
- Voice Conversion
- Speech Separation
- Speech Enhancement

**Limitations**: N/A

## 💾 Data

**Source**: CoVoST2 (En→De) for Speech Translation; Common Voice 7.0 (Mexican Spanish, Mandarin, Arabic subsets) and Santa Barbara Corpus of Spoken American English for Out-of-domain ASR; VCC2020 (any-to-one) for Voice Conversion; LibriSpeech-based simulated dataset and WHAM! noise for Speech Separation; Voicebank-DEMAND for Speech Enhancement. Also uses datasets from original SUPERB tasks (e.g., LibriSpeech).

**Size**: Speech Translation (CoVoST2): train 425.8 hours, val 25.9 hours, test 24.5 hours. OOD-ASR cross-lingual train hours: Mexican Spanish 21.5 hours (val 1.2h, test 0.6h), Mandarin 31.2 hours (val 14.4h, test 15.3h), Arabic 30.7 hours (val 12.24h, test 12.5h). OOD-ASR spontaneous (SBCSAE): 16.7 hours (val 1.6h, test 2.2h). Voice Conversion: 60 utterances (~5 minutes) for training, 25 utterances (~2 minutes) for testing. Speech Separation: train 43.3 hours, eval 4.2 hours (16 kHz, 2-speaker mix_clean condition). Speech Enhancement (Voicebank-DEMAND): train 8.8 hours, val 0.6 hours, test 0.6 hours.

**Format**: N/A

**Annotation**: Official dataset annotations as provided by respective datasets (e.g., transcriptions and translations for CoVoST2 and Common Voice; parallel/target speaker data for VCC2020; simulated mixture targets for LibriSpeech/WHAM!; clean/noisy pairs for Voicebank-DEMAND).

## 🔬 Methodology

**Methods**:
- Lightweight fine-tuning with frozen upstream (pre-trained) models and trainable task-specific downstream heads
- Automated metric-based evaluation
- Spearman's rank correlation analysis between tasks
- Ablation studies on downstream architectures and training data size to test robustness

**Metrics**:
- Case-sensitive de-tokenized BLEU (reported using sacreBLEU)
- Word Error Rate (WER)
- Character Error Rate (CER) for Mandarin
- Mel-Cepstrum Distortion (MCD)
- Automatic Speaker Verification (ASV) accept rate
- Scale-Invariant Signal-to-Distortion Ratio improvement (SI-SDRi)
- Perceptual Evaluation of Speech Quality (PESQ)
- Short-Time Objective Intelligibility (STOI)

**Calculation**: BLEU: case-sensitive de-tokenized BLEU reported using sacreBLEU. WER: averaged across OOD-ASR sub-tasks; Mandarin uses CER. ASR inference: CTC greedy decoding without language model re-scoring. Other metrics used as provided by standard implementations for MCD, ASV accept rate, SI-SDRi, PESQ, and STOI.

**Interpretation**: Metrics marked as higher-the-better or lower-the-better per task (paper indicates which direction per metric). The paper reports that no single upstream model outperforms all others across all tasks; HuBERT-Large is most competitive on linguistic and semantic tasks; FBANK can be competitive on some generative tasks.

**Baseline Results**: Baseline (FBANK) results reported in Table 2 (examples): ST BLEU 2.32; OOD-ASR avg WER 63.58; VC MCD 8.47; VC WER 38.3; VC ASV 77.25; SS SI-SDRi 9.23; SE PESQ 2.55; SE STOI 93.6.

**Validation**: Each experiment is performed as a single run with the same seed. Robustness validated via ablation studies over downstream model architectures (small/default/large) and by sub-sampling training data (100%, 10%, 5%, 1%) to test stability of rankings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Governance
- Data Laws

**Atlas Risks**:
- **Governance**: Incorrect risk testing
- **Data Laws**: Data usage restrictions
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: No new data collection was performed; the work uses public datasets and follows common preprocessing steps. The paper states there was no data collection involved and does not describe additional anonymization procedures.

**Data Licensing**: Datasets and licenses as stated in the paper: CoVoST2 (CC0), Common Voice 7.0 (CC0), Santa Barbara Corpus of Spoken American English (CC BY-ND 3.0), VCC2020 (ODbL), LibriSpeech/LibriLight (public domain/various), Librimix (CC BY 4.0), WHAM! (CC BY-NC 4.0), Voicebank-DEMAND (CC BY 4.0). The paper states that dataset licenses are clearly indicated and they follow the licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
