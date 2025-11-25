# CatShift

## 📊 Benchmark Details

**Name**: CatShift

**Overview**: CatShift is a label-only dataset-inference framework that leverages catastrophic forgetting to detect whether a suspicious dataset was used in training a large language model.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

## 🎯 Purpose and Intended Users

**Goal**: To detect unauthorized usage of proprietary datasets using label-only outputs from large language models.

**Target Audience**:
- ML Researchers
- Data Owners

**Tasks**:
- Dataset Inference

**Limitations**: CatShift may struggle with datasets that substantially overlap with other data in the model’s training corpus.

## 💾 Data

**Source**: Experimental datasets created for evaluating membership in large language models.

**Size**: Various sizes depending on subsets analyzed.

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Hypothesis testing
- Statistical analysis

**Metrics**:
- AUC Score
- F1 Score

**Calculation**: Comparison of output shifts before and after fine-tuning using a statistical hypothesis test.

**Interpretation**: Lower p-values indicate a higher likelihood that the suspicious dataset was part of the training data.

**Baseline Results**: Baseline method achieved an AUC score of 0.707 and F1 score of 0.717; CatShift achieved an AUC score of 0.979 and F1 score of 0.863.

**Validation**: Statistical tests such as Kolmogorov-Smirnov are employed to validate results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Intellectual Property

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
