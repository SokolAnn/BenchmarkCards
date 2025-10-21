# Turkish PET Dataset

## 📊 Benchmark Details

**Name**: Turkish PET Dataset

**Overview**: The Turkish PET dataset introduces potentially euphemistic terms in Turkish, providing euphemistic and non-euphemistic examples along with their contextual usages.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Turkish

**Resources**:
- [GitHub Repository](https://github.com/hasancanbiyik/Turkish_PET)

## 🎯 Purpose and Intended Users

**Goal**: To create a dataset for automatic euphemism detection in Turkish and evaluate several language models on this task.

**Target Audience**:
- ML Researchers
- Linguists
- NLP Practitioners

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Collected from published articles, social media polls, and annotated by native Turkish speakers.

**Size**: 6,115 examples

**Format**: N/A

**Annotation**: Annotated by native Turkish speakers with linguistic background.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Evaluation metrics are calculated based on the performance of transformer-based models.

**Interpretation**: Higher scores indicate better performance in detecting euphemistic terms.

**Baseline Results**: mBERT: 0.81 Accuracy, 0.80 F1 Score; XLM-RoBERTa: 0.82 Accuracy, 0.82 F1 Score; BERTurk: 0.84 Accuracy, 0.84 F1 Score; Electra: 0.86 Accuracy, 0.86 F1 Score.

**Validation**: Dataset split into training (80%), testing (10%), and validation (10%).

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
