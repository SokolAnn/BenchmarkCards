# A Crowdsourced Frame Disambiguation Corpus with Ambiguity

## 📊 Benchmark Details

**Name**: A Crowdsourced Frame Disambiguation Corpus with Ambiguity

**Overview**: Resource for FrameNet semantic frame disambiguation of over 5,000 word-sentence pairs from the Wikipedia corpus. Annotations were collected using crowdsourcing with multiple workers per sentence to capture inter-annotator disagreement and are provided as lists of candidate frames with disagreement-based scores expressing the confidence each frame applies to the word. Includes ~1,000 sentence-word pairs whose lemmas are not part of FrameNet. Presents evaluation metrics that account for ambiguity.

**Data Type**: text (sentence-word pairs with candidate frames and disagreement-based confidence scores)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- FrameNet
- Framester

**Resources**:
- [Resource](http://crowdtruth.org)
- [Resource](https://mturk.com/)
- [GitHub Repository](https://github.com/CrowdTruth/CrowdTruth-core)

## 🎯 Purpose and Intended Users

**Goal**: Provide a crowdsourced FrameNet frame disambiguation corpus that preserves inter-annotator disagreement by providing confidence scores (FSS) for candidate frames, and to propose evaluation metrics that account for ambiguity when evaluating frame disambiguation systems.

**Target Audience**:
- Natural Language Processing researchers
- Model developers

**Tasks**:
- Semantic Frame Disambiguation

**Limitations**: Candidate words restricted to verbs; candidate words limited to at most 25 candidate frames; corpus size at submission was 5,042 sentence-word pairs (noting it has since grown to over 9,000); crowd annotators can make mistakes which appear in the corpus; coverage issues where FrameNet/Framester may be missing frames for some lexical units.

## 💾 Data

**Source**: Sentences sampled from the Wikipedia corpus; candidate frames gathered from FrameNet release 1.7 and expanded using Framester mapping to WordNet synsets.

**Size**: 5,042 sentence-word pairs (paper notes corpus has since grown to over 9,000 sentence-word pairs); 742 unique frames; 1,705 unique lexical units; ~1,000 sentence-word pairs with lexical units not in FrameNet.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with 15 workers per sentence, paid $0.05 per judgment; annotations aggregated using the CrowdTruth metrics to produce frame-sentence scores (FSS) and sentence quality scores (SQS), plus worker and frame quality measures.

## 🔬 Methodology

**Methods**:
- Crowdsourcing (Amazon Mechanical Turk, 15 workers per sentence)
- CrowdTruth aggregation (disagreement-aware aggregation producing FSS and SQS)
- Baseline model evaluation (Open-Sesame (OS), modified OS+, Framester rule-based tool (FS), and TC top-crowd corpus)

**Metrics**:
- Kendall's tau (list ranking coefficient)
- Cosine similarity
- Area Under Curve (AUC) aggregated over corpus
- SQS-weighted average (w-avg)

**Calculation**: Per-sentence scores: Kendall's tau in [-1,1] for ranking agreement and cosine similarity in [0,1] using FSS values. Aggregate statistics: (1) area-under-curve (AUC) for each metric normalized by corpus size, and (2) SQS-weighted average (w-avg) which accounts for sentence ambiguity via SQS.

**Interpretation**: High FSS indicates a frame is clearly expressed in a sentence; high SQS indicates overall worker agreement (a clear sentence). Kendall's tau measures agreement in ranking of frames; cosine similarity uses actual FSS values. AUC and SQS-weighted averages summarize performance across the corpus and account for ambiguity.

**Baseline Results**: Restricted set (R-SET, 4,000 sentences with LUs from FrameNet) and Full set (F-SET, 5,042 sentences):
R-SET Kendall's AUC: OS 0.339, OS+ 0.477, FS 0.279, TC 0.466. R-SET Kendall's w-avg: OS 0.362, OS+ 0.497, FS 0.300, TC 0.480. R-SET Cos Sim AUC: OS 0.57, OS+ 0.685, FS 0.518, TC 0.818. R-SET Cos Sim w-avg: OS 0.608, OS+ 0.717, FS 0.545, TC 0.854.
F-SET Kendall's AUC: OS 0.269, OS+ 0.379, FS 0.253, TC 0.491. F-SET Kendall's w-avg: OS 0.307, OS+ 0.421, FS 0.284, TC 0.501. F-SET Cos Sim AUC: OS 0.453, OS+ 0.544, FS 0.511, TC 0.810. F-SET Cos Sim w-avg: OS 0.515, OS+ 0.607, FS 0.539, TC 0.849.

**Validation**: Evaluation performed on two sets: restricted set (R-SET) of 4,000 sentences with lexical units from FrameNet, and full set (F-SET) of 5,042 sentences. Metrics include per-sentence Kendall's tau and cosine similarity, aggregated via AUC and SQS-weighted averages to validate the corpus utility and compare baseline systems.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data, Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
