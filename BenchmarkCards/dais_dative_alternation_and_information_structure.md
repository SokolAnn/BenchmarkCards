# DAIS (Dative Alternation and Information Structure)

## 📊 Benchmark Details

**Name**: DAIS (Dative Alternation and Information Structure)

**Overview**: The DAIS dataset contains 50,136 human preference judgments for 5,000 sentence pairs, aimed at evaluating how well recent neural language models capture human preferences in the dative alternation.

**Data Type**: human preference judgments

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/taka-yamakoshi/neural_constructions)

## 🎯 Purpose and Intended Users

**Goal**: To provide a powerful benchmark for evaluating and understanding the sensitivity of language models to verb bias.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Human judgments collected from Amazon Mechanical Turk.

**Size**: 50,136 judgments

**Format**: N/A

**Annotation**: Judgments were collected using a continuous slider to indicate preference strength.

## 🔬 Methodology

**Methods**:
- Correlation analysis
- Neural network evaluation

**Metrics**:
- Correlation Coefficient

**Calculation**: Correlation between human judgments and model predictions.

**Interpretation**: Higher correlation indicates better model alignment with human preferences.

**Baseline Results**: Transformers, particularly GPT-2, show higher correlation with human judgments compared to LSTMs.

**Validation**: The dataset was validated by repeated splits and spearsman correlation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
