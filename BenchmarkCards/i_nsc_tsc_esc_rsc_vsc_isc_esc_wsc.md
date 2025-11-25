# I/n.sc/t.sc/e.sc/r.sc/v.sc/i.sc/e.sc/w.sc

## 📊 Benchmark Details

**Name**: I/n.sc/t.sc/e.sc/r.sc/v.sc/i.sc/e.sc/w.sc

**Overview**: I/n.sc/t.sc/e.sc/r.sc/v.sc/i.sc/e.sc/w.sc : a large-scale (105K conversations) media dialog dataset collected from news interview transcripts. The dataset contains speaker role annotations for each turn and is presented as a benchmark for speaker role modeling and speaker change detection in open-domain media dialog.

**Data Type**: transcribed spoken dialog (text)

**Domains**:
- Natural Language Processing
- Media/Broadcast

**Similar Benchmarks**:
- DailyDialog
- CALLHOME
- Reddit threads (as used by DialoGPT)
- Switchboard

**Resources**:
- [Resource](https://www.kaggle.com/shuyangli94/interview-npr-media-dialog-transcripts)
- [Resource](https://www.npr.org/)
- [Resource](https://arxiv.org/abs/2004.03090)

## 🎯 Purpose and Intended Users

**Goal**: Provide a large-scale open-domain media dialog dataset with speaker role annotations to serve as a benchmark for role modeling (role-conditioned dialog generation) and role change detection (speaker change detection).

**Target Audience**:
- Conversational agent developers
- Assistive system developers
- Dialog researchers

**Tasks**:
- Role Modeling (Role-conditioned Dialog Generation)
- Role Change Detection (Speaker change detection)
- Open-domain Dialogue Modeling

**Limitations**: N/A

## 💾 Data

**Source**: Interview transcripts from National Public Radio (NPR) programs (7 programs, collected over 1999–2019).

**Size**: Full dataset: 105,848 conversations; 3,199,856 turns; 7.5 million sentences; 127 million words; 184,000 speakers; ~10,000 hours of audio (transcripts). Two-party subset (I/n.sc/t.sc/e.sc/r.sc/v.sc/i.sc/e.sc/w.sc 2P): 23,714 two-party conversations; 454,739 turns; 1.24 million sentences; 21.7 million words.

**Format**: N/A

**Annotation**: Speaker role annotations for each turn (host/guest labels in two-party subset).

## 🔬 Methodology

**Methods**:
- Automated metrics (perplexity, BLEU, etc.)
- Human evaluation (Likert-scale pairwise comparisons)
- Model fine-tuning and evaluation (fine-tuning GPT2 and DialoGPT; fine-tuning BERT for classification)

**Metrics**:
- Perplexity
- BPE Perplexity
- BLEU-1
- BLEU-4
- Noun-phrase Overlap (NPO)
- Host Matching Accuracy (HMA)
- Mean Reciprocal Rank (MRR)
- Question-asking Rate
- F1 Score

**Calculation**: Train/dev/test split: 80/10/10 with unique conversations in each split. Perplexity calculated via teacher-forcing. Host response decoding via top-k sampling with k=5. Host Matching Accuracy (HMA) and Mean Reciprocal Rank (MRR) computed by ranking the likelihood of generating a gold host response conditioned on the gold host and nine randomly sampled hosts; HMA is the proportion where the gold host is highest ranked. Role change detection evaluated as binary classification using BERT with F1 score reported.

**Interpretation**: Lower perplexity and higher BLEU indicate better language modeling/generation fidelity. Higher Noun-phrase Overlap and topical overlap indicate greater topical relatedness. Higher Host Matching Accuracy and higher Mean Reciprocal Rank indicate stronger conditioning on host profiles. Higher F1 indicates better role change detection performance. The paper reports that speaker-conditioned models have lower perplexity and higher BLEU than speaker-agnostic baselines and that inclusion of speaker labels improves role change detection F1.

**Baseline Results**: Zero-shot BPE perplexity (GPT2-based): GPT2 (no fine-tuning) reported as 35.20 on I/n.sc/t.sc/e.sc/r.sc/v.sc/i.sc/e.sc/w.sc, 57.19 on DailyDialog, 137.21 on CALLHOME. Fine-tuned on I/n.sc/t.sc/e.sc/r.sc/v.sc/i.sc/e.sc/w.sc (FT-I/n...): 17.77 (I/n...), 32.85 (DailyDialog), 51.40 (CALLHOME). Generated host responses (test set): FT DialoGPT BPE PPL 20.4; FT GPT2 BPE PPL 17.4; Speaker DialoGPT BPE PPL 15.3; Speaker GPT2 BPE PPL 17.3. Role change detection (BERT): 63.2 F1 without speaker information; 66.1 F1 with speaker labels.

**Validation**: Zero-shot out-of-domain evaluation on DailyDialog and CALLHOME. Human evaluation: 150 pairwise comparisons on a Likert scale, with human raters preferring speaker-conditioned responses 62.5% of the time. Data split uses unique conversations per split (80-10-10).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
