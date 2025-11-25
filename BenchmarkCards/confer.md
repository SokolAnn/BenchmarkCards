# CONFER

## 📊 Benchmark Details

**Name**: CONFER

**Overview**: CONFER is a dataset specifically designed to evaluate how Natural Language Inference (NLI) models process inference in conditional sentences, particularly focusing on presuppositional reasoning.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Conditional-NLI/CONFER)

## 🎯 Purpose and Intended Users

**Goal**: To assess the performance of NLI models in understanding presupposition projection in conditional sentences.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Semi-automatically generated using linguist-designed templates and GPT-3.5 for sentence formation.

**Size**: 18,000 sentence pairs

**Format**: JSON

**Annotation**: Manually annotated with NLI labels (Entailment, Contradiction, Neutral) by a linguist and double-annotated for reliability.

## 🔬 Methodology

**Methods**:
- Evaluation of NLI models through various prompting techniques

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated based on performance on the dataset comparing the output of NLI models.

**Interpretation**: Higher accuracy and F1 scores indicate better model understanding of presuppositional reasoning.

**Validation**: Performance evaluation compared across several models trained on different datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
