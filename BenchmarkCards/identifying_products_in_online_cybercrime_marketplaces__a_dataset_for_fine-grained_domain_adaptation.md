# Identifying Products in Online Cybercrime Marketplaces: A Dataset for Fine-grained Domain Adaptation

## 📊 Benchmark Details

**Name**: Identifying Products in Online Cybercrime Marketplaces: A Dataset for Fine-grained Domain Adaptation

**Overview**: A dataset and evaluation task for identifying products being bought and sold in online cybercrime forums. The authors formulate a token-level product identification task (a hybrid of slot-filling information extraction and named entity recognition), annotate data from four forums (Darkode, Hack Forums, Blackhat, and Nulled), characterize cross-forum (fine-grained domain) differences, evaluate supervised and semi-supervised/domain-adaptation methods, and release a dataset of 1,938 annotated posts.

**Data Type**: text (token-level annotations of forum posts: product mentions)

**Domains**:
- Natural Language Processing
- Cybersecurity

**Similar Benchmarks**:
- TAC KBP
- CoNLL
- ACE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset and evaluation setup for extracting product mentions in online cybercrime marketplace forums and to study fine-grained domain adaptation for this task.

**Target Audience**:
- Researchers in Natural Language Processing
- Researchers in Cybersecurity

**Tasks**:
- Named Entity Recognition
- Information Extraction
- Slot Filling
- Token-level product extraction

**Limitations**: Annotation excludes product mentions outside the first and last 10 lines of each post; annotations are token-level (head word of multiword product NP annotated) rather than full span NP annotations; dataset consists of 1,938 annotated posts across four forums; standard semi-supervised and domain-adaptation techniques show limited effectiveness on cross-forum generalization.

**Out of Scope Uses**:
- Features of products are not annotated
- Generic product references (e.g., this, them) are not annotated
- Product mentions inside “vouches” (reviews from other users) are not annotated
- Product mentions outside of the first and last 10 lines of each post are not annotated

## 💾 Data

**Source**: Posts collected from four online forums: Darkode, Hack Forums, Blackhat, and Nulled (all available posts were collected and a subset was annotated).

**Size**: 1,938 annotated posts; 130,336 annotated tokens; annotators considered 478,176 tokens during labeling.

**Format**: Tokenized text (annotations performed on data tokenized with the Stanford CoreNLP toolkit); full annotation guide provided as a PDF with the data release.

**Annotation**: Token-level annotation labeling each token as a product or not. Annotation guidelines developed over six preliminary rounds (560 posts). Three annotators labeled many portions (majority vote used to merge annotations); development/test disagreements were discussed and resolved. Multiword product expressions annotated by head word; methods (verbs) may be annotated in addition to nominal references.

## 🔬 Methodology

**Methods**:
- Supervised learning: binary token classifier (SVM) and token-level CRF
- Post-level latent SVM classifier (select one token/NP per post)
- Retrained Stanford NER system
- Baselines: most-frequent noun/verb, dictionary/gazetteer lookup, first noun phrase baseline
- Semi-supervised features: Brown clusters
- Type-level annotation via gazetteers
- Token-level annotation and domain adaptation via feature-duplication (Daume III, 2007)
- Evaluation with human annotator baselines

**Metrics**:
- Precision
- Recall
- F1 Score (token-level)
- Precision
- Recall
- F1 Score (type-level product extraction per post)
- Post-level Accuracy
- NP-level (phrase-level) Precision/Recall/F1

**Calculation**: Token-level: compute precision, recall, and F1 over tokens labeled as products. Type-level product extraction: compare the set of product types in a post (predicted vs. gold) using precision, recall, and F1; product type matching uses lowercasing and stemming with an edit-distance threshold (two product tokens are same type if after lowercasing and stemming edit distance ≤0 for token length ≤4, ≤1 for length 5–7, ≤2 for length ≥8). Post-level accuracy: check whether the first product type extracted by the system is contained in the annotated set. Phrase-level evaluation: project token-level annotations to noun phrases by parsing (using Chen and Manning parser) and labeling the largest NP containing the annotated token up to length 7; verbs left as single tokens.

**Interpretation**: Token-level metrics closely mimic the annotation process. Type-level (per-post) metrics approximate KBP-style slot-filling and favor systems that correctly identify product types for posts even if not all token occurrences are retrieved. Post-level accuracy is appropriate because most posts contain a single core product; NP-level evaluation is more forgiving since token distinctions within NPs are erased.

**Baseline Results**: Provided in-paper (e.g., human annotator token F1 ~89.8 on Darkode; various system results in Tables 2–4).

**Validation**: Annotation quality assessed via inter-annotator agreement measured with Fleiss' Kappa (reported values in Table 1, e.g., Darkode 0.62/0.66; Hack Forums 0.58/0.65; Blackhat 0.66/0.67; Nulled 0.77). Annotation guidelines refined across six preliminary rounds with full discussion and resolution of disagreements; majority-vote merging for annotations; development/test disagreements were discussed and resolved to produce final annotations.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
