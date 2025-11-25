# An extended benchmark

## 📊 Benchmark Details

**Name**: An extended benchmark

**Overview**: The paper formalizes benchmarking when some system scores are missing on tasks and proposes a novel approach that uses compatible partial rankings to impute missing data, aggregated using the Borda count. It provides two refinements for task-level and instance-level scores and introduces an extended benchmark containing over 131 million scores. Code and data are shared at https://github.com/AnasHimmi/MissingDataRanking.

**Data Type**: Task-level scores and instance-level scores (numeric evaluation scores) with associated input/output/reference text

**Domains**:
- Natural Language Processing
- Computer Vision

**Similar Benchmarks**:
- GLUE
- SGLUE (SuperGLUE)
- XTREME
- GEM
- BigBench
- MiniBench

**Resources**:
- [GitHub Repository](https://github.com/AnasHimmi/MissingDataRanking)
- [Resource](https://arxiv.org/abs/2305.10284)
- [Resource](https://super.gluebenchmark.com/)

## 🎯 Purpose and Intended Users

**Goal**: Address benchmarking when one or several systems cannot be evaluated on a specific task by developing aggregation methods that handle missing system scores and providing an extended benchmark for validation.

**Target Audience**:
- Researchers
- Practitioners

**Tasks**:
- Text Classification
- Structured Prediction
- Question Answering
- Sentence Retrieval
- Text Summarization
- Image Captioning
- Dialogue Evaluation
- Machine Translation
- Data-to-Text Generation
- Natural Language Generation

**Limitations**: Potential bias in the reranking process: the selection of the "best" hypothesis may favor certain perspectives or reinforce existing biases present in the training data.

## 💾 Data

**Source**: Built upon the dataset used in [31] and collected from GLUE, SGLUE, XTREME, GEM, dialogue datasets, image description datasets (Flickr, COCO), summarization datasets (TAC08, TAC10, TAC11, RSUM, SummEval), data-to-text (WebNLG), and translation datasets (WMT15, WMT16, WMT17, WMT18, WMT19, WMT20, WMT21).

**Size**: over 131 million scores

**Format**: N/A

**Annotation**: Automatic metric scores (e.g., ROUGE, BLEU, BERTScore, MoverScore, BLEURT, COMET, etc.) and available human evaluations where provided by the original datasets.

## 🔬 Methodology

**Methods**:
- Compatible partial ranking imputation (generate compatible permutations for partial rankings)
- Matrix pairwise representation of rankings
- Borda Count aggregation
- One-level aggregation (ψl)
- Two-level aggregation for instance-level (ψ2l)
- Confidence intervals for pairwise comparisons using Hoeffding inequality
- Robustness experiments via random removal of a proportion of scores

**Metrics**:
- Kendall Tau (Kendall τ) correlation coefficient
- Top-1 agreement percentage
- Top-3 agreement percentage
- ROUGE
- BLEU
- BERTScore
- MoverScore
- BLEURT
- COMET
- CharErrorRate
- TranslationEditRate
- WordErrorRate
- MatchErrorRate
- Baryscore
- DepthScore
- Infolm
- JS (Jensen-Shannon)

**Calculation**: Final ranking: combine per-task or per-instance pairwise matrices (sum over tasks/instances) to obtain combined matrix M; compute column-wise sums of M and apply argsort to obtain Borda-count ranking. Robustness measured by computing Kendall τ between rankings with and without removed scores. Confidence intervals computed via Hoeffding inequality: cij = sqrt(-log(ε) / (2 zij)), where zij is the number of comparisons.

**Interpretation**: Higher Kendall τ (closer to 1) indicates robustness of the aggregation to missing data. If 0.5 is not in the pairwise confidence interval [cM_ij - cij, cM_ij + cij], the ordering between systems i and j is considered statistically significant with high probability.

**Baseline Results**: Baseline is mean aggregation (mean of scores) denoted ψ_mean. Task-level agreement (Kendall τ) between ψl and ψ_mean: GLUE 0.17 ± 0.24; SGLUE 0.33 ± 0.27; XTREME 0.26 ± 0.26; GEM 0.36 ± 0.36 (Table 1). Instance-level correlations (Table 3): Corr. τ ψ2l vs ψl = 0.80 ± 0.22; ψl vs ψ_mean = 0.20 ± 0.28; ψ_mean vs ψ2l = 0.19 ± 0.28. Top-1/Top-3 agreement (Table 4): ψ2l vs ψl top1=0.67 top3=0.36; ψl vs ψ_mean top1=0.21 top3=0.09; ψ_mean vs ψ2l top1=0.19 top3=0.09. Additional dataset-specific top1/top3 stats in Table 2 for task-level experiments (e.g., GEM top1=0.52 top3=0.25).

**Validation**: Validated on synthetic experiments (e.g., N=20 systems, T=20 tasks, K=20 instances; experiments repeated 100 times) and extensive real-data experiments using task-level datasets (GLUE, SGLUE, XTREME, GEM) and instance-level datasets (translation WMT series, summarization TAC and SummEval, image description Flickr/COCO, WebNLG, dialogue PersonaChat/TopicalChat). Robustness assessed by randomly removing a proportion of scores and measuring Kendall τ; confidence interval analysis applied to real benchmarks (example: WMT en-de).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias, Output bias

**Potential Harm**: Selection of the "best" hypothesis or reranking may favor certain perspectives or reinforce existing biases present in the training data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
