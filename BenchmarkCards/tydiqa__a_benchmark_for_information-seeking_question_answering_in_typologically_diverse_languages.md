# TYDIQA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages

## 📊 Benchmark Details

**Name**: TYDIQA: A Benchmark for Information-Seeking Question Answering in Typologically Diverse Languages

**Overview**: TYDIQA is a question answering dataset covering 11 typologically diverse languages with 204K question-answer pairs. Questions are information-seeking (written by people who do not know the answer) and collected directly in each language without translation. The benchmark includes two primary tasks (Passage Selection and Minimal Answer Span), a data collection procedure that is model-free and translation-free, and a public leaderboard with a hidden test set.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Arabic
- Bengali
- Finnish
- Indonesian
- Japanese
- Kiswahili
- Korean
- Russian
- Telugu
- Thai

**Similar Benchmarks**:
- SQuAD
- MLQA
- XQuAD
- Natural Questions
- QuAC
- MS MARCO
- WikiQA
- CoQA
- XNLI

**Resources**:
- [GitHub Repository](https://github.com/google-research-datasets/tydiqa)
- [Resource](https://ai.google.com/research/tydiqa)

## 🎯 Purpose and Intended Users

**Goal**: 1) To enable research progress toward building high-quality question answering systems in roughly the world’s top 100 languages; 2) To encourage research on models that behave well across the linguistic phenomena and data scenarios of the world's languages.

**Target Audience**:
- ML Researchers
- Model Developers
- Computational Linguists

**Tasks**:
- Passage Selection
- Minimal Answer Span
- Gold Passage (simplified SQuAD-style compatibility task)

**Limitations**: Contains only 11 languages and therefore is not sufficient to cover the world's languages; per-language scores are not directly comparable due to differing amounts and quality of Wikipedia content and annotator pools.

## 💾 Data

**Source**: Wikipedia articles (atomic Wikipedia snapshot per language), articles retrieved by performing a Google search restricted to the Wikipedia domain for each language; tables, long lists, and infoboxes removed.

**Size**: 204,000 question-answer pairs (166,916 one-way annotated training examples; 37,421 dev+test examples in 3-way annotation). Total annotations: 277,000.

**Format**: N/A

**Annotation**: Training: one-way annotation. Dev and test: three-way annotation. Annotators select a passage (paragraph-like HTML element) as answer or indicate NULL, and, if applicable, select a minimal answer as byte-span (or YES/NO). Annotators underwent training requiring 90%+ to qualify; dev/test answers were verified by a separate pool of annotators.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation (bootstrapped held-out annotator estimate)

**Metrics**:
- F1 (harmonic mean of Precision and Recall)
- Precision
- Recall
- SQuAD v1.1 metrics (for TYDIQA-GOLDP)

**Calculation**: Primary measure is F1 calculated per example. Passage selection: credit if predicted passage index matches any annotator-selected passage. Minimal span: compute example-wise F1 between model span and annotator span with partial credit for overlap; YES/NO treated as exact match. NULL consensus: at least 2 of 3 annotators must select an answer for consensus to be non-NULL; systems receive credit for NULL only if consensus is NULL. Macro-averaging: average scores within each language, then average over non-English languages.

**Interpretation**: Higher F1 indicates better QA performance. Caution: scores are not comparable across languages because each language has unique questions, Wikipedia content quantity/quality, and annotator pools; English is included for debugging but excluded from macro-averaged results.

**Baseline Results**: Overall (macro-averaged non-English): Passage Selection - First-passage baseline F1 = 30.2; mBERT (jointly fine-tuned) Passage Answer F1 = 63.1; Lesser human estimate Passage Answer F1 = 79.9. Minimal Answer Span - mBERT F1 = 50.5; Lesser human estimate F1 = 70.1.

**Validation**: Quality control included: sampled fluency checks by native speakers; qualification task requiring 90%+ to qualify annotators; repeated qualification tasks to prevent drift; monitoring inter-annotator agreement; dev/test verified by separate annotator pool; expert judgments sampled (200 examples for Finnish and Russian) to assess correctness; use of 3 annotations per dev/test example and consensus rules.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Data contamination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
