# A Benchmark for Structured Procedural Knowledge Extraction from Cooking Videos

## 📊 Benchmark Details

**Name**: A Benchmark for Structured Procedural Knowledge Extraction from Cooking Videos

**Overview**: We propose a benchmark of structured procedural knowledge extracted from cooking videos. The resource is a manually annotated open-vocabulary dataset including 356 instructional cooking videos and 15,523 video clip/sentence-level annotations. The task requires models to produce interpretable structured knowledge in the form of verb-argument tuples grounded to key video clips and transcript sentences.

**Data Type**: multimodal (video clips with transcripts)

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- AllRecipes
- YouCook2
- CrossTask
- COIN
- How2
- HAKE
- TACOS
- HowTo100M

**Resources**:
- [GitHub Repository](https://github.com/frankxu2004/cooking-procedural-extraction)
- [Resource](https://arxiv.org/abs/2005.00706)
- [Resource](http://youcook2.eecs.umich.edu/)

## 🎯 Purpose and Intended Users

**Goal**: Given an instructional video and its transcript, automatically extract a sequence of procedural tuples (verb; arg1; ...; argk) describing key steps, and identify the key video clips/sentences to which these procedures are grounded.

**Tasks**:
- Structured Information Extraction
- Key Clip Selection (Temporal Localization)
- Semantic Role Labeling
- Action Recognition

**Limitations**: Explicit limitations discussed: (1) coreference and ellipsis in transcripts cause arguments/verbs to be absent or ambiguous; (2) speech-to-text errors in automatically acquired transcripts cause parsing errors; (3) domain gap between pre-trained visual/action models (e.g., EpicKitchens) and this dataset limits visual-only performance; (4) closed pre-defined label sets in action detection datasets limit open-vocabulary extraction and multimodal fusion effectiveness.

## 💾 Data

**Source**: Manually annotated subset of YouCook2 instructional videos (native English-speaker annotators annotated videos into structured verb-argument tuples grounded to video clips and transcript sentences).

**Size**: 356 videos; 15,523 video clip/sentence annotations; 3,569 clips labeled as key steps; annotations span 89 recipe types.

**Format**: N/A

**Annotation**: Manual annotation by native English-speakers. Two expert annotators plus a professional labeling supervisor for quality control. Supervisor reviewed and applied heuristic rules; 25% of annotations were modified after review. Inter-annotator agreement: Cohen's Kappa 0.83 for key-clip identification (Q1). For Q2 (procedural tuple annotation) agreement measured with Jaccard ratio: verbs 0.77, arguments 0.72.

## 🔬 Methodology

**Methods**:
- Parsing-based heuristics (semantic role labeling, unsupervised recipe segmentation)
- Neural supervised key clip selection (BERT + ResNet50 + attention)
- Video action/object detection (pretrained TSM on EpicKitchens)
- Multimodal fusion (union of utterance and visual detections)
- Automated evaluation metrics (exact and fuzzy matching)

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score
- Exact Match
- Fuzzy Matching (Levenshtein-based normalized score with optimal assignment)
- Partial Fuzzy Matching (best-substring fuzzy score)

**Calculation**: Precision = TP / #predicted, Recall = TP / #gold. True positives (TP) are computed via three matching strategies: Exact Match (string equality), Fuzzy Matching (normalized Levenshtein distance s(a,b) with optimal assignment via Kuhn-Munkres), and Partial Fuzzy Matching (best-substring fuzzy score normalized by shorter string length).

**Interpretation**: Exact Match is strict; Fuzzy Matching provides a soft normalized score using edit distance; Partial Fuzzy favors best matching substrings (biases toward shorter correct phrases). Authors advise using all three metrics jointly for holistic evaluation.

**Baseline Results**: Key clip selection (Table 4): SRL w/ heuristics Acc 61.2, Precision 35.2, Recall 81.4, F1 49.1; Neural V+T (Full Model) Acc 77.7, Precision 51.0, Recall 75.3, F1 60.8. Structured extraction (Table 5, using oracle key clips): SRL w/ heur. verbs Exact-match F1 44.3; arguments Exact-match F1 2.2; fuzzy/partial fuzzy scores higher. Visual-only and fusion baselines perform worse on arguments due to domain and label-set limitations.

**Validation**: Annotation quality validated via inter-annotator agreement (Cohen's Kappa 0.83 for key-clip identification; Jaccard ratios for tuple annotation: verbs 0.77, arguments 0.72). Supervisor reviewed annotations and corrected anomalies; test set of 356 annotated videos used for evaluation. Reproducibility details and code references provided in appendices.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
