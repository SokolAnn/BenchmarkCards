# SCALE

## 📊 Benchmark Details

**Name**: SCALE

**Overview**: A multilingual, domain-specific benchmark for the Swiss legal domain challenging LLMs on five dimensions: processing long documents (up to 50K tokens), domain-specific knowledge (legal texts), multilingual understanding (German, French, Italian, Romansh, English), multitasking (Information Retrieval, Court View Generation, Leading Decision Summarization, Citation Extraction, and eight Text Classification configurations) and reasoning. The benchmark comprises seven public datasets (SMILED) derived from 26 cantons and the Swiss Federal Supreme Court and includes pretraining corpora and pretrained legal models; all resources are published under permissive CC BY-SA licenses (links provided upon acceptance).

**Data Type**: text (court rulings and legislation; document-to-document IR queries; document-summary pairs; token-level citation labels; document-level classification labels; long-form generation pairs)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- German
- French
- Italian
- Romansh
- English

**Similar Benchmarks**:
- SCROLLS
- MuLD
- LexGLUE
- LEXTREME
- LegalBench
- LBOX OPEN
- XTREME
- GLUE
- SuperGLUE
- MMLU
- BIG-Bench
- BEIR

**Resources**:
- [Resource](https://entscheidsuche.ch/dataUsage)
- [Resource](https://www.fedlex.admin.ch/en/legal-information)
- [Resource](https://arxiv.org/abs/2306.09237v3)

## 🎯 Purpose and Intended Users

**Goal**: Provide seven new multilingual Swiss legal datasets (SMILED), two large in-domain pretraining corpora, and an end-to-end benchmark (SCALE) to evaluate and spur development of models capable of long-document processing, domain-specific legal knowledge, multilingual understanding, multitasking, and legal reasoning.

**Target Audience**:
- ML Researchers
- Model Developers
- Legal Domain Experts
- Judicial Practitioners (judges and court clerks)

**Tasks**:
- Information Retrieval
- Text Generation (Court View Generation)
- Summarization (Leading Decision Summarization)
- Token Classification (Citation Extraction)
- Text Classification (Criticality Prediction, Judgment Prediction, Law Area Prediction, Sub-Law-Area Prediction)
- Document-to-Document Retrieval
- Long-document processing

**Limitations**: Domain-specific to the Swiss legal system and not directly generalizable to other jurisdictions; several tasks use algorithmically generated labels (semi-automatic extraction using regex) rather than full expert annotations; resource constraints required truncation of inputs/outputs for generation tasks (e.g., CVG outputs truncated to 512 tokens) and limited evaluation subsets; some datasets and tasks simplified (e.g., CVG uses facts as proxy for complaints).

**Out of Scope Uses**:
- Deploying Judgment Prediction (JP) as an automated decision-making tool in practice (authors state JP is unlikely to be deployed in practice anytime soon).
- Generalizing Swiss-specific legal conclusions to other countries or legal systems (authors explicitly caution against generalization).

## 💾 Data

**Source**: Swiss court rulings and legislation collected from 26 cantons and the Swiss Federal Supreme Court (SFSC), derived from publicly available sources (Entscheidsuche.ch and Fedlex) and curated by the authors; datasets collectively referred to as SMILED (SwissMultilIngualLEgalData).

**Size**: SMILED comprises multiple datasets: Rulings: 638,000 cases; Leading Decisions: 21,000; Legislation: 35,700 texts; Doc2Doc IR: 141,000; Citation Extraction: 131,000; Criticality Prediction: 139,000; Law Area Prediction: 329,000; Judgment Prediction: 329,000; Court View Generation: 404,000; Court View Origin Generation: 270; Leading Decision Summarization: 18,000. Pretraining corpora: Legislation corpus: 116M words; Court rulings corpus: 2.1B words. Swiss Rulings dataset specifically: 638K cases (3.3B tokens) distributed across German (319K), French (247K), Italian (71K). Legislation dataset: 35.7K texts (182M tokens).

**Format**: N/A

**Annotation**: Semi-automatically with human verification: labels and fields were extracted mostly using regular expressions and metadata; source documents were manually anonymized (approx. 45 minutes per case) and multiple people performed repeated quality checks; parsers and regexes were double-checked by senior authors.

## 🔬 Methodology

**Methods**:
- Pretraining of domain-specific language models
- Fine-tuning of models per task
- Zero-shot and one-shot evaluation of closed LLMs
- Automated metrics for generation and retrieval evaluation
- Ablation studies
- Information retrieval evaluation with lexical (BM25) and neural (SBERT) methods
- Hierarchical evaluation setup for text classification (LEXTREME-style aggregation)

**Metrics**:
- BERTScore
- BLEU
- METEOR
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Macro F1 Score (macro-averaged F1 using harmonic mean aggregation)
- Normalized Discounted Cumulative Gain (NDCG)
- Capped Recall@k

**Calculation**: Text Classification: hierarchical aggregation of macro-averaged F1 scores using the harmonic mean, averaged over random seeds, languages (de, fr, it), configurations, and datasets (LAP, JP, CP) following the LEXTREME setup. Information Retrieval: Capped Recall@k is computed as the proportion of relevant documents for a specific query retrieved within the top-k results; NDCG is used for ranking quality. Text Generation: multiple automated metrics (BERTScore, BLEU, METEOR, ROUGE variants) are reported per standard formulations; inputs/outputs truncated as described for experimental feasibility.

**Interpretation**: Authors note that each individual generation metric has weaknesses and thus multiple metrics are necessary for comprehensive assessment. The harmonic mean aggregation punishes models with outlier low scores, promoting fairer models across languages and configurations. NDCG and Capped Recall@k are used to assess retrieval ranking quality and retrieval coverage respectively.

**Baseline Results**: Authors report that existing publicly available multilingual models struggle across many tasks; 'the best performing model only achieving an aggregated Macro F1 score of 48.4' (as stated in the paper). Detailed per-task baselines are reported in the paper (tables with model-specific scores).

**Validation**: Downstream datasets partitioned temporally: training (until 2015), validation (2016-2017), test (2018-2022). Data quality ensured via repeated human quality checks, manual anonymization, double-checked parsers/regexes, and automated pipeline tests. Experimental validation procedures include multiple random seeds, early stopping on validation loss, gradient accumulation for batch size adjustments, and limited validation subsets for cost reasons (e.g., validation limited to 1,000 samples for LLM zero-shot classification evaluations).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy
- Explainability
- Misuse
- Societal Impact

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Misuse**: Spreading disinformation
- **Explainability**: Unexplainable output
- **Societal Impact**: Impact on Jobs, Impact on affected communities
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: Language and cantonal distributions are reported (e.g., rulings: ~50% German, ~39% French, ~11% Italian; legislation: ~49% German, ~31% French, ~17% Italian). Coverage varies significantly across cantons and courts.

**Potential Harm**: ["Potential job displacement or impact on legal professionals' roles (authors explicitly note possible impact on the job market for legal professionals).", 'Misinformation or misleading legal content produced by models (authors highlight precision issues and potential severe implications in the legal domain).', 'Privacy risks mitigated by anonymization but still a consideration (authors note anonymization and discuss sensitivity of legal data).', 'Misrepresentation or cultural/contextual errors when applied outside the Swiss jurisdiction.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data are publicly available court decisions that were manually anonymized (approx. 45 minutes per case). The authors state the person should not be identifiable and describe repeated quality checks to ensure anonymization.

**Data Licensing**: Datasets, pre-trained models, and code are published under CC BY-SA licenses (authors state release under permissive CC BY-SA licenses).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
