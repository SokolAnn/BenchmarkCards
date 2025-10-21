# Reading Between the Lines: A dataset and a study on why some texts are tougher than others

## 📊 Benchmark Details

**Name**: Reading Between the Lines: A dataset and a study on why some texts are tougher than others

**Overview**: This paper presents a dataset and an annotation scheme for understanding text difficulty specifically for audiences with intellectual disabilities, focusing on text simplification strategies.

**Data Type**: sentence pairs

**Domains**:
- Natural Language Processing
- Accessibility

**Languages**:
- English

**Similar Benchmarks**:
- ASSET
- WikiLarge

**Resources**:
- [GitHub Repository](https://github.com/Nouran-Khallaf/why-tough)

## 🎯 Purpose and Intended Users

**Goal**: To develop an extended taxonomy of translation strategies for text simplification, making information more accessible for individuals with intellectual disabilities.

**Target Audience**:
- Researchers in Text Simplification
- Developers of Accessibility Tools
- Educators

**Tasks**:
- Text Simplification
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Original text corpus sourced from Scottish public services, political manifestos, and newsletters.

**Size**: 76 parallel texts

**Format**: N/A

**Annotation**: Annotated with six predefined categories representing different text simplification strategies.

## 🔬 Methodology

**Methods**:
- Multiclass classification
- Fine-tuning transformer models
- Cross-validation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics calculated by comparing model predictions with annotated categories in the dataset.

**Interpretation**: Higher accuracy indicates better predictions of necessary simplification strategies.

**Baseline Results**: Baseline model accuracy of 24.5% and a weighted F1-score of 9.6%.

**Validation**: Stratified 5-Fold Cross-Validation used for model evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
