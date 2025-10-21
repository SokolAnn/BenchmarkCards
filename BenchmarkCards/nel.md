# NEL

## 📊 Benchmark Details

**Name**: NEL

**Overview**: An entity linking dataset NEL that focuses on the NIL prediction problem. NEL categorizes NIL mentions into two patterns (Missing Entity and Non-Entity Phrase), is constructed by taking ambiguous entities as seeds, collecting mention contexts from the Wikipedia corpus, performing human annotation, and applying entity masking to ensure about 30% of mentions link to NIL. It is intended to diagnose models' ability to predict NIL.

**Data Type**: text (mention-context and candidate-entity pairs)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AIDA
- MSNBC
- WNED-WIKI
- TAC-KBP
- ACE

**Resources**:
- [GitHub Repository](https://github.com/solitaryzero/NIL_EL)
- [Resource](https://arxiv.org/abs/2305.15725)
- [Resource](https://dumps.wikimedia.org)
- [GitHub Repository](https://github.com/facebookresearch/BLINK)
- [Resource](https://creativecommons.org/licenses/by-sa/3.0/)

## 🎯 Purpose and Intended Users

**Goal**: To provide an entity linking dataset focusing on NIL prediction that covers two patterns of NIL data (Missing Entity and Non-Entity Phrase) and can act as a benchmark for diagnosing models' ability to identify mentions that should be linked to NIL.

**Target Audience**:
- Researchers

**Tasks**:
- Entity Linking
- NIL Prediction

**Limitations**: The granularity of the typing system remains to be discussed: a system with too many types would introduce noise to long-tail types, while insufficient types would weaken disambiguation. Combining the entity typing task with PLM-based semantic encoders requires a fixed type system and further finetuning; integrating the entity typing task into pretraining is left to future work.

## 💾 Data

**Source**: Built from the 2021-07 English Wikipedia dump; Wikidata used to build the typing system. Data collected by taking ambiguous entities as seeds, mining mention contexts and candidate entities from Wikipedia, then human annotation and entity masking.

**Size**: 9,924 entries (6,593 positive examples and 3,331 negative examples); covers 1,000 mentions and 3,840 related entities; average 3.80 candidate entities per mention; dataset split train/validation/test = 80%/10%/10%.

**Format**: N/A

**Annotation**: Human annotation with 3 annotators per entry and an expert resolving disagreements; final answer is the agreement of 3 annotators or the expert decision. Inter-annotator agreement is 94.61%. Entity masking applied to 10% of positive entries to control NIL percentage.

## 🔬 Methodology

**Methods**:
- Automated metrics (accuracy on entity linking and NIL prediction)
- Model-based evaluation (evaluation of PLM-based models: BLINK, CLINK, GENRE using bi-encoder and cross-encoder structures)
- Ablation studies (type information and amount/type of NIL training data)

**Metrics**:
- Accuracy (reported as Non-NIL accuracy, NIL accuracy, and Overall accuracy (OAC))
- Inter-annotator agreement

**Calculation**: Similarity scores between mention context and each candidate entity are computed as a weighted sum of semantic similarity and type similarity: s(c,e)=λ*s_sem(c,e)+(1-λ)*s_type(c,e). A nil threshold ϵ=0.5 is used: if max_e s(c,e) >= 0.5 the argmax entity is chosen; if all s(c,e) < 0.5 the mention is linked to NIL. Training loss combines binary classification loss (Ls) and typing loss (Lt). Accuracy metrics are computed for Non-NIL (Non-NAC), NIL (NAC), and Overall (OAC).

**Interpretation**: If models are not evaluated with NIL prediction, reported accuracy may be inflated. The presence and type distribution of NIL examples in training data significantly affect NIL prediction accuracy. Entity typing as an auxiliary training task improves embedding quality and overall accuracy even when type similarity is not used at inference.

**Baseline Results**: On NEL: BLINK-bi — Non-NIL Acc 72.27, NIL Acc 88.59, OAC 77.74; CLINK-bi — Non-NIL Acc 79.24, NIL Acc 79.28, OAC 79.25; GENRE — Non-NIL Acc 54.00, NIL Acc 62.84, OAC 56.96; BLINK-cross — Non-NIL Acc 84.09, NIL Acc 88.89, OAC 85.70; CLINK-cross — Non-NIL Acc 86.97, NIL Acc 89.19, OAC 87.71. (BERT-large used as encoder base for BLINK/CLINK; BART-large for GENRE.)

**Validation**: Annotation validation: 3 annotators per entry with an expert resolving disagreements; inter-annotator agreement 94.61%. Entity masking applied to 10% of positive entries to simulate missing entities. Dataset split into train/validation/test by 80%/10%/10%.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness

**Atlas Risks**:
- **Governance**: Unrepresentative risk testing, Lack of testing diversity

**Potential Harm**: Model trained on NEL may experience under-exposure of other entity types, which could damage transferability and lead to undesired outputs on other datasets.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The Wikipedia corpus and Wikidata types are obtained via the Wikimedia dump under the CC BY-SA 3.0 license. The authors state that these datasets have been widely used and believe they have been anonymized and desensitized. Annotators were informed about how the data will be used and release was recorded in contract.

**Data Licensing**: CC BY-SA 3.0 (Wikipedia dump and Wikidata types). AIDA, MSNBC, and WNED-WIKI noted as shared under CC BY-SA 3.0.

**Consent Procedures**: Human annotators (3 annotators and 1 expert) were recruited through commercial annotation companies, paid adequately under agreed working time and price, and informed about how annotated data will be used; this was recorded in contract.

**Compliance With Regulations**: Not Applicable
