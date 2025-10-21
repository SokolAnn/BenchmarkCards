# CompLex: A New Corpus for Lexical Complexity Prediction from Likert Scale Data

## 📊 Benchmark Details

**Name**: CompLex: A New Corpus for Lexical Complexity Prediction from Likert Scale Data

**Overview**: Presents CompLex, the first English dataset for continuous lexical complexity prediction. The authors use a 5-point Likert scale to annotate complex words in texts from three sources/domains (the Bible, Europarl, and biomedical texts), resulting in a corpus of 9,476 sentences each annotated by around 7 annotators. The dataset includes single words and two-token multi-word expressions and is intended to support prediction of a continuous complexity value (Lexical Complexity Prediction).

**Data Type**: text (word-in-context instances: single words and two-token multi-word expressions annotated with 5-point Likert complexity scores)

**Domains**:
- Natural Language Processing
- Text Simplification

**Languages**:
- English

**Similar Benchmarks**:
- SemEval-2016 Task 11 (Complex Word Identification)
- CWI 2018 (Complex Word Identification shared task)

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Introduce CompLex, a new English dataset for continuous lexical complexity prediction using a 5-point Likert scale across three genres (Bible, Europarl, biomedical), and provide baseline experiments for predicting lexical complexity.

**Target Audience**:
- Natural Language Processing Researchers
- Text Simplification Researchers
- Computational Linguistics Researchers

**Tasks**:
- Lexical Complexity Prediction
- Complex Word Identification
- Support for Text Simplification evaluation

**Limitations**: Dataset limited to nouns as targets; multi-word expressions limited to two tokens and selected syntactic patterns (adjective-noun or noun-noun), limiting MWE variety. Annotator agreement (inter-annotator agreement) was not calculated. Data selection used predetermined frequency bands and three specific corpora only. The authors note subjectivity in annotations and that further analysis (e.g., compositional vs non-compositional MWEs, transferability between corpora) remains for future work.

## 💾 Data

**Source**: World English Bible translation (Christodouloupoulos and Steedman, 2015); English portion of Europarl (Koehn, 2005); CRAFT corpus biomedical articles (Bada et al., 2012). Targets comprise nouns and selected two-token multi-word expressions.

**Size**: 9,476 instances (sentences) in the final corpus, each annotated by a median of 7 annotators; pre-annotated selection of 10,800 instances prior to filtering.

**Format**: N/A

**Annotation**: Crowdsourced via the Figure Eight platform. Each target annotated on a 5-point Likert scale with descriptors (1: Very Easy, 2: Easy, 3: Neutral, 4: Difficult, 5: Very Difficult). Numerical labels were mapped to a 0–1 range using mapping 1→0, 2→0.25, 3→0.5, 4→0.75, 5→1. Requested 20 annotations per instance; post-hoc filtering removed annotators who failed platform quality checks or produced identical annotations; retained any data instance with at least 4 valid annotations. Annotators were selected from English-speaking countries (UK, USA, Australia) and Google Translate browser plug-in was disabled for annotators.

## 🔬 Methodology

**Methods**:
- Model-based evaluation (linear regression baseline)
- Automated metrics (evaluation on held-out test set)

**Metrics**:
- Mean Absolute Error (MAE)

**Calculation**: Mean Absolute Error calculated on a held-out test set consisting of 10% of the data, stratified across corpus type and complexity labels. Complexity labels are normalized to the 0–1 range using the mapping 1→0, 2→0.25, 3→0.5, 4→0.75, 5→1.

**Interpretation**: Complexity values range from 0 (very easy) to 1 (very difficult). Lower MAE indicates better prediction performance. The authors state that an MAE of approximately 0.0853 implies the ability to predict complexity with a good degree of accuracy.

**Baseline Results**: Best baseline: linear regression using hand-crafted features (word frequency, word length, syllable count) achieved Mean Absolute Error 0.0853 on the held-out test set.

**Validation**: Held-out test set (10% stratified by corpus and complexity labels). Annotation quality control via platform built-in checks, disabling Google Translate, post-hoc filtering of annotators who gave identical annotations, and requiring at least 4 valid annotations per instance. The authors did not compute inter-annotator agreement.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
