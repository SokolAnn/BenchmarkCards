# TechSumBench

## 📊 Benchmark Details

**Name**: TechSumBench

**Overview**: TechSumBench is the first Stack Overflow query-focused multi-answer summarization benchmark to enable automatic evaluation of answer summarization for technical queries on Software Question & Answer (SQA) sites. The benchmark contains 111 query-summary pairs extracted from 382 Stack Overflow answers with 2,014 sentence candidates (37 technical questions, each with three independent ground-truth extractive summaries of five sentences).

**Data Type**: question-answering pairs (technical query, multiple answers, extractive summaries)

**Domains**:
- Software Engineering
- Natural Language Processing

**Similar Benchmarks**:
- CNN/Daily Mail
- GigaWord
- DUC-2005
- DUC-2007

**Resources**:
- [GitHub Repository](https://github.com/TechSumBot/TechSumBot)
- [Resource](https://archive.org/details/stackexchange)
- [Resource](https://stackoverflow.com/help/duplicates)

## 🎯 Purpose and Intended Users

**Goal**: Enable automatic evaluation (as a complement to user studies) of answer summarization methods for technical queries on Stack Overflow by providing ground-truth extractive summaries in a repeatable and identical evaluation setting.

**Target Audience**:
- Software Engineering researchers
- Natural Language Processing researchers

**Tasks**:
- Extractive Summarization
- Query-focused Summarization
- Question Answering

**Limitations**: Current version may contain subjective bias due to limited size of the benchmark and annotators' background and judgment preferences; authors mitigate by providing multiple ground-truth summaries per query and by making the benchmark extendable.

## 💾 Data

**Source**: Constructed from Stack Overflow data dump PostLinks table (duplicate question links). For each annotation unit, the title of the original question is treated as the technical query; relevant answers include answers to the original question and its duplicates. Focused on posts tagged with 'Java' or 'Python'; only questions with 10–15 answers considered; answers with no votes or only code snippets were discarded.

**Size**: 111 query-summary pairs; 382 Stack Overflow answers; 2,014 sentence candidates; 37 technical questions (each with three ground-truth summaries).

**Format**: N/A

**Annotation**: Manual annotation by six annotators (PhD students with ≥2 years Java/Python experience) via a two-phase labeling process: (1) Useful sentence selection (binary labels: useful / not-useful / ?), with iterative guideline refinement until inter-annotator agreement reached Moderate (average Kappa = 0.43); (2) Summary generation: annotators select five extractive sentences from the useful sentences considering clarity, redundancy, and importance. Final benchmark contains three independent ground-truth extractive summaries per question.

## 🔬 Methodology

**Methods**:
- Automated metrics (ROUGE)
- Human evaluation (5-point Likert for usefulness and diversity)
- Ablation study

**Metrics**:
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Average usefulness score (5-point Likert)
- Average diversity score (5-point Likert)

**Calculation**: For automatic evaluation, compute ROUGE-N (n=1,2) and ROUGE-L between each system-generated summary and each ground-truth summary, then compute the mean of the ROUGE scores across ground-truth summaries. Human evaluation: participants provide 5-point Likert scores (1 = extremely useless / extremely redundant, 5 = extremely useful / extremely diverse); report average scores.

**Interpretation**: Higher ROUGE scores indicate greater n-gram (ROUGE-N) or longest common subsequence (ROUGE-L) overlap with ground-truth summaries. Higher Likert scores indicate greater perceived usefulness or diversity by human judges.

**Baseline Results**: Upper Bound (assuming human-annotated summaries as ideal): ROUGE-1=0.784, ROUGE-2=0.697, ROUGE-L=0.772. Baselines (ROUGE-1 / ROUGE-2 / ROUGE-L): AnswerBot: 0.490 / 0.276 / 0.456; LexRank: 0.501 / 0.289 / 0.448; Biased-TextRank: 0.428 / 0.217 / 0.400; QuerySum: 0.508 / 0.284 / 0.476. TechSumBot (authors' approach) on TechSumBench: ROUGE-1=0.563, ROUGE-2=0.377, ROUGE-L=0.536. Human evaluation (average scores): AnswerBot usefulness=3.68, diversity=3.62; QuerySum usefulness=3.80, diversity=3.64; TechSumBot usefulness=4.02, diversity=4.26.

**Validation**: Iterative guideline refinement for useful sentence selection until inter-annotator agreement reached Moderate (average Kappa = 0.43). Discarded annotation units with slight agreement. Final dataset contains 37 annotation units each labeled with three independent extractive summaries (resulting in 111 query-summary pairs).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Governance**: Incorrect risk testing

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
