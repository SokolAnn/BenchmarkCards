# ComFact: A Benchmark for Linking Contextual Commonsense Knowledge

## 📊 Benchmark Details

**Name**: ComFact: A Benchmark for Linking Contextual Commonsense Knowledge

**Overview**: We propose the new task of commonsense fact linking, where models are given contexts and trained to identify situationally-relevant commonsense knowledge from KGs. Our novel benchmark, ComFact, contains ≈293k in-context relevance annotations for commonsense triplets across four stylistically diverse dialogue and storytelling datasets.

**Data Type**: text (narrative contexts) and commonsense knowledge graph triples (head-relation-tail)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ATOMIC20 20
- ATOMIC
- ConceptNet
- PERSONA-CHAT
- MuTual
- ROCStories
- CMU Movie Summary Corpus

**Resources**:
- [GitHub Repository](https://github.com/Silin159/ComFact)
- [Resource](https://arxiv.org/abs/2210.12678)

## 🎯 Purpose and Intended Users

**Goal**: Define and benchmark the task of commonsense fact linking: identify situationally-relevant commonsense knowledge from knowledge graphs for narrative contexts, and provide a dataset (ComFact) to evaluate and advance models for this task (ComFact contains ≈293k contextually-linked commonsense facts).

**Target Audience**:
- ML Researchers
- Model Developers
- NLP Researchers

**Tasks**:
- Commonsense Fact Linking
- Knowledge Retrieval
- Entity Linking

**Limitations**: Dataset focuses on short context windows; uses English as the primary language; does not exhaustively cover all knowledge graphs, narrative corpora, and pretrained models; some evaluated models require considerable resources for inference.

## 💾 Data

**Source**: Commonsense knowledge graph: ATOMIC20 20 (used as the KG for linking). Narrative/context sources: PERSONA-CHAT, MuTual, ROCStories, and the CMU Movie Summary Corpus (samples drawn from these four English dialogue and storytelling datasets).

**Size**: ≈293,000 in-context relevance annotations (ComFact). ATOMIC20 20 contains 1.33M facts. Labeled fact candidates per ComFact split (from Table 11): PERSONA-ATOMIC: 67,196; MUTUAL-ATOMIC: 46,192; ROC-ATOMIC: 74,302; MOVIE-ATOMIC: 73,643.

**Format**: N/A

**Annotation**: Crowdsourced via Amazon Mechanical Turk with a multi-stage validation: head-entity validation (two workers per head; labels: relevant with full confidence, relevant with half confidence, irrelevant) and three-round fact candidate validation (present only; present+past; present+past+future) with two workers per evaluation round. Fact labels: always relevant, sometimes relevant, at odds, irrelevant. Link types derived: RPA (Relevant to Present Alone), RPP (Relevant to Present given the Past), RPF (Relevant to Present given the Future), IRR (Irrelevant). Worker qualification tests were used (head entity annotators required ≥95% on a qualification; fact candidate annotators required ≥90%).

## 🔬 Methodology

**Methods**:
- Automated evaluation using classification metrics
- Human evaluation (crowdworkers on sampled contexts)

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall
- Perplexity
- Distinct-1
- Distinct-2
- BLEU Score
- METEOR
- ROUGE-L
- CIDEr
- SkipThoughts

**Calculation**: Fact linking treated as binary classification: positive samples = fact candidates labeled always or sometimes relevant; negative samples = fact candidates labeled irrelevant; at odds excluded from classification evaluation. Recall is measured with respect to an initial heuristic over-sampled candidate set (≈41 facts per example context) rather than the entire KG; models encode the concatenation of context and fact candidate and output binary relevance predictions.

**Interpretation**: Higher Accuracy/F1/Precision/Recall indicate better ability to identify contextually-relevant commonsense facts. Supervised learned fact linkers substantially outperform heuristic baselines (paper reports an average absolute F1 improvement of ≈34.6% over heuristics) but still underperform humans. Improved fact linking produced average downstream relative improvements of 9.8% on a dialogue response generation task.

**Baseline Results**: Heuristic baselines (predicting all retrieved candidates as relevant) perform poorly; learned fact linking models provide an average ≈34.6% absolute F1 boost over heuristics. Improved retrieval yielded average downstream relative improvements of 9.8% for a dialogue response generation task. Models still significantly underperform human annotators.

**Validation**: Three-round crowdsourced validation on Amazon Mechanical Turk with worker qualification steps. Head entity qualification: workers must annotate ≥19/20 tested head entities (≥95%). Fact candidate qualification: workers must annotate ≥18/20 tested fact candidates (≥90%). Two workers independently annotate head entities; for fact candidates two workers annotate per round; ambiguous facts are re-evaluated in subsequent rounds; justifications requested in rounds 2 and 3 when a fact is marked relevant.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Explainability

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Explainability**: Unreliable source attribution, Unexplainable output

**Potential Harm**: ['Spurious reasoning / spurious explanations resulting from retrieval of irrelevant facts']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
