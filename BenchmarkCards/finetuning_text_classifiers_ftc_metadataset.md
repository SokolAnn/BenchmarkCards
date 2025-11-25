# Finetuning Text Classifiers (FTC) metadataset

## 📊 Benchmark Details

**Name**: Finetuning Text Classifiers (FTC) metadataset

**Overview**: The FTC metadataset contains predictions from five large finetuned models across six datasets for text classification tasks, and it evaluates the effectiveness of various ensembling strategies.

**Data Type**: predictions from text classification models

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/sebastianpinedaar/finetuning_text_classifiers)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the efficacy of ensembling strategies for finetuned text classifiers on various datasets.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Predictions from five large finetuned models on six datasets: IMDB, Tweet, News, DBpedia, SST-2, SetFit.

**Size**: 1,134 evaluated configurations, around 3,800 GPU hours of computation.

**Format**: N/A

**Annotation**: Predictions obtained by finetuning models on training data and evaluating on validation and test splits.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Negative Log-Likelihood (NLL)
- Classification error

**Calculation**: Metrics calculated from predictions on validation and test data across different ensembling strategies.

**Interpretation**: Lower NLL and classification error indicate better model performance.

**Baseline Results**: N/A

**Validation**: Best configurations for each dataset were determined via grid search on validation data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Robustness**

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
