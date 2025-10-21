# Marking

## 📊 Benchmark Details

**Name**: Marking

**Overview**: Marking is a novel grading task that enhances automated grading systems by analyzing student responses and providing visual highlights of correct, incorrect, and irrelevant segments while detecting omissions from gold answers.

**Data Type**: student response annotations

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/luffycodes/marking)

## 🎯 Purpose and Intended Users

**Goal**: To provide a more detailed and informative assessment method for automated grading beyond traditional binary scoring.

**Target Audience**:
- Educational Researchers
- AI Researchers
- Educators

**Tasks**:
- Grading
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: BioMarking dataset curated by biology Subject Matter Experts

**Size**: 318 student responses

**Format**: N/A

**Annotation**: Annotated by Subject Matter Experts based on gold standard answers

## 🔬 Methodology

**Methods**:
- Transformer models (BERT, RoBERTa) fine-tuning

**Metrics**:
- F1 Score
- Accuracy

**Calculation**: F1 Score calculated for each category: entailment, contradiction, neutral, and omission using precision and recall.

**Interpretation**: Higher F1 scores indicate better model performance in accurately assessing student responses.

**Baseline Results**: RoBERTa-large achieved an F1 score of 0.762 in the Error-focused setting.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
