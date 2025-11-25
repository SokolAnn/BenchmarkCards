# NEO-BENCH

## 📊 Benchmark Details

**Name**: NEO-BENCH

**Overview**: We present NEO-BENCH, a new benchmark designed to test the ability of LLMs to understand and process neologisms. NEO-BENCH consists of 2,505 neologisms (both words and phrases) emerging around 2020–2023 and 4 intrinsic/extrinsic tasks (Perplexity, Cloze Question Answering, Definition Generation, and Machine Translation) to evaluate LLMs' abilities to generalize on neologisms.

**Data Type**: text (neologism-containing sentences; question-answering pairs; definition prompts; cloze passages)

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- NYTWIT
- WMT23 Quality Estimation

**Resources**:
- [GitHub Repository](https://github.com/JonathanQZheng/NEO-BENCH)
- [Resource](https://trends.google.com/trends/)
- [Resource](https://translate.google.com/)
- [Resource](https://www.bing.com/translator)
- [Resource](https://www.deepl.com/translator)
- [GitHub Repository](https://github.com/tatsu-lab/stanford_alpaca)

## 🎯 Purpose and Intended Users

**Goal**: Test the ability of Large Language Models to generalize to and process neologisms across perplexity and downstream tasks (Cloze Question Answering, Definition Generation, and Machine Translation).

**Tasks**:
- Perplexity
- Cloze Question Answering
- Definition Generation
- Machine Translation

**Limitations**: Most of our neologisms largely originated in US and UK English, as we collect textual data from news articles from this region. NEO-BENCH is static as we collect neologisms from mostly 2020-2023, which will become outdated over time as newer models will be exposed to new language in context. Multilingual neologism collection and temporal drift analysis are left for future work.

## 💾 Data

**Source**: Collected 2,505 neologisms using multiple methods: filtered Reddit monthly dumps, Google News headlines (news articles), NYT First Said Twitter bot tweets, prior slang dictionary dataset samples (Zhu and Jurgens, 2021), and handpicked examples; data cover neologisms emerging around 2019–2023. For MT references and annotations, in-house native Chinese speakers and in-house native English speakers were used.

**Size**: 2,505 neologisms; Machine Translation: 240 sentences containing neologisms; Perplexity: 422 Cloze passages; Cloze Question Answering: 750 passages (multiple-choice); Definition Generation: 750 "What is [neologism]?" questions.

**Format**: N/A

**Annotation**: Manual annotation by in-house native English speakers and in-house native Chinese speakers for dataset construction and reference translations; crowdsourced human evaluation for MT (five fluent Mandarin annotators on Prolific); GPT-4 used for automatic evaluation of definition generation (with manual verification on samples).

## 🔬 Methodology

**Methods**:
- Human evaluation (crowdsourced and in-house native speakers)
- Automated metrics (BLEU, COMET, COMETKiwi, MetricX-23, MetricX-23-QE)
- Perplexity rank classification (mask filling and sequence perplexity ranking against neologism, distractor, and top 5000 Reddit words)
- 5-shot prompting for Cloze QA and Definition Generation
- GPT-4 automatic semantic equivalence evaluation for definitions

**Metrics**:
- BLEU
- COMET
- COMETKiwi
- MetricX-23
- MetricX-23-QE
- Accuracy
- Perplexity
- Spearman's rank correlation (Spearman’s ρ)

**Calculation**: For Perplexity rankings: for each passage, fill mask with the neologism, the distractor, and the top 5000 singular Reddit words, compute sequence perplexities, sort by sequence perplexity, and report average rankings. For Machine Translation: compute BLEU, COMET, and MetricX-23 against human reference translations; use COMETKiwi and MetricX-23-QE as reference-free metrics. Cloze QA and Definition Generation are evaluated by Accuracy; GPT-4 and human annotators are used to determine semantic equivalence for definitions. Correlations between automatic metrics and human judgments are computed with Spearman's ρ.

**Interpretation**: Lower neologism rankings represent lower relative perplexities and indicate the model is more likely to complete the passage with a neologism. Lower MetricX scores indicate higher performance. Spearman's ρ between metrics and human judgments is used to assess metric reliability (e.g., COMETKiwi correlation with human judgment reported as 0.491 in this study). Models with later knowledge cutoff dates generally yield lower perplexities and better downstream task performance.

**Baseline Results**: Machine Translation metrics (Table 5): BLEU best: Google Translate 0.507; COMET best: GPT-4 0.854; COMETKiwi best: DeepL 0.807; MetricX-23 best (lower is better): GPT-4 1.550; MetricX-23-QE best (lower is better): DeepL 1.260. Older LLMs (BART, T5, GPT-J, Flan-T5) have much lower performance, with average accuracies of 32.20% (Cloze QA) and 12.27% (Definition Generation) as reported.

**Validation**: Validated with human evaluation: dataset construction and references by in-house native speakers; MT human annotations via crowdsourced fluent Mandarin annotators on Prolific; inter-annotator agreement and automated evaluator agreement reported (e.g., Cohen's Kappa between GPT-4 and human evaluation for definition generation sample = 0.744). The Google Trends filtering method was sampled and manually annotated to estimate precision and recall for neologism candidate filtering.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: Most neologisms largely originated in US and UK English; Reddit data were not location-restricted but the majority of English-speaking Reddit users are from the same regions, limiting dialectal and regional coverage.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: They remove personally identifiable information by using a SpaCy named-entity recognition model to identify named entities and largely remove them; all candidates are manually inspected to ensure no PII is included; hand-crafted sentences are reviewed to avoid PII.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
