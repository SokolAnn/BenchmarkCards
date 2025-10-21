# Privacy Policy Language Understanding Evaluation (PLUE) benchmark

## 📊 Benchmark Details

**Name**: Privacy Policy Language Understanding Evaluation (PLUE) benchmark

**Overview**: PLUE is a multi-task benchmark for evaluating privacy policy language understanding across six tasks. The benchmark also includes a large corpus of privacy policies to enable privacy policy domain-specific language model pre-training.

**Data Type**: text (privacy policy documents: sentence-level multi-label classification, question-answering pairs, answer spans, intent and slot annotations, named-entity sequence labels)

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- OPP-115
- APP-350
- PrivacyQA
- PolicyQA
- PolicyIE
- PI-Extract
- Usable Privacy Policy Project
- MAPS

**Resources**:
- [GitHub Repository](https://github.com/JFChi/PLUE)
- [Resource](https://arxiv.org/abs/2212.10011v2)
- [GitHub Repository](https://github.com/citp/privacy-policy-historical)
- [Resource](https://mlco2.github.io/impact)
- [GitHub Repository](https://github.com/huggingface/transformers)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate privacy policy language understanding across six tasks and to provide a pre-training privacy policy corpus to enable domain-specific continual pre-training of language models.

**Target Audience**:
- Natural Language Processing Researchers
- Practitioners

**Tasks**:
- Text Classification
- Question Answering
- Semantic Parsing (Intent Classification and Slot Filling)
- Named Entity Recognition

**Limitations**: The pre-training privacy policy corpus and the downstream task datasets are unlikely to contain toxic or biased content; datasets are formed based on privacy policies crawled in the past and could be outdated; this work focuses on the English language only.

## 💾 Data

**Source**: Pre-training corpus: MAPS (mobile application privacy policy corpus from Zimmeck et al., 2019) and the Princeton-Leuven Longitudinal Corpus of Privacy Policies (Amos et al., 2021). Downstream datasets: OPP-115, APP-350, PrivacyQA, PolicyQA, PolicyIE, PI-Extract (datasets derived from or from prior works as cited).

**Size**: Pre-training corpus: 332M words (combined). Dataset statistics (from Table 1): OPP-115: 115 policies, 2,771 train, 395 dev, 625 test; APP-350: 350 policies, 10,150 train, 2,817 dev, 2,540 test; PrivacyQA: 35 policies, 1,350 train, 400 test; PolicyQA: 115 policies, 17,056 train, 3,809 dev, 4,152 test; PolicyIE: 31 policies, 4,209 train, 1,041 test; PI-Extract: 30 policies, 3,034 train, 1,028 test.

**Format**: Raw text (documents converted from HTML/PDF/Markdown to raw text format).

**Annotation**: Annotations come from the original datasets (OPP-115, APP-350, PrivacyQA, PolicyQA, PolicyIE, PI-Extract) and include sentence-level multi-label privacy practice annotations, relevance labels for QA, answer spans for reading-comprehension QA, intent labels and slot annotations for semantic parsing, and named-entity labels for PI-Extract.

## 🔬 Methodology

**Methods**:
- Domain-specific continual pre-training of pre-trained language models
- Task-specific fine-tuning of pre-trained language models
- Automated metrics evaluation (no human evaluation reported for model outputs in this work)
- Repeated fine-tuning runs with different random seeds (reporting averages)

**Metrics**:
- F1 Score
- Precision
- Recall
- Exact Match (EM)

**Calculation**: Metrics computed on held-out test sets; models fine-tuned three times with different random seeds and average performances reported. For OPP-115 and APP-350 class weights (inversely proportional to class occurrences) are computed and applied during fine-tuning. PrivacyQA reports Precision/Recall/F1; PolicyQA reports F1 and Exact Match.

**Interpretation**: Higher F1/Precision/Recall/EM indicates better performance. The paper interprets improvements from domain-specific continual pre-training as consistent performance gains across tasks; remaining low performance on some tasks indicates room for future work.

**Baseline Results**: Selected results (averaged over three seeds) include: PP-RoBERTa (base) — OPP-115 F1: 80.2; APP-350 F1: 69.5; PrivacyQA P/R/F1: 49.8/40.1/40.9; PolicyQA F1/EM: 57.8/30.3; PI-Extract F1 (collection/share): 71.2/61.3. Full model comparison tables are provided in the paper (Tables 2 and 3).

**Validation**: Fine-tuning uses validation examples when available and a grid search over learning rates. Models are fine-tuned for 3 epochs on QA tasks and 20 epochs on other tasks; three runs with different seeds are averaged. Class weights applied for imbalanced classification tasks (OPP-115, APP-350).

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Value Alignment
- Data Laws
- Societal Impact

**Atlas Risks**:
- **Fairness**: Data bias
- **Value Alignment**: Toxic output
- **Data Laws**: Data usage restrictions
- **Societal Impact**: Impact on the environment

**Demographic Analysis**: Focuses on English only; no demographic breakdown across population groups is provided.

**Potential Harm**: ['Privacy violations due to misunderstanding or failure to surface privacy practices in policies']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: OPP-115 and APP-350: available for research, teaching, and scholarship purposes under terms in the spirit of Creative Commons Attribution-NonCommercial (CC BY-NC). PolicyQA and PI-Extract are derived from OPP-115. PrivacyQA and PolicyIE released under an MIT license. The pre-training corpus (MAPS Policies Dataset) is released under CC BY-NC. PLUE benchmark resources to be released under CC BY-NC-SA 4.0.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
