# TextAge: A Curated and Diverse Text Dataset for Age Classification

## 📊 Benchmark Details

**Name**: TextAge: A Curated and Diverse Text Dataset for Age Classification

**Overview**: TextAge is a comprehensive and diverse dataset that maps a sentence to the age of the producer, age group of the producer, and whether the producer is underage (under 13). It collects both spoken and written data across various age groups.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2406.16890)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the TextAge dataset is to support age-related language pattern classification and enhance applications in online safety and content moderation.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Underage Detection
- Generational Classification

**Limitations**: The dataset may have limited data representation for older age groups, impacting performance on classification tasks.

## 💾 Data

**Source**: Sources include CHILDES, Meta Casual Conversations Dataset, Poki Poems-by-kids, JUSThink Dialogue and Actions Corpus, and transcripts from the TV show Survivor.

**Size**: 608,082 sentences

**Format**: CSV

**Annotation**: Data is manually annotated to label sentences according to the age of speakers and to classify age groups.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics are calculated based on classification results of models fine-tuned on the TextAge dataset.

**Interpretation**: Higher F1 scores indicate better classification performance in detecting age-related linguistic patterns.

**Baseline Results**: Naive Bayes classifier achieved an F1 score of 0.8798 as a baseline for comparison.

**Validation**: The dataset was validated through its application in underage detection and generational classification tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset includes diverse age group data, but performance may vary across groups due to representation.

**Potential Harm**: The dataset aims to prevent inappropriate content exposure for minors through improved age classification.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The data collection ensured anonymity by using public transcripts and age labels without personal identifiers.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
