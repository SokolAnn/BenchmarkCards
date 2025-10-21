# APPLS

## 📊 Benchmark Details

**Name**: APPLS

**Overview**: APPLS is a granular meta-evaluation testbed designed to evaluate metrics for Plain Language Summarization (PLS). The testbed operationalizes four PLS criteria—informativeness, simplification, coherence, and faithfulness—by defining and applying controlled perturbations to texts from two scientific PLS datasets (CELLS and PLABA) and assessing sensitivity of existing automated metrics, lexical features, and LLM prompt-based evaluations.

**Data Type**: text (scientific abstract — plain language summary pairs)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/LinguisticAnomalies/APPLS)
- [Resource](https://arxiv.org/abs/2305.14341)
- [Resource](https://community.cochrane.org)
- [Resource](https://www.anthropic.com)
- [Resource](https://www.nlm.nih.gov/research/umls/)

## 🎯 Purpose and Intended Users

**Goal**: To assess how well existing evaluation metrics capture multiple criteria of plain language summarization (informativeness, simplification, coherence, and faithfulness) and to provide a granular meta-evaluation testbed (APPLS) constructed via controlled perturbations on existing PLS datasets.

**Tasks**:
- Summarization
- Text Simplification
- Metric Evaluation (Meta-evaluation)

**Limitations**: Perturbations use synthetic data which may affect multiple PLS criteria; sentence-level alignment for simplification perturbations is imperfect; study focuses on the health domain (CELLS and PLABA) and a selected set of commonly used metrics, so generalizability may be limited.

## 💾 Data

**Source**: APPLS applies controlled perturbations to candidate summaries derived from two existing PLS datasets: CELLS (Guo et al., 2024) and PLABA (Attal et al., 2023). Candidate summaries are produced via an oracle extractive selection and round-trip translation before perturbation.

**Size**: 6,311 examples (CELLS test split) and 750 examples (PLABA); (CELLS full dataset contains ~63,000 pairs but only the 6.3k test split was used for APPLS construction).

**Format**: N/A

**Annotation**: Perturbations are generated automatically. Human validation was performed: two independent annotators (both with doctorates in the biological sciences, hired on UpWork) rated samples on informativeness, simplification, faithfulness, and coherence using 5-point Likert scales; inter-rater agreement reported (Cohen's kappa = 0.48, Spearman rank correlation = 0.58).

## 🔬 Methodology

**Methods**:
- Automated metric evaluation (overlap-based and model-based metrics)
- Lexical feature analysis
- LLM prompt-based evaluation (GPT-4 prompts)
- Human evaluation (Likert ratings for validation)

**Metrics**:
- ROUGE (average of ROUGE-1, ROUGE-2, ROUGE-L)
- BLEU
- METEOR
- SARI
- GPT-PPL
- BERTScore
- LENS
- QAEval
- Lexical features: Sentence length, Paragraph length, Familiarity (percentage of 1,000 most common words), Specificity (Speciteller), Conjunction count, Function word counts (verbs, nouns, adjectives, adverbs, numbers)
- LLM prompt-based scores (0-100 scale from GPT-4)

**Calculation**: ROUGE reported as the average of ROUGE-1, ROUGE-2, and ROUGE-L. SARI uses source, generated, and target texts and weights deleted/added/kept n-grams. GPT-PPL is computed as perplexity / average log probability using GPT-family models (lower is better). BERTScore uses contextualized embeddings to compute F1 between candidate and target. QAEval computes the proportion of generated question-answer pairs correctly answered using the generated text. LLM prompt-based scores are produced by GPT-4 on a 0 (worst) to 100 (best) scale per criterion.

**Interpretation**: Sensitivity is defined as correlation in the expected direction with the amount of change in a criterion (i.e., metric scores should change monotonically with increasing perturbation magnitude). For prompt-based evaluation, scores range 0 (worst) to 100 (best). For GPT-PPL lower values indicate better fluency/coherence. Higher values are better for ROUGE, BLEU, METEOR, SARI, BERTScore, LENS, and QAEval.

**Baseline Results**: Median reported improvements in ACL'22 summarization/generation papers (contextual reference): ROUGE (+0.89), BLEU (+0.69), METEOR (+0.50), SARI (+1.71), BERTScore (+0.55), GPT-PPL (-2.06). APPLS analysis identifies SARI as sensitive to simplification, GPT-PPL as promising for informativeness, LENS for coherence, and QAEval for faithfulness, but no single metric captures all four criteria.

**Validation**: Human validation of (i) extractive -> round-trip translated candidate summaries and (ii) GPT-simplified summaries: 100 pairs sampled per task, two expert annotators rated content alignment and the four PLS criteria on 5-point Likert scales. Agreement: Cohen's kappa = 0.48; Spearman rank correlation = 0.58. Two random seeds were used for perturbation generation to mitigate randomness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**

**Potential Harm**: Detecting hallucinations and factual inconsistencies (hallucinations) in plain language summaries that could misinform health-related decision-making.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Human annotation activity reported as exempt from institutional IRB review.
