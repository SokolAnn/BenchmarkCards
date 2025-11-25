# MIDAS (Motivational Interviewing Dataset in Spanish)

## 📊 Benchmark Details

**Name**: MIDAS (Motivational Interviewing Dataset in Spanish)

**Overview**: This paper introduces MIDAS, a counseling dataset created from public video sources that contains expert annotations for counseling reflections and questions, aiming to explore language-based differences in counselor behavior in English and Spanish.

**Data Type**: counseling conversations

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- Spanish

**Similar Benchmarks**:
- GlobHCD
- BiMISC

**Resources**:
- [GitHub Repository](https://github.com/MichiganNLP/MIDAS)

## 🎯 Purpose and Intended Users

**Goal**: To provide a resource for NLP researchers working on mental health applications and explore counseling dynamics in different languages.

**Target Audience**:
- ML Researchers
- Mental Health Practitioners

**Tasks**:
- Behavior Classification

**Limitations**: The collected transcripts are sourced from online videos created for educational purposes and may be scripted.

## 💾 Data

**Source**: Public video sources from YouTube involving motivational interviewing.

**Size**: 74 conversations

**Format**: Transcriptions

**Annotation**: Annotated by professional counselors with MI experience.

## 🔬 Methodology

**Methods**:
- Classification experiments

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Accuracy and F1 Score calculated based on the classifier predictions.

**Interpretation**: Higher accuracy and F1 scores indicate better classification of counselor behaviors.

**Validation**: Interannotator reliability was evaluated achieving a 92% intraclass correlation for reflections and questions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
