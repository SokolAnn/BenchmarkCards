# XSEMPLR (Cross-Lingual Semantic Parsing in Multiple Natural Languages and Meaning Representations)

## 📊 Benchmark Details

**Name**: XSEMPLR (Cross-Lingual Semantic Parsing in Multiple Natural Languages and Meaning Representations)

**Overview**: XSEMPLR is a unified benchmark for cross-lingual semantic parsing that consolidates 9 existing datasets to cover 5 tasks, 22 natural languages, and 8 meaning representations. It is designed to evaluate models that translate queries in multiple natural languages into meaning representations (e.g., SQL, Lambda Calculus, Prolog, SPARQL, Python, ThingTalk, hierarchical intent and slot).

**Data Type**: text: natural language queries paired with meaning representations (MRs) (e.g., SQL, Lambda Calculus, Prolog, SPARQL, Python, ThingTalk, Hierarchical intent and slot)

**Domains**:
- Natural Language Processing
- Databases
- Knowledge Graphs
- Web Question Answering
- Task-Oriented Dialogue
- Code Generation

**Languages**:
- Arabic
- Chinese
- English
- Farsi
- Finnish
- French
- German
- Greek
- Hebrew
- Hindi
- Indonesian
- Italian
- Japanese
- Kannada
- Polish
- Portuguese
- Russian
- Spanish
- Swedish
- Thai
- Turkish
- Vietnamese

**Similar Benchmarks**:
- XNLI
- XTREME
- XGLUE
- MLQA
- XQuAD
- XOR QA
- CLIRMatrix
- NLCS

**Resources**:
- [GitHub Repository](https://github.com/psunlpgroup/XSemPLR)
- [Resource](https://arxiv.org/abs/2306.04085)
- [Resource](https://yale-lily.github.io/spider)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified, high-quality benchmark (XSEMPLR) for cross-lingual semantic parsing by assembling, cleaning, aligning, and unifying 9 existing datasets to evaluate multilingual models across diverse natural languages and meaning representations.

**Target Audience**:
- ML Researchers
- Model Developers
- Multilingual Natural Language Processing researchers

**Tasks**:
- Semantic Parsing
- Natural Language Interface to Databases (Text-to-SQL)
- Question Answering over Knowledge Graphs
- Question Answering on Web data
- Task-Oriented Dialogue Semantic Parsing (Intent and Slot)
- Code Generation (NL to Python)

**Limitations**: While XSEMPLR covers a wide range of tasks, datasets, natural languages, meaning representations, and domains, the authors state they cannot include all possible dimensions. They focus on linguistic generalization because the questions are translated from English datasets.

## 💾 Data

**Source**: Aggregated and unified from nine existing semantic parsing datasets: Multilingual ATIS (MATIS), Multilingual GeoQuery (MGeoQuery), Multilingual Spider (MSpider), Multilingual NLMaps (MNLmaps), Multilingual Overnight (MOvernight), MCWQ, MSchema2QA, MTOP, and MCoNaLa. The authors collect translations where available, clean and align multilingual question–MR pairs, and unify MR formats (e.g., SQL rewriting to Spider format).

**Size**: Per-dataset counts as reported in the paper/Table 1 and Appendix A: MATIS: 4,303 training, 481 dev, 444 test; MGeoQuery: 548 training, 49 dev, 277 test; MSpider: 8,095 training, 1,034 dev; MNLmaps: 1,500 training, 880 test; MOvernight: 8,754 training, 2,188 dev, 2,740 test; MCWQ: 4,006 training, 733 dev, 648 test; MSchema2QA: 8,932 training (5% subset used), 971 test; MTOP: 5,446 training, 863 dev, 1,245 test; MCoNaLa: 1,903 training (English), 476 dev, 896 test.

**Format**: N/A

**Annotation**: Varies by dataset: many examples and translations are human-annotated or human-translated; some training examples (e.g., parts of Schema2QA) are automatically generated or machine translated; some datasets use crowdsourced paraphrasing. The authors performed manual inspection to remove misaligned samples and unified MR formats.

## 🔬 Methodology

**Methods**:
- Automated metrics (exact matching / token-by-token string comparison)
- Dataset-specific evaluation tools (Spider evaluation tool)
- Execution Score
- Denotation Accuracy
- Code BLEU
- Experiment settings: Translate-Test, Monolingual, Monolingual Few-shot, Multilingual, Cross-lingual Zero-Shot Transfer, Cross-lingual Few-Shot Transfer

**Metrics**:
- Exact Match (token-by-token string comparison)
- Execution Score
- Denotation Accuracy
- Code BLEU
- Spider Exact Set Match (Exact Set Match without Values)

**Calculation**: For most datasets, evaluation uses exact token-by-token string matching between predicted MR and ground truth. For Spider, the Spider evaluation tool is used (Exact Set Match without Values). For fair comparison with prior work, the authors also applied execution-based metrics used by prior papers including Execution Score, Denotation Accuracy, and Code BLEU where appropriate.

**Interpretation**: Higher Exact Match / Execution Score / Denotation Accuracy / Code BLEU indicates stronger semantic parsing performance. The authors interpret large gaps between monolingual and cross-lingual zero-shot performance as indicating limited cross-lingual transfer, and improvements under few-shot or multilingual training as evidence these strategies can mitigate transfer gaps.

**Baseline Results**: Selected averaged results from Table 2: Monolingual mT5 average Exact Match = 58.16; Multilingual mT5 average = 61.82; Cross-lingual Zero-Shot mT5 average = 31.97; Cross-lingual Few-Shot mT5 average = 56.18. Monolingual XLM-R+PTR average = 52.03. Translate-Test mT5 average = 36.74. (See Table 2 for per-dataset and per-setting breakdowns.)

**Validation**: Followed original dataset train/dev/test splits where applicable; used dev sets for hyperparameter search. For MCWQ, used MCD (maximum compound divergence) split. Performed manual inspection to remove samples without aligned translations and unified MR formats across datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Transparency**: Uncertain data provenance

**Demographic Analysis**: The benchmark includes analysis across 22 natural languages with breakdowns between high-resource and low-resource languages; experiments report per-language performance and examine language-family effects and resource-related performance differences.

**Potential Harm**: Detects and exposes cross-lingual generalization failures and performance gaps (particularly for low-resource languages) in semantic parsing models; aims to identify limitations in model transferability across languages and meaning representations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
