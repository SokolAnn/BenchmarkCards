# MAFALDA (Multi-level Annotated Fallacy Dataset)

## 📊 Benchmark Details

**Name**: MAFALDA (Multi-level Annotated Fallacy Dataset)

**Overview**: MAFALDA is a benchmark for fallacy classification that merges and unites previous fallacy datasets, providing a taxonomy that aligns, refines, and unifies existing classifications of fallacies, along with a new annotation scheme allowing for subjective annotations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ChadiHelwe/MAFALDA)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for detecting and classifying fallacies in text, enabling evaluation of language models and human performances.

**Target Audience**:
- ML Researchers
- Language Model Developers
- NLP Practitioners

**Tasks**:
- Fallacy Detection
- Fallacy Classification

**Limitations**: The dataset may contain sensitive content such as racism and misogyny, and it is relatively small due to the time-intensive nature of the annotation process.

## 💾 Data

**Source**: The benchmark merges multiple existing fallacy datasets, including those from Sahai et al. (2021), Martino et al. (2019), Jin et al. (2022), and Goffredo et al. (2022).

**Size**: 9,745 texts (200 annotated texts)

**Format**: N/A

**Annotation**: Manual annotation by authors with explanations for each annotation, including the introduction of a new disjunctive annotation scheme.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model performance assessment

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Precision and recall are calculated based on the matches between annotations and predictions.

**Interpretation**: Higher F1 scores indicate better performance in detecting and classifying fallacies.

**Baseline Results**: Performance results across several models with human baseline comparisons provided in the study.

**Validation**: All annotations were discussed among authors to reach consensus or provide alternative annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Transparency
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-SA

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
