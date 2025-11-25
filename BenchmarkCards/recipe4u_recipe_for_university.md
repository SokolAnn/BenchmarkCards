# RECIPE4U (RECIPE for University)

## 📊 Benchmark Details

**Name**: RECIPE4U (RECIPE for University)

**Overview**: RECIPE4U is a dataset sourced from a semester-long experiment with 212 college students in English as Foreign Language (EFL) writing courses, documenting dialogues between students and ChatGPT for essay revision.

**Data Type**: conversation logs, intention labels, self-rated satisfaction, essay edit histories

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English
- Korean

**Resources**:
- [Resource](https://zeunie.github.io/RECIPE4U/)

## 🎯 Purpose and Intended Users

**Goal**: To analyze students' interactions with ChatGPT in the context of EFL writing education and establish baseline models for intent detection and satisfaction estimation.

**Target Audience**:
- Educators
- Researches in NLP
- EFL instructors

**Tasks**:
- Intent Detection
- Satisfaction Estimation

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from interactions between 212 EFL students and ChatGPT during a semester-long course.

**Size**: 4,330 utterances

**Format**: N/A

**Annotation**: Annotated with 13 intention labels based on coding schemes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: Metrics were calculated based on user utterances and the responses of ChatGPT.

**Interpretation**: Interpretation of results based on the accuracy and engagement levels in student dialogues with ChatGPT.

**Baseline Results**: N/A

**Validation**: 5-fold cross-validation on intent detection and satisfaction estimation tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Hallucination

**Demographic Analysis**: Demographic factors included in analysis.

**Potential Harm**: ['Potential overreliance on ChatGPT for academic tasks']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Sensitive information related to student privacy will be filtered out through rule-based code and human inspection.

**Data Licensing**: Not Applicable

**Consent Procedures**: All studies conducted with institutional review board (IRB) approval.

**Compliance With Regulations**: Not Applicable
