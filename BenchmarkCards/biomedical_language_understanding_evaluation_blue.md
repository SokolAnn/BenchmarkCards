# Biomedical Language Understanding Evaluation (BLUE)

## 📊 Benchmark Details

**Name**: Biomedical Language Understanding Evaluation (BLUE)

**Overview**: We introduce the Biomedical Language Understanding Evaluation (BLUE) benchmark to facilitate research in the development of pre-training language representations in the biomedicine domain. The benchmark consists of five tasks with ten datasets that cover both biomedical and clinical texts with different dataset sizes and difficulties.

**Data Type**: text (sentence pairs, token-level mentions, relation-labeled sentences, multi-label documents, premise-hypothesis pairs)

**Domains**:
- Natural Language Processing
- Biomedical Research
- Healthcare

**Similar Benchmarks**:
- General Language Understanding Evaluation (GLUE)

**Resources**:
- [GitHub Repository](https://github.com/ncbi-nlp/BLUE_Benchmark)
- [GitHub Repository](https://github.com/ncbi-nlp/NCBI_BERT)
- [Resource](http://tabilab.cmpe.boun.edu.tr/BIOSSES/)
- [Resource](https://spacy.io/)
- [Resource](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-v/track-3-cdr/)
- [Resource](https://physionet.org/works/ShAReCLEFeHealth2013/)
- [Resource](http://labda.inf.uc3m.es/ddicorpus)
- [Resource](https://biocreative.bioinformatics.udel.edu/news/corpora/chemprot-corpus-biocreative-vi/)
- [Resource](https://www.i2b2.org/NLP/DataSets/)
- [Resource](https://www.cl.cam.ac.uk/~sb895/HoC.html)
- [Resource](https://physionet.org/physiotools/mimic-code/mednli/)
- [Resource](https://nlp.stanford.edu/projects/glove/)
- [Resource](https://allennlp.org/elmo)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in the development of pre-training language representations in the biomedicine domain by providing a benchmark of five tasks with ten biomedical and clinical corpora, code for data construction and evaluation, pretrained models, and baseline results.

**Target Audience**:
- BioNLP community
- Biomedical NLP researchers
- Model Developers

**Tasks**:
- Sentence Similarity
- Named Entity Recognition
- Relation Extraction
- Document Multi-label Classification
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Preexisting datasets widely used by the BioNLP community: MedSTS, BIOSSES, BC5CDR (disease and chemical), ShARe/CLEF eHealth Task 1, DDI 2013, ChemProt, i2b2 2010, HoC (Hallmarks of Cancer), MedNLI. Pre-training corpora: PubMed abstracts and MIMIC-III clinical notes.

**Size**: See Table 1 (per-dataset splits as reported): MedSTS: 675 train, 75 dev, 318 test; BIOSSES: 64 train, 16 dev, 20 test; BC5CDR-disease: 4182 train, 4244 dev, 4424 test; BC5CDR-chemical: 5203 train, 5347 dev, 5385 test; ShARe/CLEFE: 4628 train, 1075 dev, 5195 test; DDI: 2937 train, 1004 dev, 979 test; ChemProt: 4154 train, 2416 dev, 3458 test; i2b2 2010: 3110 train, 11 dev, 6293 test; HoC: 1108 train, 157 dev, 315 test; MedNLI: 11232 train, 1395 dev, 1422 test. Pre-training corpora sizes: PubMed abstract >4,000M words; MIMIC-III >500M words.

**Format**: N/A

**Annotation**: Dataset-specific annotation procedures as stated in the paper: BIOSSES - five curators judged sentence similarity (scores 0-4); MedSTS - two medical experts graded semantic similarity (scores 0-5); BC5CDR - diseases and chemicals annotated independently by two human experts with medical training and curation experience; ShARe/CLEF - disorders annotated by two professionally trained annotators followed by adjudication; DDI - drug-drug interactions annotated by two expert pharmacists; ChemProt - chemical-protein interactions annotated by domain experts; i2b2 2010 - annotated by medical practitioners for relations; HoC - sentence-level annotation by an expert with 15+ years of cancer research experience; MedNLI - premise-hypothesis pairs graded by two board-certified radiologists.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation (fine-tuning pre-trained models)
- Fine-tuning of pre-trained language models (BERT, ELMo)

**Metrics**:
- Pearson correlation coefficient
- Precision
- Recall
- F1 Score
- Micro-averaged F1 Score
- Accuracy
- Macro-average (F1 and Pearson)

**Calculation**: Sentence similarity: Pearson correlation coefficient on sentence-pair similarity scores. Named Entity Recognition: strict precision, recall, and F1-score (span-level, strict matching). Relation extraction: micro-average precision, recall, and F1-score across relation types. Document multi-label classification: example-based F1-score at abstract level. Inference (MedNLI): overall accuracy. Total score: macro-average of F1-scores and Pearson scores.

**Interpretation**: Higher values of the reported metrics (Pearson, F1, Accuracy) indicate better performance. Overall system ranking is determined by the macro-average of per-task F1-scores and Pearson scores as the total score.

**Baseline Results**: The paper reports baseline results for ELMo, BioBERT, and several BERT variants (pre-trained on PubMed and on PubMed+MIMIC-III). The authors state that BERT-Base pre-trained on PubMed abstracts and MIMIC-III (BERT-Base (P+M)) achieved the best results across the five tasks (see Table 3 for per-task scores and comparisons).

**Validation**: Used standard training/development/test splits from respective shared tasks where available; BIOSSES was randomly split 80% train and 20% test due to lack of standard split. Model selection was performed using the development set (selecting the best model on the dev set after several runs for small datasets).

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
