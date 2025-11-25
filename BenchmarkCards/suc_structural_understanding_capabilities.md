# SUC (structural understanding capabilities)

## 📊 Benchmark Details

**Name**: SUC (structural understanding capabilities)

**Overview**: We propose the SUC benchmark to evaluate the structural understanding capabilities of LLMs through seven distinct tasks (e.g., cell lookup, row retrieval and size detection) and to compare various input designs for table serialization and prompting.

**Data Type**: text (structured tables) and question-answering pairs

**Domains**:
- Natural Language Processing
- Information Retrieval

**Languages**:
- English

**Similar Benchmarks**:
- TabFact
- FEVEROUS
- SQA
- HybridQA
- ToTTo

**Resources**:
- [Resource](https://anonymous.4open.science/r/StructuredLLM-76F3/README.md)
- [GitHub Repository](https://github.com/microsoft/TableProvider)

## 🎯 Purpose and Intended Users

**Goal**: To compare different input designs and investigate the structural understanding capabilities of large language models on table (structured) data, and to provide guidance and prompting methods (self-augmented prompting) to improve LLM performance on tabular reasoning tasks.

**Target Audience**:
- ML Researchers
- Researchers and developers working on table/structured data and LLMs
- Future research on tabular reasoning

**Tasks**:
- Table Partition
- Table Size Detection
- Merged Cell Detection
- Cell Lookup
- Reverse Lookup
- Column Retrieval
- Row Retrieval

**Limitations**: Method primarily designed for languages with limited morphology such as English; scalability to longer texts is left for future exploration.

## 💾 Data

**Source**: Structured portions extracted from public tabular/benchmarked datasets: TabFact, FEVEROUS, SQA, HybridQA and ToTTo. All tables are from Wikipedia. For merged cell detection, samples are taken from ToTTo.

**Size**: For each task setting, 1,500 tables randomly sampled for testing (guaranteed table distribution). Downstream dataset sizes noted: SQA: 6,066 question sequences; HybridQA: 62,682 questions; FEVEROUS: 87,026 claims; ToTTo: more than 100,000 examples.

**Format**: Various serialization/storage formats considered and used in evaluation: CSV, JSON, XML, Markdown, HTML, XLSX (benchmark compares these formats and uses serialized table representations).

**Annotation**: Reference answers (groundtruth) sourced from the original datasets; each parsed sample appended with a unique question. Questions manually filtered by model-based checks (GPT-3.5) to remove consistently trivial questions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- One-shot in-context evaluation
- Zero-shot evaluation
- Ablation studies (input design variants)

**Metrics**:
- Accuracy
- BLEU-1
- BLEU-2
- BLEU-3
- BLEU-4

**Calculation**: Accuracy computed as exact-match under constrained output formats (e.g., instructions to split answers with '|' ); nonconforming outputs parsed with regular expressions for ~10% of cases. BLEU metrics computed for table-to-text generation (ToTTo) as reported.

**Interpretation**: Higher Accuracy and BLEU indicate better structural understanding by LLMs. Example: HTML markup with format explanations, role prompts, and no order change achieves a 65.43% overall accuracy across seven tasks; self-augmented prompting yields improvements over 1-shot baselines on downstream tasks (e.g., TabFact, HybridQA, SQA, FEVEROUS, ToTTo).

**Baseline Results**: Key reported baselines: 1-shot on downstream tasks — TabFact: 72.04% Accuracy; HybridQA: 46.07% Accuracy; SQA: 73.81% Accuracy; FEVEROUS: 75.56% Accuracy; ToTTo BLEU-4: 17.24%. HTML with format explanation/role prompts/no order change achieved 65.43% overall accuracy on seven SUC tasks. See tables in paper for full micro-results.

**Validation**: Evaluation performed with GPT-3.5 (text-davinci-003) and GPT-4 (GPT-4 evaluated on random subset of 300 samples per task). Output format constraints enforced; ~10% nonconforming outputs parsed via regular expressions. Questions that models consistently answered correctly during generation at nonzero temperature were manually eliminated.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
