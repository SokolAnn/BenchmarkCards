# MEDDISTANT 19

## 📊 Benchmark Details

**Name**: MEDDISTANT 19

**Overview**: This work presents a more accurate benchmark MEDDISTANT 19 for broad-coverage distantly supervised biomedical relation extraction that addresses shortcomings in existing benchmarks (notably train-test triples overlap) and is obtained by aligning MEDLINE abstracts with the widely used SNOMED CT knowledge base.

**Data Type**: text (entity-linked sentences; bag-level sentence groups for relation extraction)

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- UMLS.v1
- DTI
- UMLS.v2
- BioRel
- UMLS.v3
- TBGA

**Resources**:
- [Resource](https://arxiv.org/abs/2204.04779)
- [GitHub Repository](https://github.com/suamin/MedDistant19)
- [GitHub Repository](https://github.com/pminervini/meddistant-baselines)
- [GitHub Repository](https://github.com/allenai/scispacy)
- [Resource](https://lhncbc.nlm.nih.gov/ii/information/MBR/Baselines/2019.html)
- [Resource](https://uts.nlm.nih.gov/license.html)
- [Resource](https://download.nlm.nih.gov/umls/kss/2019AB/umls-2019AB-full.zip)

## 🎯 Purpose and Intended Users

**Goal**: Introduce an accurate broad-coverage distantly supervised biomedical relation extraction benchmark (MEDDISTANT 19) by aligning PubMed MEDLINE abstracts with SNOMED CT and addressing train-test KG triple overlap and data construction inconsistencies.

**Target Audience**:
- Machine Learning Researchers
- Biomedical Natural Language Processing Researchers
- Model Developers

**Tasks**:
- Relation Extraction
- Corpus-level Triples Extraction
- Sentence-level Relation Detection

**Limitations**: Limited scope of ontologies (focused on SNOMED CT); limited subset of relation types (e.g., does not include may_treat); lacks coverage of some relations such as protein-protein interactions, drug side-effects, and gene relations from other vocabularies (e.g., RxNorm, Gene Ontology). MEDDISTANT 19 is automatically-created and susceptible to noise and should be approached carefully as a potential source for biomedical knowledge.

## 💾 Data

**Source**: PubMed MEDLINE abstracts published up to 2019 (32,151,899 abstracts) aligned with SNOMED CT via a distilled UMLS2019AB; entity linking performed with ScispaCy.

**Size**: 450,071 training instances; 39,434 validation instances; 91,568 test instances; 20,256 unique entities; 22 relations (plus NA); 88,861 training bags; 10,475 validation bags; 22,606 test bags; 150,173,169 unique sentences extracted from MEDLINE.

**Format**: JSON (OpenNRE-compatible format; examples provided in appendix)

**Annotation**: Automatically generated via distant supervision by aligning SNOMED CT/UMLS triples to text using ScispaCy entity linking; negative sampling to create NA labels; no manual expert annotation for dataset creation (automatically-created).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (baseline neural models fine-tuned on dataset)
- Automated metrics (corpus- and sentence-level)
- Bag-level and sentence-level evaluation

**Metrics**:
- Area Under the Precision-Recall Curve (AUC, corpus-level)
- Micro-F1
- Macro-F1
- Precision
- Recall
- F1 Score
- Precision-at-k (P@k) for k in {100,200,300,1000,2000}

**Calculation**: Corpus-level AUC computed on the Precision-Recall curve; Micro-F1 and Macro-F1 computed at corpus-level; Precision-at-k computed for top-ranked triples; sentence-level Precision, Recall, and F1 computed for sentence-level relation detection. Macro-F1 reported due to imbalance of relational instances.

**Interpretation**: Higher AUC and F1 indicate better corpus-level relation extraction performance. Macro-F1 is used to evaluate per-relation performance due to class imbalance. Precision-at-k reflects top-scoring triple precision.

**Baseline Results**: Best reported baseline: BERT fine-tuned at sentence-level with AVG pooling achieved AUC 79.9, F1-micro 76.2, F1-macro 65.4 on the inductive split (Table 10). Sentence-level results for BERT+sent+AVG: Precision 0.79, Recall 0.65, F1 0.71 (Table 9).

**Validation**: Inductive KG split method (Daza et al., 2021) used to ensure no overlap of triples between train/validation/test (split ratios 70%/10%/20%). Additional validation steps include removing mention-level overlap across splits, type-based mention pruning (removing mentions appearing >10,000 times), enforcing type and role constraints in negative sampling, and creating a transductive split for comparison.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Data Laws
- Misuse

**Atlas Risks**:
- **Accuracy**: Data contamination, Poor model accuracy
- **Privacy**: Personal information in data
- **Data Laws**: Data usage restrictions
- **Misuse**: Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: Overestimation of model performance due to train-test triples overlap (train-test leakage) and potential misuse or redistribution without respecting UMLS licensing.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Uses publicly available PubMed MEDLINE abstracts (mostly English). Authors note they cannot guarantee the absence of confidential or sensitive information (e.g., clinical findings that reveal age/gender) and did not perform a thorough analysis to distill such information.

**Data Licensing**: Use of the benchmark requires signing the UMLS license/agreement. UMLS contains copyrighted material; users must respect source ontology licenses and obtain agreements for copyrighted sources before commercial or production use (see UMLS license).

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
