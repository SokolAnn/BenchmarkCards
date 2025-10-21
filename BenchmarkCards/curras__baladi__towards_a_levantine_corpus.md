# Curras + Baladi: Towards a Levantine Corpus

## 📊 Benchmark Details

**Name**: Curras + Baladi: Towards a Levantine Corpus

**Overview**: This paper presents two-fold contributions: a full revision of the Palestinian morphologically annotated corpus (Curras), and a newly annotated Lebanese corpus (Baladi). Both corpora can be used as a more general Levantine corpus. Baladi consists of around 9.6K morphologically annotated tokens. Each token was manually annotated with several morphological features and using LDC’s SAMA lemmas and tags. Curras was revised by refining all annotations for accuracy, normalization and unification of POS tags, and linking with SAMA lemmas.

**Data Type**: text (token-level morphological annotations)

**Domains**:
- Natural Language Processing

**Languages**:
- Palestinian Arabic
- Lebanese Arabic

**Similar Benchmarks**:
- Curras
- Penn Arabic Treebank (PATB)
- CALLHOME Egyptian Arabic corpus
- ARZATB (Egyptian Tree Bank)
- MADAR

**Resources**:
- [Resource](https://portal.sina.birzeit.edu/curras)

## 🎯 Purpose and Intended Users

**Goal**: Provide Baladi, a Lebanese morphologically annotated corpus (9.6K tokens), and a revised Curras (Palestinian corpus) to form a more general Levantine corpus compatible with LDC's SAMA tags and lemmas.

**Tasks**:
- Morphological annotation
- Part-of-Speech tagging
- Lemmatization
- Tokenization
- Glossing

**Limitations**: Baladi size is relatively small (9.6K tokens). The authors did not preprocess the text (no unification of letter variations, no removal of diacritics, no correction of typos). Arabizi (Arabic written in Latin letters) was avoided and not included.

## 💾 Data

**Source**: Baladi: manually collected Lebanese texts from Facebook posts, blog posts, and traditional poems. Curras (revised): originally collected from Facebook, Twitter, and scripts of the Palestinian series "Watan Aa Watar" (original Curras collection).

**Size**: Baladi: 9.6K tokens; Curras (revised): 55,889 tokens; combined ~65.2K tokens

**Format**: Merged into a single raw text file; annotations represented in a spreadsheet (Google Sheet / AnnoSheet) with one row per token and separate columns for annotation fields (sentence ID, token ID, token text, CODA, prefixes, stem, suffixes, POS, MSA lemma, dialect lemma, gloss, person, aspect, gender, number).

**Annotation**: Manual annotation by four linguists over ten months using AnnoSheet (Google Sheet) enhanced with JavaScript validation and lookup features. Annotations used LDC's SAMA lemmas and tags (MSA lemma restricted to SAMA where possible); annotators re-used solutions from the revised Curras Solutions table; daily validation via a Google Colab application; manual expert corrections for disambiguation where necessary.

## 🔬 Methodology

**Methods**:
- Inter-annotator agreement (Cohen's Kappa)
- Expert annotation comparison using Precision and Recall (and F1-Score)
- Automated validation and disambiguation tools (JavaScript validation in AnnoSheet; POS parser; lemma disambiguator; Python sklearn.metrics for metric computation)

**Metrics**:
- Cohen's Kappa
- Precision
- Recall
- F1-Score

**Calculation**: Cohen's Kappa computed as (po - pe) / (1 - pe) where po is observed agreement and pe is expected agreement. Precision = tp / (tp + fp). Recall = tp / (tp + fn). F1-Score = 2 * precision * recall / (precision + recall). Metric computations used the Python sklearn.metrics package; precision and recall computed with the expert annotator as reference.

**Interpretation**: Kappa interpretation follows McHugh (2015): aspect and suffix features scored moderate agreement (.4-.6), stem and prefix scored near-perfect agreement (> .81), and the rest scored substantial agreement (.61-.80). Reported overall Cohen's Kappa: 0.785. Reported overall F1-Score: 0.901.

**Baseline Results**: Inter-annotator Cohen's Kappa per feature (selected): Stem 0.884; Prefix 0.860; Suffixes 0.738; POS 0.821; Person 0.629; Aspect 0.911; Gender 0.687; Number 0.741. Overall Kappa: 0.785. Precision / Recall / F1 per feature (selected): Stem Precision 0.9036, Recall 0.8935, F1 0.893; Prefixes Precision 0.964, Recall 0.95, F1 0.955; Suffixes Precision 0.948, Recall 0.895, F1 0.915; POS Precision 0.898, Recall 0.85, F1 0.853; Overall Precision 0.918, Recall 0.894, F1 0.901.

**Validation**: Inter-annotator evaluation used a random selection of sentences consisting of 400 tokens (4.2% of Baladi). These 400 tokens were divided so each annotator re-annotated ~100 tokens annotated by another annotator. An expert annotator reviewed and corrected the 400 tokens; corrections used to compute precision, recall, and F1. Automated daily validation ran via Google Colab; annotation validation triggers and lookup features ran in the AnnoSheet; a POS parser and lemma disambiguator were used to validate and disambiguate Curras entries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
