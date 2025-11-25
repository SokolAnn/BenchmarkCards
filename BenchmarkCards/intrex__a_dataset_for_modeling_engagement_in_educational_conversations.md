# IntrEx: A Dataset for Modeling Engagement in Educational Conversations

## 📊 Benchmark Details

**Name**: IntrEx: A Dataset for Modeling Engagement in Educational Conversations

**Overview**: IntrEx is the first large dataset annotated for interestingness and expected interestingness in teacher-student interactions, capturing how engagement evolves across dialogue sequences.

**Data Type**: conversation annotations

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/collections/XingweiT/intrex-68a8f2c97688157066860ae2)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset that models engagement in educational dialogues for second-language learners.

**Target Audience**:
- ML Researchers
- Educators
- Curriculum Developers

**Tasks**:
- Engagement Modeling
- Conversational Analysis

**Limitations**: Annotator Proficiency Bias may underrepresent lower-proficiency learners' perspectives.

## 💾 Data

**Source**: Teacher-Student Chatroom Corpus (TSCC)

**Size**: 5,801 sequences

**Format**: CSV

**Annotation**: Comparison-based ratings by over 100 second-language learners.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Agreement rates (AC2)
- Interestingness scores

**Calculation**: Interestingness and expected interestingness scores are computed based on the annotated ratings following a comparison-based approach.

**Interpretation**: Higher scores indicate greater engagement and interest observed in the dialogues.

**Baseline Results**: Small instruction-tuned models outperformed larger models like GPT-4 in predicting interest ratings.

**Validation**: Annotators provided ratings for different conversations to enhance reliability and inter-annotator agreement.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The annotator backgrounds included a range of ages and multiple first languages, primarily from Greek, Polish, and Portuguese speakers.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data has been anonymized before public release, and participants were informed about the anonymization procedures.

**Data Licensing**: Not Applicable

**Consent Procedures**: Participants provided informed consent prior to participation.

**Compliance With Regulations**: Ethics approval obtained from the institutional review board.
