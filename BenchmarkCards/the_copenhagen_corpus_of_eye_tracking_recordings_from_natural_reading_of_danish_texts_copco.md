# The Copenhagen Corpus of Eye Tracking Recordings from Natural Reading of Danish Texts (CopCo)

## 📊 Benchmark Details

**Name**: The Copenhagen Corpus of Eye Tracking Recordings from Natural Reading of Danish Texts (CopCo)

**Overview**: CopCo is the first Danish eye tracking corpus with contextualized, running text and self-paced reading. The first release includes eye tracking data from 22 participants and contains 1,832 sentences with 34,897 tokens of Danish text extracted from a collection of speech manuscripts. The corpus is intended to make eye movement recordings from natural reading available for psycholinguistic research and natural language processing purposes.

**Data Type**: Time-series eye-tracking recordings paired with Danish running text (character-level and word-level eye-tracking features)

**Domains**:
- Natural Language Processing
- Psycholinguistics
- Reading Research

**Languages**:
- Danish

**Similar Benchmarks**:
- GECO corpus
- ZuCo
- Provo Corpus
- Multilingual Eye Movement Corpus (MECO)
- Dundee corpus

**Resources**:
- [Resource](https://osf.io/ud8s5/)
- [GitHub Repository](https://github.com/norahollenstein/copco-processing)

## 🎯 Purpose and Intended Users

**Goal**: Provide a Danish eye-tracking corpus of natural, contextualized reading to enable psycholinguistic analyses and to support NLP applications that leverage eye movement data.

**Target Audience**:
- ML Researchers
- Natural Language Processing Researchers
- Psycholinguistics Researchers
- Reading Research Community

**Tasks**:
- Part-of-Speech Tagging
- Named Entity Recognition
- Syntactic Analysis
- Semantic Analysis
- Eye Movement Prediction
- Reading Behavior Analysis

**Limitations**: First release contains recordings from 22 participants and 20 speeches (1,832 sentences, 34,897 tokens). Reading materials are limited to selected Danish speech manuscripts from 2010–2019; not all manuscripts used canonical punctuation and this may affect readability scores. The corpus is a growing resource and will be extended in future releases.

## 💾 Data

**Source**: Danish speech manuscripts from https://dansketaler.dk/; eye-tracking recordings collected with an EyeLink 1000 Plus eye tracker; experiment materials and texts manually subsampled and proofread by a native Danish speaker.

**Size**: 1,832 sentences; 34,897 tokens; eye-tracking recordings from 22 participants (first release); 20 speeches sampled from the Danske Taler archive; 68 comprehension questions in total.

**Format**: Provided versions: raw eye-tracking recordings; character-level fixation information; character-level saccade information; word-level eye-tracking feature files. (Processing code available: https://github.com/norahollenstein/copco-processing)

**Annotation**: Eye-tracking features automatically extracted using custom Python code (character- and word-level feature extraction). Comprehension questions (yes/no) collected during reading (68 questions total). Texts proofread by a native Danish speaker.

## 🔬 Methodology

**Methods**:
- Automated eye-tracking feature extraction (character-level to word-level mapping)
- Statistical validation analyses (e.g., correlations, feature range comparisons)

**Metrics**:
- Accuracy (reading comprehension accuracy)
- Spearman's rank correlation coefficient
- Mean
- Median
- Standard deviation

**Calculation**: Reading comprehension accuracy: proportion of correctly answered reading comprehension questions. Correlations reported using Spearman's rank correlation coefficient. Feature summaries reported using means, medians, and standard deviations as shown in the validation analyses.

**Interpretation**: Higher reading comprehension accuracy indicates adequate participant comprehension (mean accuracy reported as 82%). Extracted eye-tracking feature ranges are interpreted by comparison to similar corpora and are reported as 'in line with related research'.

**Validation**: Data quality assessed via analyses of reading comprehension scores, effects of word length and word frequency on skipping and fixation, landing position analyses at character level, and comparison of extracted word-level feature ranges to existing corpora (e.g., GECO and ZuCo). Fixations shorter than 100 ms were excluded from analysis.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All participants gave written consent to their participation and the reuse of the data for research purposes. Study was approved by the Research Ethics Committee at the Faculty of Humanities of the University of Copenhagen.

**Data Licensing**: Not Applicable

**Consent Procedures**: Written consent obtained from all participants for participation and reuse of the data for research purposes.

**Compliance With Regulations**: Study approved by the Research Ethics Committee at the Faculty of Humanities of the University of Copenhagen.
