# NarrativeXL: a Large-scale Dataset for Long-Term Memory Models

## 📊 Benchmark Details

**Name**: NarrativeXL: a Large-scale Dataset for Long-Term Memory Models

**Overview**: We propose a new large-scale (nearly a million questions) ultra-long-context (more than 50,000 words average document length) reading comprehension dataset. Using GPT-3.5, we summarized each scene in 1,500 hand-curated fiction books from Project Gutenberg, which resulted in approximately 150 scene-level summaries per book. After that, we created a number of reading comprehension questions based on these summaries, including three types of multiple-choice scene recognition questions, as well as free-form narrative reconstruction questions. Most questions have a known “retention demand”, indicating how long-term of a memory is needed to answer them, which should aid long-term memory performance evaluation.

**Data Type**: text (question-answering pairs: multiple-choice read-along questions; free-form summary reconstruction and hierarchical summary reconstruction)

**Domains**:
- Natural Language Processing

**Similar Benchmarks**:
- NarrativeQA
- SCROLLS
- Zero-SCROLLS
- BookSum
- QuALITY
- QMSum
- ASJ
- PG19
- Long Range Arena

**Resources**:
- [GitHub Repository](https://github.com/r-seny/NarrativeXL)
- [Resource](https://arxiv.org/abs/2305.13877)

## 🎯 Purpose and Intended Users

**Goal**: Create a large-scale ultra-long-context reading comprehension dataset to train and evaluate long-term memory models and to provide diagnostic tasks with explicit memory retention demand.

**Target Audience**:
- Academic and industry organizations
- Model developers
- Machine learning researchers

**Tasks**:
- Reading Comprehension
- Question Answering
- Summarization (scene-level and hierarchical)

**Limitations**: It is likely that many questions can be answered using relatively simple Information Retrieval approaches (IR). Data contamination (books appearing in model pretraining) is impossible to fully control; authors take mitigation steps (remove titles/authors, named-entity substitution) but do not claim to fully resolve the issue. The authors also note they do not directly show that the dataset will improve ultra-long-context LLMs, focusing instead on validating the data.

## 💾 Data

**Source**: Full-text books downloaded from Project Gutenberg (1,500 hand-curated fiction books); scene summaries and distorted summaries generated with GPT-3.5; named-entity substitution applied using spaCy; manual filtering of books performed.

**Size**: 990,595 total questions across 1,500 books. Breakdown: 726,803 multiple-choice read-along questions; 244,111 non-hierarchical scene summary reconstruction (freeform); 19,681 hierarchical summary reconstruction (freeform). Average context/document lengths: read-along questions avg context ~54,334 words; summary reconstruction avg context ~87,051 words.

**Format**: N/A

**Annotation**: Scene summaries, hierarchical summaries, and distorted summaries generated with GPT-3.5. Manual book filtering/cleaning performed. Named-entity substitution dictionaries created and applied (spaCy used for named entity identification). Small-scale human validation performed via Amazon Mechanical Turk.

## 🔬 Methodology

**Methods**:
- Automatic summarization and false-summary generation using GPT-3.5
- Manual filtering and cleaning of Project Gutenberg books
- Named entity substitution using spaCy
- Human validation study (Amazon Mechanical Turk)
- Model-based evaluation: zero-shot evaluation with GPT-4 and Anthropic Claude; fine-tuning experiments (GPT-3 Curie, Longformer Encoder-Decoder)
- Automated metric evaluation (ROUGE, BertSCORE) and accuracy measurements

**Metrics**:
- Accuracy
- ROUGE-1 F1
- ROUGE-2 F1
- ROUGE-L F1
- BertSCORE F1

**Calculation**: Multiple-choice performance measured by Accuracy. Summary reconstruction quality measured by ROUGE-1 F1, ROUGE-2 F1, ROUGE-L F1 (ROUGE scores calculated using https://pypi.org/project/rouge-score/) and BertSCORE F1 by comparing reconstructed summaries to true summaries.

**Interpretation**: Higher Accuracy on read-along questions indicates better long-term memory/retention for the required retention demand. Summary reconstruction metric improvements (ROUGE/BertSCORE) indicate better ability to reconstruct true summaries given context. The dataset provides explicit 'retention demand' measures enabling measurement of forgetting curves and diagnosis of memory capacity.

**Baseline Results**: Read-along zero-shot: GPT-4 accuracy 0.783, Anthropic (Claude) accuracy 0.53 (on 60-question subset). BERT fine-tuned to distinguish distorted vs true summaries (no context) achieved accuracy 0.524 on subset. Summary reconstruction (Table 5): Baseline (corrupted vs true) ROUGE-1 F1 .522, ROUGE-2 F1 .261, ROUGE-L F1 .408, BertSCORE F1 .906. LED (fine-tuned) ROUGE-1 F1 .53, ROUGE-2 F1 .26, ROUGE-L F1 .40, BertSCORE .90. GPT-3 (fine-tuned) ROUGE-1 F1 .504, ROUGE-2 F1 .236, ROUGE-L F1 .384, BertSCORE .900. GPT-4 no context ROUGE-1 F1 .512; GPT-4 with context ROUGE-1 F1 .576 (other metrics improved similarly).

**Validation**: Human validation: 25 MTurk workers (US-based, master qualification) labeled 250 scenes (10 scenes each) and achieved 0.95 accuracy identifying true vs false summaries. Model validation: zero-shot evaluation with GPT-4 and Anthropic on subsets; fine-tuning experiments with GPT-3 Curie and LED; statistical tests (paired t-tests, Spearman correlation, chi-square) used to evaluate effects of context length on performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
