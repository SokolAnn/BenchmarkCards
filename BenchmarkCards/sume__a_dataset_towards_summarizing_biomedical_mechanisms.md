# SuMe: A Dataset Towards Summarizing Biomedical Mechanisms

## 📊 Benchmark Details

**Name**: SuMe: A Dataset Towards Summarizing Biomedical Mechanisms

**Overview**: We introduce a biomedical mechanism summarization task and SuMe, a large-scale dataset constructed from PubMed abstracts where each instance consists of a pair of biochemical entities (regulator and regulated), supporting sentences from the abstract, the relation between the entities (positive/negative activation or regulation), and a sentence that summarizes the mechanism underlying the relation. We create 22K mechanism summarization instances via a semi-automatic bootstrapping process and a 611K-instance conclusion sentence generation pretraining set, and benchmark several general and domain-adapted language models using automatic and manual evaluation.

**Data Type**: text (supporting sentences and conclusion/mechanism sentences from biomedical abstracts)

**Domains**:
- Natural Language Processing
- Biomedical Research

**Similar Benchmarks**:
- ChemProt
- ScisummNet
- TLDR
- TalkSumm
- FacetSum

**Resources**:
- [Resource](https://arxiv.org/abs/2205.04652)
- [Resource](https://pubmed.ncbi.nlm.nih.gov)

## 🎯 Purpose and Intended Users

**Goal**: To create a biomedical mechanism summarization task and dataset (SuMe) that pairs supporting sentences and entity pairs with a conclusion mechanism sentence, and to benchmark language generation models on generating relations and mechanism summaries.

**Target Audience**:
- ML Researchers
- Domain Experts (Biomedical researchers)
- Model Developers

**Tasks**:
- Text Summarization
- Relation Extraction
- Text Generation
- Explanation Generation

**Limitations**: SuMe is constructed via a semi-automatic bootstrapping process and contains noise: experts found that 16% of the data has some error (relation extraction or non-mechanism output) and 15% of instances require background knowledge. The curated clean evaluation partition is small (125 instances).

## 💾 Data

**Source**: PubMed open access subset; relation and entity extraction performed using REACH (Valenzuela-Escárcega et al., 2018); mechanism seed sentences and labels derived from ChemProt sentences annotated by experts and from a small manually labeled mechanism sentence set collected from domain experts.

**Size**: 22,765 mechanism summarization instances (Train: 20,765 instances; Dev: 1,000 instances; Test: 1,000 instances); Pretraining conclusion-generation set: 611,000 instances; Source corpus: ~1.1M abstracts

**Format**: N/A

**Annotation**: Semi-automated bootstrapping: 21 experts annotated ChemProt sentences on a 4-point Likert scale (3 annotators per sentence, majority vote) yielding 439 Mechanism and 447 Non-Mechanism sentences; trained mechanism-sentence classifiers (BioBERT, SciBERT, BiomedNLP, BioELECTRA) and used the classifier (BioELECTRA best, 74% macro F1) to label conclusion sentences and create 22K mechanism instances. A clean evaluation partition of 125 instances was manually checked by five domain experts.

## 🔬 Methodology

**Methods**:
- Automated evaluation with lexical and learned metrics
- Manual evaluation by biomedical experts
- Pretraining on conclusion generation as auxiliary task
- Fine-tuning of pretrained transformer models

**Metrics**:
- F1 Score (for relation generation)
- BLEURT (BLEURT-20)
- ROUGE-1
- ROUGE-2
- ROUGE-L
- Macro F1 (for mechanism sentence classifier)

**Calculation**: Relation generation: generated relation deemed correct if it exactly matches the reference relation name; report F1 for binary relation classification. Mechanism generation: compare generated mechanism sentence (hypothesis) to gold reference using BLEURT-20 and ROUGE (ROUGE-1, ROUGE-2, ROUGE-L). Model selection on validation uses the average of BLEURT and ROUGE-L.

**Interpretation**: Higher F1 indicates more accurate relation generation; higher BLEURT and ROUGE indicate greater similarity between generated and reference mechanism sentences. Manual evaluation criteria: whether generated sentence contains a mechanism explaining the relation, whether information is supported by supporting sentences, and whether the mechanism is factually correct. Despite automatic scores, only 32% of model outputs were acceptable on all manual criteria for the best model.

**Baseline Results**: Table 3 results (automatic eval on mechanism generation + RG F1): BART — RG F1: 76, BLEURT: 42.49, ROUGE-1: 46.54, ROUGE-2: 25.92, ROUGE-L: 35.34. GPT2 — RG F1: 74, BLEURT: 44.19, ROUGE-1: 46.54, ROUGE-2: 28.32, ROUGE-L: 38.78. T5 — RG F1: 72, BLEURT: 44.41, ROUGE-1: 48.26, ROUGE-2: 27.63, ROUGE-L: 38.77. GPT2-Pubmed — RG F1: 78, BLEURT: 46.33, ROUGE-1: 48.37, ROUGE-2: 29.55, ROUGE-L: 40.19. SciFive — RG F1: 79, BLEURT: 47.81, ROUGE-1: 52.10, ROUGE-2: 32.62, ROUGE-L: 43.31. Mechanism sentence classifier (BioELECTRA) macro F1: 74%. Manual evaluation on best model (SciFive pretrained): model generates some mechanism in 79% of cases, supported by inputs in 53% of cases, scientifically correct in 58% of cases, and acceptable on all manual criteria in 32% of cases.

**Validation**: Validation/dev set of 1,000 instances used for hyperparameter tuning and model selection; a curated clean partition of 125 instances manually evaluated by five biomedical experts for dataset quality; manual evaluation of model outputs conducted with three biomedical experts on 100 instances.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
