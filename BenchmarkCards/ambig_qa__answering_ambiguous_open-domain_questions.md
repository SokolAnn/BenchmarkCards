# AMBIG QA: Answering Ambiguous Open-domain Questions

## 📊 Benchmark Details

**Name**: AMBIG QA: Answering Ambiguous Open-domain Questions

**Overview**: A new open-domain question answering task which involves finding every plausible answer to an ambiguous question and rewriting the question for each answer to resolve the ambiguity. The paper also constructs AMBIG NQ, a dataset of annotated disambiguated question-answer pairs derived from NQ-OPEN.

**Data Type**: question-answering pairs (text)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- NQ-OPEN (Natural Questions)
- Natural Questions
- TriviaQA
- SearchQA
- BoolQ

**Resources**:
- [Resource](https://nlp.cs.washington.edu/ambigqa)
- [Resource](https://arxiv.org/abs/2004.10645)
- [GitHub Repository](https://github.com/julianmichael/spacro)
- [Resource](https://developers.google.com/custom-search/)

## 🎯 Purpose and Intended Users

**Goal**: Provide a benchmark and dataset to evaluate systems that (1) identify all semantically distinct, equally plausible answers to an open-domain question and (2) generate minimally edited, disambiguated versions of the question corresponding to each answer.

**Target Audience**:
- ML Researchers
- Natural Language Processing researchers
- Question Answering researchers

**Tasks**:
- Question Answering
- Question Rewriting / Question Disambiguation
- Open-domain Question Answering

**Limitations**: Limited annotated data for question disambiguation (the paper notes a lack of annotated data for QD). Distributional differences between NQ-OPEN development and test sets (sampling bias) affect evaluation. Metrics may miss semantically correct but differently phrased edits. The dataset contains time-dependent questions which are rewritten to reduce time-dependence.

## 💾 Data

**Source**: Prompt questions drawn from NQ-OPEN (an open-domain version of Natural Questions) with evidence from English Wikipedia; annotations collected via crowdsourcing on Amazon Mechanical Turk using a generation and validation pipeline.

**Size**: 14,042 examples

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with a two-stage pipeline: generation (workers search English Wikipedia and produce all plausible answers paired with minimal edits of the prompt question) and validation (separate validators review and combine generator outputs). For dev/test: two generators and one validator per prompt; for training: one generator per prompt. Workers were qualified via a qualification test and received feedback; generation and validation payments are reported (USD 0.75 and 0.15 per prompt).

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (baseline neural models)
- Human validation of annotations

**Metrics**:
- F1 (answers only) (F1ans)
- F1BLEU (uses BLEU as question similarity f)
- F1EDIT-F1 (uses EDIT-F1 as question similarity f)
- BLEU Score
- EDIT-F1
- Exact Match (EM)

**Calculation**: Each predicted question-answer pair (x_i, y_i) is assigned a correctness score c_i = max_{j: y_i in Y_j} f(x_i,  x_j), where f is a string-similarity function in [0,1]. precision = sum c_i / m, recall = sum c_i / n, and F1 = 2 * precision * recall / (precision + recall). F1ans sets f=1 for answer-only evaluation. F1BLEU uses BLEU to compute f; F1EDIT-F1 uses EDIT-F1 to compute f.

**Interpretation**: F1ans measures answer correctness ignoring question rewrites. F1BLEU rewards surface similarity of predicted disambiguated questions to references. F1EDIT-F1 evaluates whether the predicted edits from the prompt question match the key semantic differences in the gold edits. High F1ans with low F1EDIT-F1 indicates correct answers but poor disambiguation.

**Baseline Results**: Reported baselines on AMBIG NQ include: DISAMBIG-FIRST (dev F1ans(all)=28.1, test=24.8), Thresholding+QD (dev 37.1, test 32.3), SPANSEQGEN+QD (dev 39.7, test 33.5). Best reported baseline: SPANSEQGEN (ensemble with co-training) + QD achieved dev F1ans(all)=42.3 and test F1ans(all)=35.9. Zero-shot results (models trained only on NQ-OPEN) reported e.g., SPANSEQGEN EM on NQ-OPEN: dev 42.0 test 42.2 and corresponding F1ans on AMBIG NQ as reported in the paper.

**Validation**: Generation stage: workers search English Wikipedia (via Google Search API restricted to Wikipedia) and provide answers and minimal edited questions. Validation stage: validators review multiple generators' outputs, mark correct/incorrect, or provide combined question-answer pairs. Validation is skipped when generators exactly match (37% of cases). Inter-annotator agreement: generators vs generators 60.8 F1ans; average F1ans between co-authors and workers on a sample of validations was 89.0%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Governance

**Atlas Risks**:
- **Transparency**: Uncertain data provenance
- **Governance**: Unrepresentative risk testing
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
