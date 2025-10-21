# EBM-COMET

## 📊 Benchmark Details

**Name**: EBM-COMET

**Overview**: We introduce “EBM-COMET”, a dataset in which 300 Randomised Clinical Trial (RCT) PubMed abstracts are expertly annotated for clinical outcomes. Unlike prior related datasets that use arbitrary outcome classifications, we use labels from a taxonomy recently published to standardise outcome classifications.

**Data Type**: text (annotated clinical trial abstracts; token-level outcome phrase spans)

**Domains**:
- Evidence Based Medicine
- Clinical Trials
- Healthcare
- Natural Language Processing

**Similar Benchmarks**:
- EBM-NLP
- EBM-NLP rev

**Resources**:
- [GitHub Repository](https://github.com/MichealAbaho/ODP-tagger)
- [GitHub Repository](https://github.com/flairNLP/flair)
- [GitHub Repository](https://github.com/allenai/bilm-tf)
- [Resource](https://ebm-nlp.herokuapp.com/)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate outcome detection in Evidence Based Medicine by providing EBM-COMET, a dataset of 300 RCT PubMed abstracts expertly annotated for clinical outcomes using a standardised outcome taxonomy, and to assess contextualised representations for the outcome detection task.

**Target Audience**:
- Biomedical domain audience
- Clinicians

**Tasks**:
- Outcome Detection (token-level outcome phrase extraction)
- Named Entity Recognition
- Token-level Sequence Labeling
- Outcome Type Classification

**Limitations**: Annotations were performed jointly by two domain experts; inter-annotator agreement was not reported. Dataset comprises 300 RCT abstracts (5,193 sentences).

## 💾 Data

**Source**: 300 Randomised Clinical Trial (RCT) abstracts fetched from open access PubMed using the Entrez API; abstracts reviewed to exclude non-human studies and replaced when needed; outcomes annotated by two domain experts with outcome domains drawn from a published taxonomy.

**Size**: 300 abstracts; 5,193 sentences total; train/dev/test split: 3,895 / 779 / 519 sentences; sentences with outcome phrases in train/dev/test: 1,569 / 451 / 221.

**Format**: Structured format (annotations extracted into an Excel sheet); original annotations created in Microsoft Word using XML-like tags to demarcate spans.

**Annotation**: Manual expert annotation by two domain experts jointly annotating granular outcome spans and assigning outcome domain labels from the referenced taxonomy; annotators used XML-like tags and domain symbol notation; annotators did not annotate independently.

## 🔬 Methodology

**Methods**:
- Fine-tuning pre-trained contextualised language models (e.g., BioBERT, SciBERT, ClinicalBERT, BioELMo, BioFLAIR)
- Feature-extraction using frozen contextualised embeddings with a custom ODP-tagger (BiLSTM + POS features + CRF)
- PCA dimensionality reduction for large embedding vectors (BioFLAIR, BioELMo)
- Automated evaluation using token-level metrics and strict full-phrase exact-match evaluation

**Metrics**:
- Macro-average F1 Score
- F1 Score
- Precision
- Recall / Sensitivity
- Specificity

**Calculation**: Two evaluation criteria: (1) token-level evaluation using BIO tagging (word-level), and (2) strict full outcome phrase exact-match evaluation where a model is rewarded only when it correctly predicts all tokens of an outcome phrase in sequence (exact match). Specificity calculated as True Negative Rate on a word-by-word basis.

**Interpretation**: Higher F1, Precision and Recall indicate better outcome phrase detection. Strict full-phrase evaluation is more informative for biomedical users and yields lower scores when models partially detect phrase tokens. Specificity is high due to many True Negatives counted word-by-word.

**Baseline Results**: Best reported model: Fine-tuned BioBERT on EBM-COMET achieved 81.5% F1, 81.3% sensitivity (Recall) and 98.0% specificity. Fine-tuned BioBERT on EBM-NLP rev achieved 53.1% F1 (token-level). Feature-extraction (ODP-tagger) and other models reported in Table 3 (e.g., SciBERT 77.6% on EBM-COMET fine-tuned; W2V ODP-tagger 59.3% on EBM-COMET).

**Validation**: Datasets partitioned with 75% training, 15% development, and 10% testing. Hyperparameters tuned on the development set (EBM-NLP rev dev used to tune ODP-tagger and fine-tuned models). No independent inter-annotator agreement reported because annotations were done jointly.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Governance

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Governance**: Lack of data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
