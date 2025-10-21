# MUG (Meeting Understanding and Generation Benchmark)

## 📊 Benchmark Details

**Name**: MUG (Meeting Understanding and Generation Benchmark)

**Overview**: Establishes a general Meeting Understanding and Generation benchmark (MUG) to benchmark the performance of a wide range of spoken language processing (SLP) tasks (topic segmentation, topic-level and session-level extractive summarization, topic title generation, keyphrase extraction, and action item detection). To facilitate MUG, the authors construct and release the AliMeeting4MUG Corpus (AMC), a large-scale meeting dataset of 654 recorded Mandarin meeting sessions with manual annotations for SLP tasks, and provide baseline systems and evaluation methods.

**Data Type**: manual meeting transcripts (long-form spoken language text)

**Domains**:
- Natural Language Processing

**Languages**:
- Mandarin

**Similar Benchmarks**:
- AMI meeting corpus
- ICSI meeting corpus
- ELITR Minuting Corpus
- QMSum
- ISL meeting corpus
- NIST Meeting Room Corpus

**Resources**:
- [Resource](https://modelscope.cn/datasets/modelscope/Alimeeting4MUG/summary)
- [GitHub Repository](https://github.com/alibaba-damo-academy/SpokenNLP)

## 🎯 Purpose and Intended Users

**Goal**: Provide a general and comprehensive benchmark (MUG) and the AliMeeting4MUG Corpus to drive spoken language processing (SLP) research on meetings by defining SLP tasks, providing annotations, evaluation methods, and baseline systems.

**Target Audience**:
- Spoken Language Processing researchers
- Research community

**Tasks**:
- Topic Segmentation
- Topic-level Extractive Summarization
- Session-level Extractive Summarization
- Topic Title Generation
- Keyphrase Extraction
- Action Item Detection

**Limitations**: Current release covers Mandarin meetings only. The paper states plans to add tasks such as Question Answering and Session-level Abstractive Summarization and to cover more languages (e.g., English) in future releases. Also, 130 of the 654 meetings are annotated only with Topic Segmentation.

## 💾 Data

**Source**: AliMeeting4MUG Corpus (AMC). Extends 224 meetings from the previously released Alimeeting corpus with 430 additionally collected meetings, yielding 654 recorded Mandarin meeting sessions. Manual transcripts with manual punctuation and speaker labels; manual annotations for SLP tasks (Topic Segmentation, Topic- and Session-level Extractive Summarization, Topic Title Generation, Keyphrase Extraction, Action Item Detection). 524 meetings annotated for all 5 SLP tasks; 130 meetings annotated only for Topic Segmentation. Train/Dev/Test splits: for the 524 fully-annotated meetings: Train 295, Dev 65, Stage1 Test 82, Stage2 Test 82 (except TS-Test sets). For the 130 TS-only meetings: TSonly-Test1 65, TSonly-Test2 65.

**Size**: 654 meeting sessions; 524 meetings with all 5 SLP annotations and 130 meetings with only Topic Segmentation; Train: 295 sessions; Dev: 65 sessions; Stage1 Test: 82 sessions; Stage2 Test: 82 sessions; TSonly-Test1: 65 sessions; TSonly-Test2: 65 sessions. Avg. session length: 10,772.5 tokens (per-session average after tokenization).

**Format**: manual transcripts with manual punctuation and speaker labels (text); paragraph segmentation applied (character tokenization for Chinese).

**Annotation**: Manual transcription with manual punctuation insertion and speaker labels. Paragraph segmentation produced by a sequence model; then manual annotations applied per paragraph-segmented documents for Topic Segmentation, Topic-level and Session-level Extractive Summarization, Topic Title Generation, Keyphrase Extraction (top-K, K <= 20), and Action Item Detection. TS: one annotator then expert review; ES/TTG/KPE/AID: three annotators per document (with described aggregation: union of annotators for KPE and ES references; three reference copies for TTG; expert decision for AID disagreements). Inter-annotator agreement computed with ROUGE-1/2/L F-scores for ES/TTG, exact F1 for KPE, and Kappa for AID.

## 🔬 Methodology

**Methods**:
- Automated metrics (per-track standard metrics as described below)
- Baseline model evaluation using fine-tuned pre-trained Transformers and unsupervised KPE (YAKE)

**Metrics**:
- Positive F1
- P_k
- WinDiff
- ROUGE-1 F-score
- ROUGE-2 F-score
- ROUGE-L F-score
- Exact F1
- Partial F1
- Precision
- Recall
- F1 Score

**Calculation**: Topic Segmentation: positive F1, P_k and WinDiff; report 1-P_k and 1-WD so larger values indicate better performance. Extractive Summarization and Topic Title Generation: ROUGE-1/2/L F-scores computed with https://pypi.org/project/rouge/; references from three annotators reported as average and best ROUGE scores. Keyphrase Extraction: exact F1 and partial F1 at top-K; partial match if |LCS(i,j)| >= L with L=2 characters. Action Item Detection: positive precision, recall, and F1. P_k and WinDiff computed with segeval (https://segeval.readthedocs.io/en/latest/).

**Interpretation**: Larger metric values indicate better performance. For ES/TTG, both average and best scores across three annotator references are reported; for ES the final track score averages topic-level and session-level ROUGE scores. For TS, 1-P_k and 1-WD are used so that larger values indicate better segmentation performance. For KPE, exact matches count for Exact F1; Partial F1 allows partial string overlap as defined.

**Baseline Results**: Track 1 (Topic Segmentation) Longformer positive F1: 22.7 ± 0.98; 1-P_k: 0.583 ± 0.008; 1-WD: 0.56 ± 0.008. Track 2 (Extractive Summarization, average): Longformer R-1 Avg/Best: 53.83 ± 0.39 / 61.64 ± 0.68; R-2 Avg/Best: 32.33 ± 0.60 / 42.73 ± 0.84; R-L Avg/Best: 42.94 ± 0.61 / 53.87 ± 0.68. Track 3 (Topic Title Generation) BART R-1 Avg/Best: 32.16 ± 0.21 / 45.11 ± 0.22; R-2 Avg/Best: 17.87 ± 0.22 / 28.26 ± 0.32; R-L Avg/Best: 30.1 ± 0.26 / 43.16 ± 0.22. Track 4 (Keyphrase Extraction) YAKE Exact/Partial F1@10: 15.2 / 24.9; @15: 17.5 / 27.8; @20: 19.1 / 29.5. Track 5 (Action Item Detection) Longformer positive P: 60.18 ± 5.06; positive R: 66.89 ± 3.29; positive F1: 63.14 ± 1.41.

**Validation**: Inter-annotator agreement reported: ROUGE-1/2/L F-scores for ES and TTG between annotator pairs; exact F1 for KPE; Kappa coefficient for AID. Aggregation strategies: union of three annotators used for KPE and ES references; TTG has three reference copies for training; expert adjudication for AID disagreements. Standard train/dev/test splits provided as described in the dataset section.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The authors state they ensured all 654 meetings have no personally identifiable information, nor sensitive information about projects or organizations.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
