# A Dataset for N-ary Relation Extraction of Drug Combinations

## 📊 Benchmark Details

**Name**: A Dataset for N-ary Relation Extraction of Drug Combinations

**Overview**: An expert-annotated dataset for extracting information about the efficacy of drug combinations from the scientific literature; the dataset is the first relation extraction dataset consisting of variable-length relations and relations predominantly require language understanding beyond the sentence level.

**Data Type**: text (annotated biomedical abstracts with drug mention spans and enclosing context)

**Domains**:
- Natural Language Processing
- Biomedical Research

**Languages**:
- English

**Similar Benchmarks**:
- DDI
- BioCreative V CDR
- BioCreative VI
- SciERC

**Resources**:
- [Resource](https://huggingface.co/datasets/allenai/drug-combo-extraction)
- [GitHub Repository](https://github.com/allenai/drug-combo-extraction)
- [Resource](https://huggingface.co/allenai/drug-combo-classifier-pubmedbert-dapt)
- [Resource](http://drugcombdb.denglab.org/download/)

## 🎯 Purpose and Intended Users

**Goal**: Provide an expert-annotated resource and baseline models to enable extraction of drug combinations and their reported efficacy from scientific literature, and to serve as a test-bed for variable-length n-ary relation extraction and document-level relation understanding.

**Target Audience**:
- Medical professionals
- Natural Language Processing researchers
- Model developers
- Biomedical domain experts

**Tasks**:
- Relation Extraction
- Document-level Relation Extraction
- N-ary Relation Extraction
- Information Extraction

**Limitations**: Annotating such data is costly; initial sampling without trigger phrases produced a dataset highly skewed toward NO_COMB, so a trigger-based sampling strategy was used which may impose lexical restrictions (the authors note triggers are recall oriented but not clearly indicative). Agreement for a discouraged-combination label was low and was therefore merged into OTHER_COMB.

## 💾 Data

**Source**: Collected from PubMed abstracts using the SPIKE extractive search tool; drug list curated from DrugBank (with removal of non-pharmacological interventions) and the FDA Orange Book; additional distant supervision from DrugComboDB.

**Size**: 1634 annotated abstracts; split into 1362 train and 272 test instances; 1248 annotated relations (838 POS_COMB, 410 OTHER_COMB); relation arities: 900 binary, 226 ternary, 69 four-ary, 53 five-ary or more.

**Format**: N/A

**Annotation**: Manual annotation by seven graduate students in biomedical engineering using the Prodigy annotation tool, supervised by a domain expert; test instances received two annotations with domain-expert arbitration for disagreements; annotators marked all subsets of drugs participating in combinations and indicated whether context was required.

## 🔬 Methodology

**Methods**:
- Automated metrics (Precision, Recall, F1)
- Baseline model evaluation using BERT-based architectures (SciBERT, BlueBERT, PubmedBERT, BioBERT) adapted from PURE
- Domain-adaptive pretraining (DAPT) on in-domain PubMed abstracts
- Rule-based baseline
- Human-level annotation comparison and inter-annotator agreement analysis

**Metrics**:
- Precision
- Recall
- F1 Score (Positive Combination F1, Any Combination F1)
- Exact Match
- Partial Match (partial-credit scoring)

**Calculation**: Standard precision, recall and F1 are used. For Partial Match, a predicted combination is scored as (shared_drugs / total_drugs); when multiple partial matches exist, the match with maximum overlap is used. Recall is computed over all gold relations; precision is computed over identified relations. Two aggregated metrics are reported: averaged Positive Combination F1 (POS_COMB vs. rest) and averaged Any Combination F1 (POS_COMB or OTHER_COMB vs. NO_COMB).

**Interpretation**: Higher F1 indicates better extraction performance. Partial Match is a more relaxed metric that gives partial credit for partially-correct subsets. Any Combination F1 is an easier metric than Positive Combination F1 because it counts both POS_COMB and OTHER_COMB as correct compared to NO_COMB.

**Baseline Results**: Human-Level (Exact/Partial): Any Combination F1 86.1 / 88.9; Positive Combination F1 79.6 / 83.4. Rule-based baseline (Exact/Partial) Positive Combination F1 31.8 / 45.6; Any Combination F1 39.1 / 57.4. PubmedBERT w/ DAPT (Exact/Partial): Positive Combination F1 61.8 / 67.7; Any Combination F1 69.4 / 77.5. (Mean and standard deviations reported across 4 seeds for models.)

**Validation**: Test set instances received two independent annotations and disagreements were resolved by a domain expert to create the test set. Inter-annotator agreement was measured using an adapted pairwise F1 metric (allowing partial matches). Model comparisons used a paired multi-bootstrap hypothesis test with 1000 bootstrap samples sampling over random seeds and test-set subsets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
