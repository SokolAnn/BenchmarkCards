# CEAMC (Chinese Essay Argument Mining Corpus)

## 📊 Benchmark Details

**Name**: CEAMC (Chinese Essay Argument Mining Corpus)

**Overview**: The CEAMC is a comprehensive multi-task dataset designed for understanding argumentation in Chinese high school students' essays, focusing on argument component detection, relation prediction, and automated essay grading.

**Data Type**: argumentative essays with annotated argument components and relations

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- Chinese

**Resources**:
- [Resource](https://arxiv.org/abs/2505.12028)

## 🎯 Purpose and Intended Users

**Goal**: To enhance understanding of argumentative structures and quality assessment in educational contexts through fine-grained argument annotations.

**Target Audience**:
- ML Researchers
- Educators
- Model Developers

**Tasks**:
- Argument Component Detection
- Relation Prediction
- Automated Essay Grading

**Limitations**: N/A

## 💾 Data

**Source**: Chinese high school examination essays, annotated with argument components and relations.

**Size**: 226 essays

**Format**: N/A

**Annotation**: Manual annotations by experts specializing in linguistics and education.

## 🔬 Methodology

**Methods**:
- Fine-tuning of language models
- Precision, Recall, F1 Score evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy

**Calculation**: Metrics calculated based on matches between predicted and gold standard argument components and relations.

**Interpretation**: Higher F1 scores indicate better model performance in predicting argument components and relations.

**Validation**: Cohen’s kappa used to measure Inter-Annotator Agreement for argument unit boundaries and relations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
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
