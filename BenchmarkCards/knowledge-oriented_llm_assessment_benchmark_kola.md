# Knowledge-oriented LLM Assessment benchmark (KoLA)

## 📊 Benchmark Details

**Name**: Knowledge-oriented LLM Assessment benchmark (KoLA)

**Overview**: We construct a Knowledge-oriented LLM Assessment benchmark (KoLA), in which we carefully design three crucial factors: (1) For ability modeling, we mimic human cognition to form a four-level taxonomy of knowledge-related abilities, covering 19tasks. (2) For data, to ensure fair comparisons, we use both Wikipedia, a corpus prevalently pre-trained by LLMs, along with continuously collected emerging corpora, aiming to evaluate the capacity to handle unseen data and evolving knowledge. (3) For evaluation criteria, we adopt a contrastive system, including overall standard scores for better numerical comparability across tasks and models and a unique self-contrast metric for automatically evaluating knowledge-creating ability.

**Data Type**: text (knowledge triplets, question-answering pairs, document-level texts, event annotations, narrative generation)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- Big-Bench-Hard

**Resources**:
- [Resource](https://arxiv.org/abs/2306.09296)
- [Resource](https://www.wikipedia.org)
- [GitHub Repository](https://github.com/ranahaani/GNews)
- [Resource](https://archiveofourown.org)
- [Resource](https://open-platform.theguardian.com)
- [Resource](https://www.theguardian.com/open-platform/terms-and-conditions)
- [GitHub Repository](https://github.com/THU-KEG/OmniEvent)
- [Resource](https://huggingface.co/unitary/toxic-bert)
- [Resource](https://huggingface.co/dslim/bert-base-NER)
- [GitHub Repository](https://github.com/togethercomputer/RedPajama-Data)

## 🎯 Purpose and Intended Users

**Goal**: Carefully benchmarking the world knowledge of LLMs by (i) modeling abilities with a four-level cognitive taxonomy, (ii) using both known (Wikipedia) and continuously collected evolving data, and (iii) adopting a contrastive evaluation system including standardized scores and a self-contrast metric for knowledge creation.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners
- Domain Experts

**Tasks**:
- Knowledge Probing (Knowledge Memorization / fact probing)
- Named Entity Recognition
- Relation Extraction
- Event Detection
- Event Relation Extraction
- Question Answering (including Multi-hop Question Answering)
- Knowledge Base Question Answering
- Document-level Relation Extraction
- Text Generation (Knowledge Creating)
- Concept Probing

**Limitations**: KoLA evaluates LLMs’ world knowledge about concepts, entities, and events and only covers 19 English datasets now. Our automatic evaluation still relies on contrasting model-generated content with human-provided knowledge; if a model produces knowledge that is novel and reasonable but just not aligned with human-provided knowledge, its capabilities might be underestimated.

**Out of Scope Uses**:
- The intended use of KoLA is not to construct applications or train LLMs

## 💾 Data

**Source**: Known: Wikipedia and Wikidata5M (using a 2019 Wikipedia dump / Wikidata5M subset). Evolving: continuously crawled web content published in the recent ~90 days, including factual news (e.g., via GNews / The Guardian open platform) and fictional novels (Archive of Our Own). Test sets are constructed from these two sources; each Season crawls a minimum of 500 articles.

**Size**: Known: Wikipedia contains over 6.6 million English articles; Xlore alignment produced a dataset of 5 million articles. Evolving: each Season crawls at least 500 articles (first season collected 1,000 articles and retained 500 candidates; annotated 500 articles). Annotation output: 2.7K correct triples annotated for evolving data, of which 459 triples cannot be found in earlier corpora.

**Format**: N/A

**Annotation**: Crowdsourced annotation with a 21-member annotation team for dataset construction; each triple annotated by two annotators; event argument annotation with multi-round quality checks and validators (three Ph.D. holders). Reported inter-annotator agreement: Cohen's Kappa of 0.71 for triple correctness (a vs b+c) and 0.55 for whether triples pre-existed; Fleiss' Kappa of 0.62 for event argument annotation. Annotation team demographics are reported and quality control steps described.

## 🔬 Methodology

**Methods**:
- Automated metrics (EM, F1, Accuracy, BLEU, ROUGE-L)
- Standardized scoring (z-score then Min-Max scaling across tasks)
- Self-contrast evaluation for generation (automated)
- Human evaluation (manual annotation) used to validate knowledge-creating metrics

**Metrics**:
- Exact Match (EM)
- F1 Score (token-level / relaxed F1)
- Accuracy
- BLEU Score
- ROUGE-L (F1)
- Standardized score (z-score followed by Min-Max scaling to [0,100])
- Self-contrast metric (based on ROUGE-L similarities between T, Tk, and R)

**Calculation**: Standardized score: for a task, compute x_ij (chosen metric), then z_ij = (x_ij - mean_i)/std_i, then apply Min-Max scaling across all z to obtain scores in [0,100]. Self-contrast metric for Knowledge Creating: x = avg(∂(T,R), ∂(T,Tk), ∂(Tk,R)), where ∂(·) is ROUGE-L (F1).

**Interpretation**: Standardized scores enable comparability across tasks and models by reporting relative performance; the self-contrast metric focuses on faithfulness of created knowledge and correlates with human-judged faithfulness (Spearman coefficient 0.61). Removal of the self-contrast component from the overall KC metric decreases correlation with human-judged overall quality by 32%.

**Baseline Results**: KoLA evaluated 28 open-source and commercial LLMs across two seasons. Reported overall standardized rankings place GPT-4 and GPT-3.5-turbo at the top in Season 2. Detailed standardized scores and absolute metrics for each model and task are provided in the paper's Tables (Season 1 and Season 2 results).

**Validation**: Manual annotation of Knowledge Creating outputs (human raters rated overall quality and faithfulness on a 1-5 scale). Spearman correlation between the self-contrast metric ∂(T,Tk) and human-judged faithfulness is 0.61; removing the self-contrast metric from the overall KC metric reduces correlation with human-judged overall quality by 32%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Robustness
- Misuse
- Transparency
- Intellectual Property
- Data Laws
- Societal Impact

**Atlas Risks**:
- **Transparency**: Lack of training data transparency, Uncertain data provenance
- **Data Laws**: Data usage restrictions
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Intellectual Property**: Copyright infringement, Data usage rights restrictions
- **Robustness**: Hallucination
- **Misuse**: Improper usage
- **Societal Impact**: Impact on the environment
- **Accuracy**: Data contamination

**Demographic Analysis**: Annotation team demographics reported: Dataset construction annotation team (21 members): Female 85.7%, Male 14.3%; Education: Bachelor 47.6%, Master 52.4%. Creating-evaluation annotators (14 members): Female 71.4%, Male 28.6%; Education: Bachelor 57.1%, Master 42.9%.

**Potential Harm**: ['Knowledge hallucination (the benchmark aims to detect and evaluate knowledge hallucination via the self-contrast metric)', 'Bias and fairness issues (benchmark notes potential for bias and fairness concerns and reports checks)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Evolving data were filtered for inappropriate content; seven authors manually checked newly constructed evolving test datasets and random samples of previously released datasets and reported no instances of personally identifiable information, discriminatory content, explicit violence, or offensive content.

**Data Licensing**: Known data source: Wikipedia (licensed under CC BY-SA 3.0). Evolving data: public news (The Guardian, accessed following The Guardian terms and conditions) and fiction from Archive of Our Own (AO3); AO3 copyright status noted as ambiguous, KoLA remains non-commercial and does not redistribute crawled data (only samples provided).

**Consent Procedures**: Crowdsourced annotators were hired for annotation and human evaluation; work contracts were signed with all annotators, compensation was provided according to mutually agreed wage standards and working hours, and employment arrangements comply with local regulations.

**Compliance With Regulations**: All employment arrangements are in compliance with local regulations. Access to The Guardian data follows The Guardian's terms and conditions; KoLA asserts non-commercial, research-only use and cites fair use considerations for AO3 material per Organization for Transformative Works guidance.
