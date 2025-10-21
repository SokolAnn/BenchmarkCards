# The RealTalk Dataset

## 📊 Benchmark Details

**Name**: The RealTalk Dataset

**Overview**: Our dataset, The RealTalk Dataset, contains videos of natural, unscripted conversations between two people, who come from diverse demographic backgrounds and discuss a wide range of topics and emotions.

**Data Type**: video (dyadic conversation videos)

**Domains**:
- Computer Vision
- Natural Language Processing
- Healthcare
- Assistive Technology
- Augmented Reality

**Similar Benchmarks**:
- Learning2Listen

**Resources**:
- [Resource](https://realtalk.cs.columbia.edu)
- [Resource](https://arxiv.org/abs/2301.10939)

## 🎯 Purpose and Intended Users

**Goal**: We use our data as a benchmark to evaluate our method on goal-conditioned listener retrieval.

**Target Audience**:
- Computer Vision researchers

**Tasks**:
- Video Retrieval
- Modeling Facial Expressions
- Multimodal Reasoning

**Limitations**: Lack of multi-modal speaker context; Temporal speaker-listener misalignment; Language model failures (GPT-3 hallucinations).

**Out of Scope Uses**:
- Using the framework or data to misappropriate listener identities
- Using the framework or data to construe fake conversations

## 💾 Data

**Source**: 692 in-the-wild videos from The Skin Deep YouTube channel

**Size**: 692 videos; total 115 hours of raw data; average slightly over 10 minutes per video

**Format**: Video files at 25 frames per second and 1280x720 resolution; released with precomputed ASR transcripts, visual embeddings, and speaker annotations

**Annotation**: Transcripts generated with automatic speech recognition (ASR); speaking individual(s) annotated using active speaker detection; frames filtered with off-the-shelf face detection; visual embeddings and EMOCA-based expression parameters computed

## 🔬 Methodology

**Methods**:
- Automated perceptual metrics (feature-space distances)
- Retrieval evaluation (Recall@k, median rank)
- Human evaluation (two-alternative forced choice)

**Metrics**:
- Perceptual Loss (L2 distance in representation space of pretrained face models: VGG-Face, FaceNet, FaceNet-512, DeepFace)
- Recall@k
- Median retrieval rank (M. Rank)
- Human preference percentage (2-alternative forced choice)

**Calculation**: Perceptual loss: L2 distance between predicted listener and ground-truth listener in feature spaces of VGG-Face, FaceNet, FaceNet-512, and DeepFace. Recall@k: fraction of speakers in the evaluation set for whom the corresponding ground-truth listener is ranked among the top k predictions. Median rank: ground-truth listener's median retrieval rank. Human studies: 2AFC where participants choose the more socially-appropriate listener.

**Interpretation**: Lower perceptual loss indicates closer similarity to ground-truth (better). Higher Recall@k indicates better retrieval performance. Lower median rank indicates better retrieval. Higher human preference percentage indicates retrieved listeners judged more socially-appropriate.

**Baseline Results**: Retrieval results on 407-sample test set (retrieval bank 1896 videos): Social Response (ours) R@500=0.31, R@1000=0.56, M. Rank=834; w/o CLIP Tuning R@500=0.29, R@1000=0.60, M. Rank=830; w/o Keyframes R@500=0.31, R@1000=0.56, M. Rank=895; Learning2Listen R@500=0.26, R@1000=0.50, M. Rank=996; Random Chance R@500=0.26, R@1000=0.52, M. Rank=948; Rude Response (ours) R@500=0.22, R@1000=0.47, M. Rank=1061. Perceptual losses: our socially-correct listeners yield the lowest perceptual loss across tested pretrained face models (VGG-Face, FaceNet, FaceNet-512, DeepFace).

**Validation**: Dataset split into 1896 clips (15.36s each): 1489 clips used to train visual prompt, 407 clips used for evaluation; full set of 1896 used as retrieval databank. Validation includes automated perceptual metrics and human studies: 2AFC human evaluations on a curated subset of 30 speakers with 4 evaluators per comparison (120 evaluations per comparison group).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Misuse
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias
- **Misuse**: Nonconsensual use, Spreading disinformation
- **Robustness**: Hallucination

**Potential Harm**: ['misappropriate listener identities', 'construe fake conversations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The RealTalk Dataset is constructed from publicly-available YouTube videos of real people who have consented to be filmed discussing their lives.

**Data Licensing**: Not Applicable

**Consent Procedures**: Videos are publicly-available YouTube videos of real people who have consented to be filmed.

**Compliance With Regulations**: Not Applicable
