# Ontology Enrichment from Texts: A Biomedical Dataset for Concept Discovery and Placement

## 📊 Benchmark Details

**Name**: Ontology Enrichment from Texts: A Biomedical Dataset for Concept Discovery and Placement

**Overview**: We propose a new benchmark, adapting MedMentions dataset (PubMed abstracts) with SNOMED CT versions in 2014 and 2017 under the Diseases sub-category and the broader categories of Clinical finding, Procedure, and Pharmaceutical / biologic product. We provide usage on the evaluation with the dataset for out-of-KB mention discovery and concept placement, adapting recent Large Language Model based methods.

**Data Type**: text (contextual mention-level and mention-edge-pair-level from PubMed abstracts)

**Domains**:
- Healthcare
- Natural Language Processing

**Similar Benchmarks**:
- MedMentions
- NILK
- ShARe/CLEF 2013
- CLEF HIPE 2020
- EDIN
- NEEL 2015-2016
- ChEBI 500
- ChEBI+ 500
- MAG
- WordNet
- OSConcepts
- MeSH
- SemEval

**Resources**:
- [Resource](https://zenodo.org/record/8228005)
- [GitHub Repository](https://github.com/KRR-Oxford/OET)
- [GitHub Repository](https://github.com/KRR-Oxford/DeepOnto)
- [GitHub Repository](https://github.com/chanzuckerberg/MedMentions)
- [Resource](https://www.nlm.nih.gov/healthit/snomedct/archive.html)
- [GitHub Repository](https://github.com/IHTSDO/snomed-owl-toolkit)
- [Resource](http://protegeproject.github.io/protege/)
- [Resource](https://pubmed.ncbi.nlm.nih.gov/)

## 🎯 Purpose and Intended Users

**Goal**: Support two sequential tasks: (i) Out-of-KB Mention and Entity Discovery: identifying new mentions of concepts from texts which are not included in a KB; (ii) Concept Placement: given a new entity expressed as a mention in the text, placing it into a KB, either an ontology with complex concepts or a taxonomy with only atomic concepts.

**Tasks**:
- Out-of-KB Mention and Entity Discovery
- Concept Placement

**Limitations**: N/A

## 💾 Data

**Source**: MedMentions (PubMed abstracts) linked to UMLS (version 2017AA) and SNOMED CT subsets (SNOMED CT ver 20140901 and 20170301).

**Size**: MM-S14-Disease: 64,900 concepts (824 complex); 237,826 edges (4,997 complex). Mentions and mention-edge pairs: train: 11,812 mentions / 887,840 mention-edge pairs (917 mention-edge pairs with complex edges); valid: 4,248 mentions / 383,457 mention-edge pairs (203 with complex edges); test: 3,970 mentions / 316,319 mention-edge pairs (393 with complex edges); out-of-KB: 605 mentions / 1,637 mention-edge pairs (13 with complex edges). MM-S14-CPP: 175,895 concepts (2,718 complex); 625,994 edges (19,401 complex). Mentions and mention-edge pairs: train: 34,704 mentions / 1,398,111 mention-edge pairs (9,475 with complex edges); valid: 11,707 mentions / 548,295 mention-edge pairs (4,305 with complex edges); test: 11,564 mentions / 478,424 mention-edge pairs (4,129 with complex edges); out-of-KB: 1,000 mentions / 2,131 mention-edge pairs (22 with complex edges).

**Format**: JSON (mention-level and mention-edge-pair-level)

**Annotation**: Mentions in MedMentions were manually and exhaustively linked to UMLS; mapping to SNOMED CT entities via UMLS alignment; directed edges extracted from SNOMED CT (after transformation of equivalence axioms to subsumption and pruning) to provide gold-standard mention-to-edge mappings.

## 🔬 Methodology

**Methods**:
- Rule-based Sieve-based approach for out-of-KB detection
- BLINKout (bi-encoder candidate generation + cross-encoder selection; SapBERT used) for out-of-KB detection
- Edge bi-encoder (contextual mention to directed edge matching) for concept placement
- GPT-3.5-turbo zero-shot prompting to select among top-k edge candidates

**Metrics**:
- Overall Accuracy
- Out-of-KB Precision
- Out-of-KB Recall
- Out-of-KB F1 Score
- In-KB Precision
- In-KB Recall
- In-KB F1 Score
- Precision at k (P@k)
- Recall at k (R@k)
- F1 Score at k (F1@k)
- Mean Rank (MR)
- Mean Reciprocal Rank (MRR)

**Calculation**: Out-of-KB Mention Discovery: overall accuracy for all mentions; out-of-KB precision, recall, and F1 to measure detection of out-of-KB mentions; in-KB precision, recall, and F1 for in-KB mentions. Concept Placement: evaluate ranking of directed edges for a given mention using P@k, R@k, F1@k, MR, and MRR; reported P@k and R@k for different top-k values.

**Interpretation**: BLINKout (BERT-based) outperforms the Sieve-based rule method in overall accuracy and out-of-KB F1, but out-of-KB detection remains challenging (out-of-KB F1 between about 15% and 30%). Concept placement (edge prediction) is very challenging; GPT-3.5 zero-shot prompting to select from top-50 candidates does not improve or only marginally improves results.

**Baseline Results**: Out-of-KB Mention Discovery (MM-S14-Disease) — Sieve-based: A=55.9, P_o=6.4, R_o=47.0, F1_o=11.2, P_in=88.1, R_in=56.2, F1_in=68.6. BLINKout: A=67.2, P_o=14.6, R_o=17.4, F1_o=15.9, P_in=69.0, R_in=68.6, F1_in=68.8. (MM-S14-CPP) Sieve-based: A=49.7, P_o=3.3, R_o=59.3, F1_o=6.3, P_in=85.7, R_in=49.6, F1_in=62.8. BLINKout: A=65.9, P_o=22.5, R_o=32.6, F1_o=26.6, P_in=66.8, R_in=66.4, F1_in=66.6. Concept Placement (MM-S14-Disease) — Edge-Bi-encoder P/R@1=4.5/1.6, P/R@5=6.0/11.0, P/R@10=5.4/19.9, P/R@50=2.1/38.4; +GPT-3.5 P/R@1=4.3/1.6. (MM-S14-CPP) Edge-Bi-encoder P/R@1=2.2/1.0, P/R@5=2.2/5.2, P/R@10=2.0/9.4, P/R@50=1.4/32.4; +GPT-3.5 P/R@1=2.5/1.2.

**Validation**: For Out-of-KB Mention Discovery the dataset follows the original MedMentions training/validation/test splits. For Concept Placement the setting is unsupervised for out-of-KB mentions: training and validation use in-KB mentions and testing is performed on out-of-KB mentions (and in-KB mentions).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
