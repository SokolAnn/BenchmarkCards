# WIKIHOP and MEDHOP

## 📊 Benchmark Details

**Name**: WIKIHOP and MEDHOP

**Overview**: Proposes a cross-document multi-hop reading comprehension task and a general dataset induction strategy; induces two datasets (WIKIHOP from WIKIPEDIA/WIKIDATA and MEDHOP from MEDLINE/DRUGBANK) to evaluate models that must seek and combine evidence across multiple documents to answer queries.

**Data Type**: question-answering pairs with supporting documents (multi-document text)

**Domains**:
- Natural Language Processing
- Molecular Biology

**Similar Benchmarks**:
- WIKIREADING
- SQuAD
- TriviaQA
- WikiQA
- SearchQA
- MS MARCO
- LAMBADA
- CNN/Daily Mail

**Resources**:
- [Resource](http://qangaroo.cs.ucl.ac.uk)
- [Resource](https://arxiv.org/abs/1710.06481v2)

## 🎯 Purpose and Intended Users

**Goal**: To encourage the development of models for text understanding across multiple documents and to investigate the limits of existing reading comprehension methods by requiring multi-hop (multi-step) inference across documents.

**Tasks**:
- Question Answering
- Reading Comprehension (Multi-hop / Cross-document)

**Limitations**: Datasets center around factoid questions about entities and, as extractive RC datasets, assume the answer is mentioned verbatim; distant supervision induces noise (the distant supervision assumption is violated for ~20% of samples); validated subsets were created because distantly supervised data can be noisy.

## 💾 Data

**Source**: WIKIHOP: WIKIPEDIA articles (first paragraphs) and WIKIDATA tuples; MEDHOP: MEDLINE abstracts with structured resources DRUGBANK, SWISS-PROT, and REACTOME used for graph traversal and distant supervision.

**Size**: WIKIHOP: 51,318 samples (43,738 train, 5,129 dev, 2,451 test). MEDHOP: 2,508 samples (1,620 train, 342 dev, 546 test).

**Format**: N/A

**Annotation**: Training labels induced via distant supervision from WIKIDATA (WIKIHOP) and DRUGBANK (MEDHOP). Human validation: WIKIHOP development and a validated test subset annotated via Amazon Mechanical Turk (3 annotators per sample, majority vote); MEDHOP: manual annotation of 20% of the test set by experts for validation of samples.

## 🔬 Methodology

**Methods**:
- Automated metrics (Accuracy / Exact Match)
- Human evaluation (crowdsourced annotation via Amazon Mechanical Turk; manual expert annotation for MEDHOP test subset)
- Model-based evaluation (baseline heuristics, retrieval baselines, and neural extractive RC models such as BiDAF and FastQA)

**Metrics**:
- Accuracy
- Exact Match
- Fleiss' kappa (inter-annotator agreement for human annotations)

**Calculation**: For extractive models accuracy measured as exact match between prediction and answer after lowercasing and removing articles, trailing whitespace and punctuation (same normalization as Rajpurkar et al., 2016). Inter-annotator agreement measured using Fleiss' kappa. Validated test sets consist of samples with majority crowd label 'follows' and requiring 'multiple' documents.

**Interpretation**: Higher Accuracy/Exact Match indicates better multi-hop cross-document reasoning. Authors report a substantial gap between model performance and human performance (e.g., best model accuracy 54.5% vs human 85.0% on an annotated test set), indicating room for improvement.

**Baseline Results**: Representative results reported: WIKIHOP total dataset sizes 51,318 samples. Baseline and model accuracies (examples): BiDAF reaches up to 54.5% accuracy on an annotated test set (paper reports best accuracy 54.5% vs human 85.0%). Document-cue and majority-candidate baselines achieve substantial accuracy before filtering (e.g., document-cue up to 74.6% on unfiltered WIKIHOP), motivating dataset filtering and masking. Full tables of baseline/model results are provided in the paper (e.g., Table 5, Table 6, Table 7).

**Validation**: Validated test sets were created: WIKIHOP validated subset annotated via crowdsourcing (3 annotators per sample, majority vote, Fleiss' kappa reported). For MEDHOP, 20% of the test set was manually annotated by experts to identify samples where the text implies the correct answer and multiple documents are required.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Transparency

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Transparency**: Uncertain data provenance

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
