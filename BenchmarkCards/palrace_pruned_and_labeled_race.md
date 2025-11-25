# PALRACE (Pruned And Labeled RACE)

## 📊 Benchmark Details

**Name**: PALRACE (Pruned And Labeled RACE)

**Overview**: PALRACE is a new Machine Reading Comprehension (MRC) dataset with human labeled rationales for 800 passages selected from the RACE dataset. It aims to support supervised learning of rationales to improve the interpretability and robustness of models.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RACE

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To investigate whether human rationales can improve current models and facilitate supervised learning of human rationales.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Machine Reading Comprehension

**Limitations**: N/A

## 💾 Data

**Source**: The reading comprehension passages and questions were selected from the test set of the large-scale RACE dataset.

**Size**: 800 passages

**Format**: N/A

**Annotation**: Each passage was read by at least 26 human readers, who labeled their rationales to answer the question.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: The models were fine-tuned on the RACE dataset to maximize the log-score of the correct option.

**Interpretation**: Models with access to human rationales are more robust and less sensitive to how they are fine-tuned.

**Baseline Results**: RoBERTa-large outperforms human readers in all 6 types of questions.

**Validation**: 10-fold cross validation was used to generate training, development, and test sets.

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
