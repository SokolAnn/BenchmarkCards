# NNE: A Dataset for Nested Named Entity Recognition in English

## 📊 Benchmark Details

**Name**: NNE: A Dataset for Nested Named Entity Recognition in English

**Overview**: We describe NNE—a fine-grained, nested named entity dataset over the full Wall Street Journal portion of the Penn Treebank (PTB). Our annotation comprises 279,795 mentions of 114 entity types with up to 6 layers of nesting. We publicly release the standoff annotations along with detailed annotation guidelines and scripts for knitting annotations onto the underlying PTB corpus. We hope the public release of this large dataset for English newswire will encourage development of new techniques for nested NER.

**Data Type**: text (standoff annotations of nested named entity mentions over Wall Street Journal portion of the Penn Treebank)

**Domains**:
- Natural Language Processing
- Newswire

**Languages**:
- English

**Similar Benchmarks**:
- ACE2005
- GENIA
- BBN

**Resources**:
- [Resource](https://arxiv.org/abs/1906.01359)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a large-scale, manually-annotated, fine-grained nested named entity dataset over the Wall Street Journal portion of the Penn Treebank to facilitate research and development of nested NER techniques.

**Target Audience**:
- Researchers in Natural Language Processing
- Model developers working on Named Entity Recognition

**Tasks**:
- Named Entity Recognition
- Nested Named Entity Recognition

**Limitations**: Complexity and run time are open challenges (decoding speed is slow for some models due to large number of entity categories). Dataset is limited to the Wall Street Journal portion of the Penn Treebank (English newswire).

## 💾 Data

**Source**: Standoff annotations over the full Wall Street Journal portion of the Penn Treebank (PTB).

**Size**: 279,795 mentions; 1.1M tokens; 2,312 documents; 49,208 sentences.

**Format**: Standoff annotations (scripts provided to knit annotations onto the PTB); exact file format not specified in text.

**Annotation**: Manual annotation by four annotators with detailed annotation guidelines and use of a custom annotation tool; sections 00 and 23 doubly annotated; section 02 annotated by all four annotators; adjudication performed (additional 17 hours); total annotation time 270 hours.

## 🔬 Methodology

**Methods**:
- Automated evaluation using CoNLL exact-match evaluation
- Model-based evaluation: evaluated existing NER models (BiLSTM-CRF flat models, hypergraph-based model, transition-based model)

**Metrics**:
- Precision
- Recall
- F1 Score
- Fleiss' kappa (inter-annotator agreement)

**Calculation**: Follow CoNLL evaluation schema requiring an exact match of mention start, end and entity type (Sang and Meulder, 2003). The model that performs best on the development set is evaluated on the test set for final results.

**Interpretation**: Flat NER models achieve high precision but suffer from low recall when applied to nested structures. Hypergraph-based model attains the best F1 on this dataset but has slow decoding speed (9 words/second). Transition-based method has higher decode speed (57 words/second) but lower precision than flat models.

**Baseline Results**: BiLSTM-CRF-TOP: Precision 89.9, Recall 38.0, F1 53.5; BiLSTM-CRF-BOTTOM: Precision 93.8, Recall 62.0, F1 74.7; BiLSTM-CRF-BOTH: Precision 92.2, Recall 85.8, F1 88.9; Hypergraph: Precision 91.8, Recall 91.0, F1 91.4; Transition: Precision 77.4, Recall 70.1, F1 73.6.

**Validation**: Inter-annotator agreement measured on Section 02 (annotated by all four annotators). Fleiss' kappa over all tokens: 0.907; Fleiss' kappa for tokens part of at least one mention: 0.832. Average precision, recall and F1 across four annotators w.r.t. adjudicated gold: 94.3, 91.8, 93.0.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
