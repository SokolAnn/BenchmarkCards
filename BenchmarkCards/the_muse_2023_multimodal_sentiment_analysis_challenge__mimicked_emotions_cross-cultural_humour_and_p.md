# The MuSe 2023 Multimodal Sentiment Analysis Challenge: Mimicked Emotions, Cross-Cultural Humour, and Personalisation

## 📊 Benchmark Details

**Name**: The MuSe 2023 Multimodal Sentiment Analysis Challenge: Mimicked Emotions, Cross-Cultural Humour, and Personalisation

**Overview**: MuSe 2023 is a set of shared tasks addressing three multimodal affect and sentiment analysis problems: MuSe-Mimic (predict three continuous self-reported emotion intensity targets using the novel Hume-Vidmimic dataset), MuSe-Humour (cross-cultural humour detection using Passau-SFCH as training data and an English Premier League test extension), and MuSe-Personalisation (personalised prediction of continuous arousal and valence using the Ulm-Trier Social Stress Test dataset). The challenge provides pre-extracted multimodal features and baseline systems to foster comparison of approaches.

**Data Type**: multimodal: audio, video, text, and physiological biosignals (ECG, EDA, Respiration, BPM)

**Domains**:
- Affective Computing
- Natural Language Processing
- Computer Vision
- Signal Processing
- Health Informatics

**Languages**:
- English
- German

**Similar Benchmarks**:
- Passau Spontaneous Football Coach Humour (Passau-SFCH)
- Ulm-Trier Social Stress Test (Ulm-TSST)
- MuSe 2021
- MuSe 2022

**Resources**:
- [Resource](https://www.muse-challenge.org)
- [Resource](https://codalab.lisn.upsaclay.fr/)
- [GitHub Repository](https://github.com/EIHW/MuSe-2023)
- [GitHub Repository](https://github.com/audeering/opensmile)
- [GitHub Repository](https://github.com/DeepSpectrum/DeepSpectrum)
- [Resource](https://huggingface.co/audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim)
- [Resource](https://huggingface.co/bert-base-multilingual-cased)
- [Resource](https://huggingface.co/dbmdz/bert-base-german-cased)
- [GitHub Repository](https://github.com/ipazc/mtcnn)
- [Resource](https://py-feat.org)

## 🎯 Purpose and Intended Users

**Goal**: Provide a common platform and shared tasks to evaluate and compare multimodal methods for affect and sentiment analysis across three problems: mimicked emotions (multi-output regression), cross-cultural humour detection (binary classification), and personalised continuous emotion prediction (arousal and valence).

**Target Audience**:
- Audio-visual emotion recognition researchers
- Natural Language Processing researchers
- Signal Processing researchers
- Health Informatics researchers
- Affective Computing researchers
- Machine Learning researchers

**Tasks**:
- Multimodal Emotion Regression (predict continuous intensities: Approval, Disappointment, Uncertainty)
- Humour Detection (binary classification of humorous vs non-humorous 2 s frames)
- Personalised Continuous Emotion Recognition (predict continuous arousal and valence with subject-specific adaptation)

**Limitations**: N/A

## 💾 Data

**Source**: Hume-Vidmimic (new dataset for MuSe-Mimic); Passau Spontaneous Football Coach Humour (Passau-SFCH) extended with English Premier League recordings (MuSe-Humour); Ulm-Trier Social Stress Test (Ulm-TSST) recordings (MuSe-Personalisation).

**Size**: MuSe-Mimic (Hume-Vidmimic): 557 subjects, total duration 32:19:56 (30+ hours), mean clip duration 6.4 seconds. MuSe-Humour (Passau-SFCH + extension): 16 unique coaches/subjects, total duration 17:26:53 (more than 17 hours). MuSe-Personalisation (Ulm-TSST): 69 subjects, total duration 5:47:27 (circa 6 hours).

**Format**: Audio: normalized to mono, 16 kHz, 16-bit. Video: face images sampled at 2 frames per second; face detection via MTCNN. Transcripts: manual transcripts with timestamps. Biosignals (Ulm-TSST): original 1 kHz signals provided and downsampled/smoothed 2 Hz versions available. Additionally, pre-extracted feature sets (audio, video, text) are provided.

**Annotation**: MuSe-Mimic (Hume-Vidmimic): subjects self-reported intensity ratings (0–100) across selected emotion categories; target labels for three continuous intensities created via agglomerative clustering and mean intensity per seed-mimic pair. MuSe-Humour (Passau-SFCH + extension): manual annotations at 2 Hz following the Humor Style Questionnaire (HSQ), binarized to presence/absence of humour per 2 s frame. MuSe-Personalisation (Ulm-TSST): arousal and valence labelled at 2 Hz by three annotators; valence gold standard fused using RAAW; arousal fused using the two annotators with highest agreement combined with subject EDA.

## 🔬 Methodology

**Methods**:
- Automated metrics evaluation via centralized test submission on CodaLab
- Baseline model evaluation using GRU-based Recurrent Neural Network and late fusion
- Hyperparameter search with fixed random seeds and selection based on development set
- Two-stage subject-specific fine-tuning for personalisation

**Metrics**:
- Pearson’s Correlation Coefficient
- Area Under the Curve (AUC)
- Concordance Correlation Coefficient (CCC)
- Mean Squared Error (MSE) used as training loss for regression baselines
- Binary Cross-Entropy used as training loss for humour detection baseline
- CCC-Loss used for MuSe-Personalisation training

**Calculation**: MuSe-Mimic: Pearson’s correlation coefficient (ρ) computed for each of the three continuous targets and reported as mean ρ across the three targets. MuSe-Humour: AUC computed on binary humour labels at 2 s frame granularity. MuSe-Personalisation: Concordance Correlation Coefficient (CCC) reported for arousal and valence; CCC-Loss employed during training for personalisation experiments. Baseline results obtained via GRU-RNNs with hyperparameter searches and fixed seeds; late fusion averages unimodal predictions weighted by development set performance.

**Interpretation**: N/A

**Baseline Results**: MuSe-Mimic: mean Pearson’s correlation (late fusion audio+text+video) = 0.4727 on test. MuSe-Humour: Area Under the Curve (late fusion audio+text+video) = 0.8310 on test. MuSe-Personalisation: Best arousal CCC (DeepSpectrum) = 0.7482 on test; Valence CCC (late fusion audio+video) = 0.7827 on test; combined mean CCC = 0.7639 on test.

**Validation**: Datasets partitioned into speaker-independent training, development, and test sets. MuSe-Humour test set is cross-cultural (English) and distinct from German training data. Baselines validated via development set performance; hyperparameter searches run with multiple fixed seeds (typically 5) and best checkpoints selected based on development set. Test predictions submitted via CodaLab.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Explainability
- Privacy
- Dependability
- Environmental impact

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: Datasets include demographic information: Hume-Vidmimic subjects located in the United States aged 19–59. MuSe-Humour training subjects aged 30–53 (German coaches), test subjects aged 47–57 (English coaches); all coaches are male. Ulm-TSST comprises 69 subjects aged 18–39, 49 of whom are female.

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: To preserve subjects' privacy, parts of videos in which subjects disclose their names were deleted. Entry to the challenge requires an academic affiliation and acceptance of an End-User License Agreement (EULA).

**Data Licensing**: Not Applicable

**Consent Procedures**: Hume-Vidmimic subjects were recruited via Prolific and reimbursed for their time (explicit recruitment and reimbursement stated).

**Compliance With Regulations**: Not Applicable
