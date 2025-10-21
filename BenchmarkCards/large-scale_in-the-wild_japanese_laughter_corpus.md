# large-scale in-the-wild Japanese laughter corpus

## 📊 Benchmark Details

**Name**: large-scale in-the-wild Japanese laughter corpus

**Overview**: We present a large-scale in-the-wild Japanese laughter corpus comprising 3.5 hours of laughter (7489 utterances from 470 speakers) and propose pseudo phonetic tokens (PPTs) obtained by clustering HuBERT-extracted features to represent laughter; PPTs are used with a TTS model for laughter synthesis and a token language model for unconditional laughter generation. Comprehensive subjective and objective evaluations demonstrate the proposed method significantly outperforms a baseline and can generate natural laughter unconditionally.

**Data Type**: audio (single-speaker laughter utterances)

**Domains**:
- Speech Synthesis

**Languages**:
- Japanese

**Similar Benchmarks**:
- OGVC
- H-VB
- AudioSet

**Resources**:
- [Resource](https://sites.google.com/site/shinnosuketakamichi/research-topics/laughter_corpus)
- [GitHub Repository](https://github.com/Aria-K-Alethia/laughter-synthesis)
- [GitHub Repository](https://github.com/jrgillick/laughter-detection)
- [GitHub Repository](https://github.com/facebookresearch/demucs)
- [Resource](https://huggingface.co/facebook/hubert-base-ls960)
- [Resource](https://huggingface.co/facebook/wav2vec2-xlsr-53-espeak-cv-ft)
- [GitHub Repository](https://github.com/jik876/hifi-gan)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale in-the-wild Japanese laughter corpus designed for laughter synthesis and to enable evaluation of laughter synthesis methods (including synthesis from pseudo phonetic tokens and unconditional generation via a token language model).

**Tasks**:
- Speech Synthesis
- Unconditional Audio Generation

**Limitations**: MOS and SMOS cannot evaluate the diversity of the synthesized laughter subjectively.

## 💾 Data

**Source**: Collected from YouTube videos crawled using caster and YouTuber lists obtained from Wikipedia; candidate videos filtered with a pretrained laughter detector; videos labeled via crowdsourcing into single-speaker/multi-speaker/others; manual segmentation of single-speaker laughter utterances; non-Japanese videos discarded; vocal extraction/denoising performed using the Demucs pretrained model.

**Size**: 7489 utterances (about 3.5 hours) from 470 speakers; after filtering 7290 utterances used for experiments; train/validation/test split: 7110/90/90 utterances; test set consists of 30 speakers with 3 utterances per speaker.

**Format**: 16 kHz sampled waveform audio

**Annotation**: Crowdsourced labeling of detected videos by ~1500 workers into three categories (single-speaker laughter, multi-speaker laughter, others); manual segmentation of laughter utterances; denoising via Demucs source separation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Subjective evaluation (Mean Opinion Score)
- Similarity MOS (SMOS)
- Crowdsourced labeling

**Metrics**:
- Mel-cepstral distortion (MCD)
- F0 root mean square error (F0-RMSE)
- Perplexity (PPL)
- Self-BLEU
- Mean Opinion Score (MOS)
- Similarity MOS (SMOS)

**Calculation**: MCD and F0-RMSE are computed with dynamic time warping (DTW). Perplexity (PPL) is defined as the normalized inverse probability on the test set of the token language model (tLM). Self-BLEU is the average 4-gram BLEU between a generated sentence and the rest of generated sentences; a normalized Self-BLEU is used (ratio to Self-BLEU of the test set) resulting in values in [0,1]. MOS and SMOS are standard 5-point subjective tests conducted via crowd-sourcing.

**Interpretation**: MCD and F0-RMSE reflect the quality of synthesized laughter (lower is better). PPL reflects tLM performance (lower is better). Normalized Self-BLEU (in [0,1]) reflects diversity of generated sequences relative to ground truth (lower indicates higher diversity relative to GT). Higher MOS and SMOS indicate better naturalness and similarity respectively.

**Baseline Results**: Baseline method (phoneme-based via multilingual ASR + FastSpeech2): MCD = 16.59 dB, F0-RMSE = 117.65 Hz, MOS = 1.25, SMOS = 1.20. Proposed methods (PPT-based, selected layers): Proposed-L5: MCD = 11.53 dB, F0-RMSE = 80.28 Hz, MOS = 3.00, SMOS = 3.07; Proposed-L8: MCD = 11.69 dB, F0-RMSE = 82.81 Hz, MOS = 2.98, SMOS = 3.17; Proposed-L12: MCD = 11.41 dB, F0-RMSE = 81.43 Hz, MOS = 2.96, SMOS = 3.22. HiFi-GAN (vocoder from GT mel-spectrograms): MCD = 6.68 dB, F0-RMSE = 53.70 Hz, MOS = 3.31, SMOS = 4.74. (Unconditional generation MOS/SMOS: Proposed-L5 MOS=3.11 SMOS=2.65; Proposed-L8 MOS=2.80 SMOS=2.59; Proposed-L12 MOS=3.06 SMOS=2.59.)

**Validation**: Data split: train/validation/test = 7110/90/90 utterances. Subjective MOS test for synthesis: 54 listeners, each evaluated 36 utterances (3 answers per utterance). SMOS test: 45 listeners. Unconditional generation MOS test: 27 listeners, each evaluated 33 utterances (3 answers per utterance). Objective metrics computed on test set or generated PPT sequences.

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
