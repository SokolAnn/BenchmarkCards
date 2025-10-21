# BenCoref: A Multi-Domain Dataset of Nominal Phrases and Pronominal Reference Annotations

## 📊 Benchmark Details

**Name**: BenCoref: A Multi-Domain Dataset of Nominal Phrases and Pronominal Reference Annotations

**Overview**: We introduce a new dataset, BenCoref, comprising coreference annotations for Bengali texts gathered from four distinct domains. This relatively small dataset contains 5,200 mention annotations forming 502 mention clusters within 48,569 tokens. We describe the process of creating this dataset and report performance of multiple models trained using BenCoref.

**Data Type**: text (coreference-annotated nominal and pronominal mentions; mention clusters)

**Domains**:
- Biography
- Descriptive (Wikipedia-like articles)
- Story
- Novel

**Languages**:
- Bengali

**Similar Benchmarks**:
- ACE
- OntoNotes
- WikiCoref
- LitBank

**Resources**:
- [GitHub Repository](https://github.com/ShadmanRohan/BenCoref)

## 🎯 Purpose and Intended Users

**Goal**: Introduce BenCoref, the first publicly available dataset of coreference annotations in Bengali collected from four diverse domains, describe the creation and annotation process, and evaluate end-to-end coreference resolution models trained on it.

**Tasks**:
- Coreference Resolution

**Limitations**: Relatively small dataset (48,569 tokens); annotation guideline described is incomplete and limited in scope; coreference link types have not been annotated and remain pending; the process of resolving annotator disagreements was not adequately documented.

## 💾 Data

**Source**: BnWikiSource and Banglapedia; story and novel texts sourced from copyright-free books of the 19th and 20th centuries; biographies and descriptive texts primarily from Banglapedia.

**Size**: 48,569 tokens; 5,200 mention annotations; 502 mention clusters; 122 train+dev documents and 37 test documents (total 159 documents).

**Format**: An index.csv file is included; annotations were created in WebAnno and exported and converted from character-level to token-level annotations.

**Annotation**: Manual annotation using WebAnno; annotators initially instructed to annotate noun phrases and their coreferences (primary noun phrases tagged as 'entity' and corresponding coreferences as 'ref'); guidelines adapted from OntoNotes; annotators focused on nominal and pronominal mentions; singletons were removed during post-annotation processing; two annotators annotated independently with a third annotator consulted to adjudicate disagreements to create the gold standard.

## 🔬 Methodology

**Methods**:
- Model training and evaluation with end-to-end neural coreference resolution systems (Bi-directional LSTM with span-ranking head; BERT-base; multilingual BERT for cross-lingual experiments)
- Automated evaluation using CONLL-2012 official evaluation scripts

**Metrics**:
- Identification of Mentions
- MUC
- B3
- CEAF (phi4)
- Precision
- Recall
- F1 Score
- Average F1 (MUC, B3, CEAF phi4)

**Calculation**: Metrics computed using the CONLL-2012 official evaluation scripts which calculate Identification of Mentions, MUC, B3 and CEAF. The main evaluation metric is the average F1 score of MUC, B3, and CEAF phi4.

**Interpretation**: Authors report that higher average F1 of MUC, B3 and CEAF phi4 indicates better coreference clustering. They state the model performance is reasonable given the dataset size; identification of mentions achieved relatively high scores while clustering performance decreased; zero-shot cross-lingual performance from English was poor, demonstrating need for language-specific resources.

**Baseline Results**: Reported test-average F1 (Avg column, Table 5) for BERT-base by domain: Biography 74.03; Story 45.38; Novel 44.10; Descriptive 43.35. Identification of Mentions F1 (Table 4) for BERT-base by domain: Biography 90.00; Story 73.79; Novel 73.43; Descriptive 62.66. Multilingual BERT (zero-shot) average F1 scores on test were very low (e.g., Biography 0.88; Story 1.19; Novel 1.40; Descriptive 1.47). Additional model variants (c2f + Glove, c2f + Fasttext) and parameter settings and their precision/recall/F1 are reported in Tables 4 and 5.

**Validation**: Two annotators independently annotated documents; disagreements were resolved by consulting a third annotator to produce adjudicated gold annotations. Based on the adjudicated gold, individual annotations achieved an average MUC score of 78.3 on the combined dataset while the combined inter-annotator MUC score was 67.6. The authors note that the disagreement resolution process was not adequately documented.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Governance

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Governance**: Lack of data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
