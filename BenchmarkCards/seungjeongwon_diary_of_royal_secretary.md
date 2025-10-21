# SeungJeongWon (Diary of Royal secretary)

## 📊 Benchmark Details

**Name**: SeungJeongWon (Diary of Royal secretary)

**Overview**: This paper introduces Korean historical corpus (Diary of Royal secretary which is named SeungJeongWon) recorded over several centuries and recently added with named entity information as well as phrase markers which historians carefully annotated.

**Data Type**: text (paragraph-level historical text with named entity annotations and punctuation/phrase markers)

**Domains**:
- Natural Language Processing
- Historical Research

**Languages**:
- Classical Chinese
- Korean

**Resources**:
- [Resource](https://sjw.history.go.kr)
- [Resource](https://huggingface.co/Nara-Lab/History_NER)

## 🎯 Purpose and Intended Users

**Goal**: Introduce the Seungjeongwon historical corpus annotated with named entities and punctuation/phrase markers, and evaluate NER transfer learning across time using fine-tuned language models and comparative experiments.

**Target Audience**:
- Historians
- Researchers

**Tasks**:
- Named Entity Recognition

**Limitations**: Study uses only two kings' diaries (Injo and Soonjong) from the Seungjeongwon corpus; complete translation of the full corpus remains unfinished; scarcity of annotated historical corpora is acknowledged.

## 💾 Data

**Source**: Seungjeongwon Diary corpus (Diary Records of Royal Secretariat of Joseon Dynasty) provided by National Institute of Korean History; digitized and annotated by historians (annotations following national guidelines).

**Size**: 1,896,173 paragraphs; 242.5 million characters; 3,243 books; 13,666 character types

**Format**: Unicode text (digitized); prepared as two variants: with punctuation markers and without punctuation markers

**Annotation**: Manual annotation by historians following national guidelines: named entities labeled (name, location, book title) and phrase/punctuation markers; additional historian notes include omission notes, comparative notes, and linking notes.

## 🔬 Methodology

**Methods**:
- Automated metrics (Micro F1, Accuracy, Quality scores via Flair)
- Model fine-tuning and transfer learning experiments across time-based paths
- Statistical significance testing (Welch's t-test on Flair quality scores)

**Metrics**:
- Micro F1 score
- Accuracy
- Quality score (Flair)

**Calculation**: Micro F1 used as the primary metric; accuracy and quality scores provided by the Flair library for each entity; statistical significance assessed using Welch's t-test on Flair quality numerical evaluation scores.

**Interpretation**: Higher Micro F1 and Flair quality scores indicate better NER performance; p < 0.005 in Welch's t-test is reported as statistically significant in the paper's comparisons.

**Baseline Results**: Authors supply the best History NER model, which is Bert Path A at https://huggingface.co/Nara-Lab/History_NER. Table 3 reports mean quality scores for hypothesis tests (e.g., H1 A:0.8338, D:0.9055; H3 B:0.5141, E:0.4182).

**Validation**: Validation via Welch's t-test on all quality numerical evaluation scores provided by Flair; experiments validated across six transfer-learning paths comparing past/future and punctuated/unpunctuated variants.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Data contamination, Unrepresentative data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
