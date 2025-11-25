# ELF-Gym (Evaluating Large Language Models Generated Features for Tabular Prediction)

## 📊 Benchmark Details

**Name**: ELF-Gym (Evaluating Large Language Models Generated Features for Tabular Prediction)

**Overview**: ELF-Gym is a framework for evaluating LLM-generated features by curating a dataset that includes 251 expert-crafted features from top-performing teams in Kaggle competitions. It quantifies LLM-generated features' impact on model performance and compares semantic and functional similarities with human-engineered features.

**Data Type**: feature descriptions

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Lilyzhangyanlin/ELF-Gym)
- [Resource](https://doi.org/10.1145/3627673.3679153)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of the disparities between LLM-generated features and expert-crafted features in feature engineering tasks.

**Target Audience**:
- ML Researchers
- Data Scientists

**Tasks**:
- Feature Engineering

**Limitations**: N/A

## 💾 Data

**Source**: Curated from historical Kaggle competitions datasets

**Size**: 251 golden features

**Format**: N/A

**Annotation**: Manual extraction and validation of features using GPT-4o

## 🔬 Methodology

**Methods**:
- Quantitative evaluation
- Feature comparison metrics

**Metrics**:
- Recall

**Calculation**: Recall is calculated based on the proportion of golden features found in LLM-generated feature sets.

**Interpretation**: Higher recall indicates better alignment with expert-crafted features.

**Validation**: Initial experiments conducted with GPT-4o, Claude 3, LLaMA 3, and Mixtral

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
