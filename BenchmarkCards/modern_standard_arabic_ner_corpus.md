# Modern Standard Arabic NER corpus

## 📊 Benchmark Details

**Name**: Modern Standard Arabic NER corpus

**Overview**: This work provides a new structured dataset for Named Entity Recognition (NER) in the Arabic language covering seven domains (Geography, History, Medical, Sport, Technology, News, and Cooking) using the BIOES format; the dataset consists of more than thirty-six thousand records. The paper also proposes LSTM and GRU models for Arabic NER and reports approximately 80% precision on validation and test sets.

**Data Type**: Token-level labeled text (word, tag pairs)

**Domains**:
- Natural Language Processing
- Geography
- History
- Medical
- Sport
- Technology
- News
- Cooking

**Languages**:
- Arabic
- Modern Standard Arabic

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: Provide a new structured dataset for Arabic named entity recognition covering seven fields and evaluate LSTM and GRU models on it.

**Tasks**:
- Named Entity Recognition
- Text Classification
- Sentence Classification

**Limitations**: N/A

## 💾 Data

**Source**: New dataset created by the authors, organized into training, validation, and test sets; dataset covers seven fields (Geography, History, Medical, Sport, Technology, News, Cooking) and is stored as multiple Excel files.

**Size**: 143 files; 2,104 sentences; 36,380 words (Training: 120 files, 1,731 sentences, 31,586 words; Validation: 15 files, 218 sentences, 3,107 words; Test: 8 files, 155 sentences, 1,687 words)

**Format**: Excel files (each with four columns: file_name, sentence, word, tag)

**Annotation**: Annotated using BIOES format; nine entity categories: Person (PER), Location (LOC), Geopolitical (GPE), Time (TIM), Profession (PRO), Organization (ORG), Disease (DIS), Geography (GEO), Miscellaneous (MISC).

## 🔬 Methodology

**Methods**:
- Model evaluation using trained LSTM and GRU models
- Automated metrics (precision) using held-out validation and test sets

**Metrics**:
- Precision

**Calculation**: The accuracy measure used in this work is precision, which equals dividing the accurately predicted labels by the total number of labels in the sentence.

**Interpretation**: Results around approximately 80% precision are described as relatively good; authors state models can generalize and successfully detect named entities in validation and test sets. Increasing iterations did not necessarily improve results beyond a reached threshold.

**Baseline Results**: Table 3 results: 500 iterations - LSTM validation 81.86%, test 80.24%; 500 iterations - GRU validation 78.86%, test 77.78%. 1000 iterations - LSTM validation 79.88%, test 80.06%; 1000 iterations - GRU validation 76.26%, test 75.38%. Number of trainable parameters: LSTM 608,937; GRU 603,887.

**Validation**: Dataset split into training (120 files), validation (15 files), and test (8 files); results reported on validation and test sets.

## ⚠️ Targeted Risks

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
