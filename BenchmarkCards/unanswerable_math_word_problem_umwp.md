# Unanswerable Math Word Problem (UMWP)

## 📊 Benchmark Details

**Name**: Unanswerable Math Word Problem (UMWP)

**Overview**: The UMWP dataset includes both answerable and unanswerable math word problems to investigate how GPT models respond to unanswerable scenarios and improve their abstention capabilities.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2410.13029)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of GPT models in handling unanswerable math word problems using various prompting strategies.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: The dataset includes a limited range of math word problems and does not explore the performance of models across different mathematical categories.

## 💾 Data

**Source**: The UMWP dataset, containing both answerable and unanswerable math word problems, was utilized for evaluation.

**Size**: 2,000 questions

**Format**: N/A

**Annotation**: The dataset consists of pairs of answerable and unanswerable questions where unanswerable variants were created by perturbing the original questions.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Confidence Balance
- Cautious Response Indicator
- False Resistance

**Calculation**: Accuracy is calculated as the proportion of correct predictions made by the model out of the total number of predictions.

**Interpretation**: A high score in confidence balance indicates better performance in accurately predicting answers while maintaining confidence.

**Validation**: The evaluation metrics assess the ability of models to abstain from answering unanswerable questions and correct the answerable ones.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
