# Borrowing or Codeswitching? Annotating for Finer-Grained Distinctions in Language Mixing

## 📊 Benchmark Details

**Name**: Borrowing or Codeswitching? Annotating for Finer-Grained Distinctions in Language Mixing

**Overview**: We present a new corpus of Twitter data annotated for codeswitching and borrowing between Spanish and English. The corpus contains 9,500 tweets annotated at the token level with code switches, borrowings, and named entities.

**Data Type**: text (tweets with token-level language and borrowing annotations)

**Domains**:
- Natural Language Processing
- Sociolinguistics

**Languages**:
- Spanish
- English

**Similar Benchmarks**:
- LinCE
- LM2013

**Resources**:
- [GitHub Repository](https://github.com/lirondos/borrowing-or-codeswitching)
- [Resource](https://dle.rae.es/)
- [Resource](https://www.asale.org/recursos/diccionarios/damer)
- [GitHub Repository](https://github.com/huggingface/transformers/tree/master/examples/pytorch/token-classification)

## 🎯 Purpose and Intended Users

**Goal**: To provide a corpus that distinguishes lexical borrowing from codeswitching in Spanish-English Twitter data to enable study and modeling of these phenomena.

**Target Audience**:
- Researchers studying codeswitching and borrowing
- Model developers in Natural Language Processing

**Tasks**:
- Language Identification (token-level)
- Named Entity Recognition
- Borrowing detection / Codeswitching classification

**Limitations**: This corpus is not designed to be an evenly-balanced English-Spanish codeswitching dataset; it is primarily Spanish. The distinction between codeswitching and borrowing is fuzzy and many gray areas remain. The geographic distribution of speakers and dialectal varieties in the dataset are unknown.

## 💾 Data

**Source**: Reannotation of the LM2013 codeswitching-dense corpus (Lignos and Marcus, 2013), which selected tweets from the Spanish subset of Burger et al. (2011).

**Size**: 9,500 tweets; 198,706 tokens

**Format**: Stand-off annotation (stand-off annotation files released; file encoding/format not specified)

**Annotation**: Manual token-level reannotation following explicit guidelines (labels: SPA, ENG, OTH, BOR, ENT, N). Reannotation and adjudication were completed by a native Spanish speaker with a background in linguistics; adjudication completed for all 9,500 tweets.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (Transformer-based token classification)
- Train/dev/test split 80/10/10

**Metrics**:
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Token-level evaluation. Micro-averaged precision, recall, and F1 reported. Accuracy reported at token level. Results reported from a single run per model.

**Interpretation**: Higher token-level Accuracy and F1 indicate better performance at language/borrowing labeling. Authors note mBERT and BETO achieved the highest F1 (~96.65) and caution differences between top models may not be meaningful without further experimentation.

**Baseline Results**: mBERT: Accuracy 96.88, Precision 96.69, Recall 96.61, F1 96.65; BETO: Accuracy 96.91, Precision 96.69, Recall 96.60, F1 96.64; RoBERTa-BNE: Accuracy 93.73, Precision 93.19, Recall 93.23, F1 93.21; RoBERTa Twitter: Accuracy 93.39, Precision 92.82, Recall 92.86, F1 92.84.

**Validation**: Annotation adjudication completed for all 9,500 tweets. Model evaluation used an 80/10/10 train/development/test split. No additional reliability metrics (e.g., inter-annotator agreement scores) or cross-validation procedures reported for model evaluation in the paper.

## ⚠️ Targeted Risks

**Risk Categories**:
- Transparency
- Governance

**Atlas Risks**:
- **Transparency**: Uncertain data provenance
- **Governance**: Incomplete usage definition

**Demographic Analysis**: The authors state that the geographic distribution of speakers and dialectal varieties in the dataset is unknown.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Text is distributed in compliance with Twitter Terms of Service. No additional anonymization procedures are described.

**Data Licensing**: Stand-off annotation released under Creative Commons CC BY 4.0; the text is distributed in compliance with Twitter Terms of Service.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data distribution stated to be in compliance with Twitter Terms of Service; no mention of GDPR, CCPA, or other regulatory compliance.
