# CEAC (Cause-Emotion-Action Corpus)

## 📊 Benchmark Details

**Name**: CEAC (Cause-Emotion-Action Corpus)

**Overview**: CEAC (Cause-Emotion-Action Corpus), which manually annotates not only emotion, but also cause events and action events. Based on CEAC, we introduce two tasks: emotion causality (extract a triple (cause, emotion, action) as CEA relation) and emotion inference (infer the probable emotion given a tuple of cause and action events).

**Data Type**: text (news passages with annotated cause, emotion, and action events)

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Similar Benchmarks**:
- Academia Sinica Balanced Chinese Corpus
- NTCIR-13 ECA (Emotion Cause Analysis) task
- Event2Mind

**Resources**:
- [Resource](http://www.keenage.com)
- [Resource](http://ir.dlut.edu.cn/EmotionOntologyDownload)
- [Resource](http://academiasinicanlplab.github.io/)
- [Resource](https://dcc.blcu.edu.cn)
- [Resource](https://arxiv.org/abs/1903.06901)

## 🎯 Purpose and Intended Users

**Goal**: To define emotion action and integrate it into emotion causality (Cause-Emotion-Action chains), to define and investigate two tasks (emotion causality and emotion inference), and to manually label and release a corpus (CEAC) to support these tasks.

**Tasks**:
- Cause-Emotion-Action Relation Extraction (Emotion Causality)
- Emotion Inference

**Limitations**: Imbalance distribution of emotion cause and emotion action limits analysis; dataset currently contains 10,603 annotated sentences which the authors state may be insufficient and plan to expand in future.

## 💾 Data

**Source**: National Language Resources Dynamic Circulation Corpus (DCC) 2005-2015 (news text passages extracted by emotion keywords, with three preceding and three following clauses kept as context).

**Size**: 10,603 samples and 15,892 events

**Format**: Annotated in W3C Emotion Markup Language (EML) XML format; raw data are news text passages (clauses preserved as context).

**Annotation**: Manual annotation by trained annotators: two annotators independently annotate cause(s), action(s) and experiencer for each emotion keyword; a third annotator serves as arbitrator for inconsistencies; cause/action tags include attributes (id, type).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (Bi-LSTM + CRF for Cause-Emotion-Action relation extraction)
- Model-based evaluation (LSTM classifier for Emotion Inference)

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Precision, Recall and F1 are computed per class and overall as reported in result tables.

**Interpretation**: Higher Precision/Recall/F1 indicates better extraction/inference. Baseline performance is relatively low, indicating the tasks are difficult and there is substantial room for improvement (as stated by the authors).

**Baseline Results**: Cause-Emotion-Action Extraction (Bi-LSTM+CRF) - ALL (cause) Precision 0.55 Recall 0.53 F1 0.54; ALL (action) Precision 0.48 Recall 0.44 F1 0.46. Emotion Inference (LSTM) - ALL Precision 0.55 Recall 0.55 F1 0.55 (results reported per emotion category in paper tables).

**Validation**: Train/test split 4:1 for both tasks; inter-annotator agreement Kappa at clause level = 0.8201; inconsistent annotations adjudicated by a third annotator.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
