# MARBLE (Music Audio Representation Benchmark for Universal Evaluation)

## 📊 Benchmark Details

**Name**: MARBLE (Music Audio Representation Benchmark for Universal Evaluation)

**Overview**: MARBLE aims to provide a benchmark for various Music Information Retrieval (MIR) tasks by defining a comprehensive taxonomy with four hierarchy levels (acoustic, performance, score, and high-level description). It establishes a unified protocol based on 18 tasks on 12 publicly- or commercially-available datasets, providing a fair and standard assessment of open-sourced pre-trained models developed on music recordings, and offers an easy-to-use, extendable, and reproducible suite with clear statements on dataset copyright.

**Data Type**: audio (music recordings; includes line-level lyrics transcripts and other annotations)

**Domains**:
- Music Information Retrieval

**Languages**:
- English
- French
- Spanish
- Italian
- German
- Russian

**Similar Benchmarks**:
- GLUE
- SuperGLUE
- ERASER
- VTAB
- VISSL
- SUPERB
- HEAR

**Resources**:
- [Resource](https://marble-bm.shef.ac.uk)
- [GitHub Repository](https://github.com/a43992899/MARBLE-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: Provide a comprehensive benchmark for evaluating pre-trained music audio representations across a taxonomy of MIR tasks, with a unified protocol, standardised preprocessing and data splitting, and an evaluation toolkit to ensure fair and reproducible assessment.

**Target Audience**:
- Music Information Retrieval researchers
- Audio and AI researchers
- Model developers

**Tasks**:
- Key Detection
- Music Tagging
- Genre Classification
- Emotion Recognition
- Pitch Classification
- Beat Tracking
- Melody Extraction
- Chord Estimation
- Lyrics Transcription
- Vocal Technique Detection
- Singer Identification
- Instrument Classification
- Source Separation

**Limitations**: Generative tasks are currently outside the scope of the initial MARBLE release. Some tasks include only one or two evaluation metrics due to copyright issues preventing many datasets from being publicly available, lack of standard pre-processing or maintenance, and time limitations. Some datasets are insufficient for a single task (e.g., GTZAN has less than 10 hours and does not have a commercially-available license, making evaluation more subject to bias). MIR on symbolic music is not included in the first version.

**Out of Scope Uses**:
- Generative tasks are currently outside our scope.
- MIR on symbolic music is not included in the first version of our benchmark.

## 💾 Data

**Source**: Publicly or commercially available datasets curated into MARBLE, including (but not limited to) Giantsteps (and Giantsteps-MTG-keys subset), MagnaTagATune (MTT), MTG-Jamendo (MTG), GTZAN, Emomusic, Nsynth, GTZAN Rhythm, MelodyDB/MedleyDB, GuitarSet, MulJam2.0 (derived from MulJam), Jamendo, VocalSet, MUSDB18, and MTG-instrument.

**Size**: Various per dataset. Examples explicitly stated: MagnaTagATune: 25.9k clips (170 hours); MTG-Jamendo: 55k clips (nearly 2,000 hours); Nsynth: ~340 hours (306,000 tracks); MedleyDB: 108 tracks (7.3 hours); MUSDB18: 150 tracks (~10 hours); MulJam: 6,031 songs (~153k lines); VocalSet: 10.1 hours; GTZAN filtered: 930 tracks (~8 hours).

**Format**: Raw audio files (clips and full tracks) with associated annotations (tags, labels, timestamps, frame-level annotations, lyrics transcripts) and provided preprocessing code/toolkits.

**Annotation**: Manual human annotations as provided by each dataset (e.g., manual tags in MagnaTagATune, valence/arousal scores in Emomusic, performed/instructed chord annotations in GuitarSet, line-level lyrics annotations in MulJam2.0), with some derived/aligned annotations (e.g., MulJam2.0 line-level annotations aligned using Whisper and human annotation).

## 🔬 Methodology

**Methods**:
- Automated metrics (task-specific)
- Unified evaluation protocol with three tracks: unconstrained, semi-constrained, and constrained
- Pre-trained models used as frozen or fine-tuned backbones providing representations; task-specific prediction heads trained per task
- Evaluation toolkit and standardized preprocessing/data splits provided

**Metrics**:
- Accuracy
- ROC-AUC (Receiver Operating Characteristic - Area Under Curve)
- PR-AUC / Average Precision (AP)
- F-measure (beat tracking, 20 ms tolerance)
- R2 (determination coefficient) for valence and arousal
- Character Error Rate (CER)
- Word Error Rate (WER)
- Source-to-Distortion Ratio (SDR)
- mir_eval chord metrics: root, majmin, mirex, thirds, triads, sevenths, majmin_inv, sevenths_inv

**Calculation**: Task-specific calculations as described in the paper: music tagging uses macro-average of tag ROC-AUCs and AP; beat tracking uses F-measure with a 20 ms tolerance (mir_eval); key detection uses accuracy with an error tolerance weighted score granting partial credit; melody extraction uses Overall Accuracy metric from mir_eval; chord estimation uses six mir_eval measures plus two additional measures (majmin_inv and sevenths_inv); lyrics transcription uses CER and WER (using beam search with combined CTC and S2S scores and an LM at test time); source separation uses mean SDR across songs as defined in the referenced MDX/SDR definitions.

**Interpretation**: Higher is better for Accuracy, ROC-AUC, PR-AUC/AP, F-measure, R2, and SDR. Lower is better for WER and CER (the paper explicitly states 'WER and CER values are the less the better'). For beat tracking a prediction is correct if the difference to the ground truth is <= 20 ms. Key detection uses a weighted score granting partial credit for reasonable errors.

**Baseline Results**: MARBLE reports evaluations of 9 open-sourced pre-trained music models as baselines. Example explicit results: best performance on NSynth pitch classification reached 94.4% accuracy (MAP-MERT-v1-330M). Tables 3-5 in the paper provide constrained-track results across tasks for models including MusiCNN, CLMR, Jukebox-5B, MULE, MAP-Music2Vec, MAP-MERT variants, showing that large pre-trained models often perform best on many tasks (detailed per-task numbers are provided in Tables 3-5).

**Validation**: Use dataset-specific train/validation/test splits described per task (paper provides split strategies and references). Checkpoints are selected according to best validation results for final testing and submission. The benchmark enforces a computational wall: systems must finish each task within a week on a machine equipped with a single consumer GPU (RTX3090). The constrained track restricts hyper-parameter search space and uses frozen backbones with standardized lightweight heads (detailed in Appendix A).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Mixed: MARBLE uses a mixture of publicly and commercially-available datasets. The paper explicitly notes some datasets are commercially available; examples in the paper/table include GuitarSet and Jamendo (MIT) and also notes GTZAN does not have a commercially-available license. The benchmark provides clear statements on dataset copyright and allows partial submissions for tasks on commercially-available datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
