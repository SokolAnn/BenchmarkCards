# RoNLI (Romanian Natural Language Inference)

## 📊 Benchmark Details

**Name**: RoNLI (Romanian Natural Language Inference)

**Overview**: RoNLI is the first Romanian NLI corpus comprising 58K training sentence pairs and 6K validation and test sentence pairs, focusing on the task of recognizing the entailment relationship in sentence pairs.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Romanian

**Resources**:
- [GitHub Repository](https://github.com/Eduard6421/RONLI)

## 🎯 Purpose and Intended Users

**Goal**: To provide a publicly available corpus for Romanian natural language inference to stimulate research in low-resource NLI tasks.

**Target Audience**:
- ML Researchers
- NLP Practitioners

**Tasks**:
- Natural Language Inference

**Limitations**: The dataset is limited by the number of samples with manual labels due to the labor-intensive annotation process.

## 💾 Data

**Source**: Romanian Wikipedia

**Size**: 64,000 sentence pairs

**Format**: CSV

**Annotation**: Training pairs obtained via distant supervision; validation and test pairs manually annotated.

## 🔬 Methodology

**Methods**:
- Grid search for hyperparameter tuning
- Machine learning models including word embeddings and transformer-based models

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics were calculated based on predictions compared to manually labeled test set.

**Interpretation**: Higher precision and F1 scores indicate better performance in recognizing entailment relationships.

**Baseline Results**: The best F1 Score achieved was approximately 73% micro F1 and 56% macro F1.

**Validation**: Validation performed through human annotators ensuring quality labeling.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The dataset does not include a demographic breakdown.

**Potential Harm**: Potential labeling noise due to automatic annotation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY-NC-SA 4.0

**Consent Procedures**: Annotation was voluntary, with students agreeing to participate for bonus points.

**Compliance With Regulations**: Not Applicable
