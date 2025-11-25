# EXPRESS (EXperiences and PRocessed Emotions in Self-disclosure Stories)

## 📊 Benchmark Details

**Name**: EXPRESS (EXperiences and PRocessed Emotions in Self-disclosure Stories)

**Overview**: EXPRESS is a benchmark dataset curated from Reddit communities featuring 251 fine-grained, self-disclosed emotion labels, designed to evaluate the emotion recognition capabilities of language models.

**Data Type**: text (self-disclosed emotion labels)

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Computing-for-Social-Good-CSG/express-emotion-recognition.git)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models’ emotion recognition capabilities and facilitate potential emotion alignment.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Emotion Recognition

**Limitations**: N/A

## 💾 Data

**Source**: Reddit posts containing emotional experiences

**Size**: 33,679 examples

**Format**: N/A

**Annotation**: Self-disclosed emotions extracted from user posts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Lexical Accuracy
- Vector Accuracy
- Average Vector F-1 Score

**Calculation**: Metrics are calculated based on the predicted versus actual self-disclosed emotions.

**Interpretation**: Higher scores indicate better alignment of predicted emotions with self-disclosed emotions.

**Baseline Results**: N/A

**Validation**: Evaluation on various models using different prompting strategies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized to protect user identities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Self-disclosed emotions are used without external annotations.

**Compliance With Regulations**: Not Applicable
