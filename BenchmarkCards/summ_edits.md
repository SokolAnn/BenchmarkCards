# SUMM EDITS

## 📊 Benchmark Details

**Name**: SUMM EDITS

**Overview**: SUMM EDITS is a 10-domain benchmark and a protocol to evaluate factual inconsistency detection in summaries (inconsistency detection). The benchmark is created via a three-step protocol (seed summary verification, generation of edited summaries, annotation of edited summaries) designed to produce atomic edits that are easy for human annotators to judge, yielding high reproducibility and low cost. The authors report the benchmark is 20 times more cost-effective per sample than previous benchmarks, estimate inter-annotator agreement at about 0.9, and find most LLMs struggle on SUMM EDITS with performance substantially below estimated human performance.

**Data Type**: Document-summary pairs (text)

**Domains**:
- News
- Podcast
- BillSum
- Samsum
- Shakespeare
- SciTLDR
- QMSum
- ECTSum
- Sales Email
- Sales Call

**Similar Benchmarks**:
- FactCC
- SummEval
- Polytope
- FRANK
- CLIFF
- AggreFact
- DialSummEval
- SummaC
- QAFactEval

**Resources**:
- [GitHub Repository](https://github.com/salesforce/factualNLG)
- [Resource](https://arxiv.org/abs/2305.14540)

## 🎯 Purpose and Intended Users

**Goal**: Provide a reproducible, low-cost, multi-domain benchmark and a protocol to evaluate LLMs' ability to detect factual inconsistencies in summaries (a binary detection task: consistent vs inconsistent) and to encourage reporting of model performance on factual inconsistency detection. The protocol also aims to enable low-cost, in-domain benchmark creation.

**Target Audience**:
- LLM developers
- NLP practitioners
- Model developers
- ML researchers
- Practitioners requiring specific domain expertise

**Tasks**:
- Factual Consistency Detection (binary classification: consistent vs inconsistent)
- Explanation generation for inconsistency predictions
- Fine-grained inconsistency detection (per edit/error type)

**Limitations**: SUMM EDITS consists of synthetic edits of seed summaries, so the benchmark cannot directly provide insights on summarizers and their ability to remain consistent. The choice of LLM used to generate edits (ChatGPT in this work) may affect the benchmark and could favor models similar to the one used for benchmark creation.

**Out of Scope Uses**:
- Direct evaluation of summarizer generation quality or summarizer ability to avoid generating inconsistencies (the benchmark uses synthetic edits and thus does not directly measure summarizer generation behavior)

## 💾 Data

**Source**: Created via the SUMM EDITS protocol applied to ten domains. Sources include: News (Google News top events feed, Feb 2023), Podcast (Spotify podcast transcripts), BillSum (US bills), SamSum (dialogue dataset), Shakespeare (Tiny Shakespeare corpus), SciTLDR (research paper abstracts / TLDRs), QMSum (meeting summarization), ECTSum (earnings call transcripts), and synthetic Sales Email and Sales Call samples generated with ChatGPT. Seed summaries were either human-written or generated (ChatGPT/ChatGPT-derived) and verified manually.

**Size**: 6,348 edited-summary samples overall. Per-domain counts: News 819, Podcast 500, BillSum 853, SamSum 664, Shakespeare 814, SciTLDR 466, QMSum 431, ECTSum 668, Sales Email 613, Sales Call 520.

**Format**: N/A

**Annotation**: Manual annotation by two professional annotators (compensated $20/hour) following the three-step protocol: seed verification and labeling of edited summaries. Each edited summary labeled as consistent, inconsistent, or borderline. At least 20% of samples per domain were annotated by multiple annotators. Reported inter-annotator agreement (Cohen's Kappa) per domain 0.72-0.90 (average 0.82 with all three labels), and average Cohen's Kappa 0.92 after removing borderline samples; authors estimate inter-annotator agreement about 0.9.

## 🔬 Methodology

**Methods**:
- Automated metrics (balanced accuracy, precision, recall, F1)
- Human evaluation (manual annotation of edited summaries and of model-generated explanations)
- Model-based evaluation (zero-shot LLM evaluation with standardized prompts; specialized non-LLM baselines)
- Oracle evaluation (providing seed summary to model as additional input for analysis)

**Metrics**:
- Balanced Accuracy
- Accuracy
- Precision
- Recall
- F1 Score
- Correlation
- Cohen's Kappa (annotator agreement)

**Calculation**: Benchmark is framed as a binary detection task (consistent vs inconsistent). Balanced accuracy is computed for binary classification results. Precision and recall are reported for fine-grained per-error-type detection experiments. F1 and recall reported for the edit-type annotation classifier (prompt-based). Correlation and transformed binary labels used for comparisons on other benchmarks (e.g., DialSummEval).

**Interpretation**: Human performance on SUMM EDITS is estimated at about 90%+. Models approaching this level indicate strong performance. The authors note that most models perform substantially below estimated human performance (e.g., GPT-4 is reported ~8% below estimated human performance). Lower balanced accuracy (closer to random chance) indicates poor factual inconsistency detection.

**Baseline Results**: Selected results on SUMM EDITS (Balanced Accuracy, overall): QAFactEval (specialized non-LLM): 65.7; Dav003: 70.7; PaLM2-Bison: 69.0; GPT3.5-turbo: 71.3; GPT4: 82.4; GPT4 Oracle: 88.9; Human Performance (estimate): 90.9. (Values are reported in Table 9 of the paper.)

**Validation**: Validation of the benchmark included: computing inter-annotator agreement (Cohen's Kappa) on multi-annotated samples; removing 'borderline' labels to improve reproducibility (Cohen's Kappa rises to 0.92); estimating human performance on the plurally annotated subset. The authors also ran experiments across ten domains and report per-domain IAA and per-domain model performance to validate multi-domain behavior.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance
- Explainability

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of testing diversity, Incomplete usage definition, Lack of data transparency
- **Explainability**: Unexplainable output

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
