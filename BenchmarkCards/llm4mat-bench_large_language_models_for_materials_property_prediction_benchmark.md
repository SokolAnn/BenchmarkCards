# LLM4Mat-Bench (Large Language Models for Materials Property Prediction Benchmark)

## 📊 Benchmark Details

**Name**: LLM4Mat-Bench (Large Language Models for Materials Property Prediction Benchmark)

**Overview**: LLM4Mat-Bench is a benchmark dataset designed to evaluate large language models in predicting the properties of crystalline materials, containing approximately 1.9M crystal structures and 45 distinct properties sourced from 10 publicly available materials data sources.

**Data Type**: crystal structure-property pairs

**Domains**:
- Materials Science

**Languages**:
- English

**Similar Benchmarks**:
- MatBench
- TextEdge

**Resources**:
- [GitHub Repository](https://github.com/vertaix/LLM4Mat-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating the performance of large language models in predicting properties of crystalline materials.

**Target Audience**:
- Materials Scientists
- ML Researchers
- Data Scientists

**Tasks**:
- Property Prediction

**Limitations**: The study did not perform thorough hyperparameter searches due to computational constraints.

## 💾 Data

**Source**: 10 publicly available materials databases, including Materials Project and OQMD.

**Size**: 1,978,985 pairs

**Format**: CIF, Textual Descriptions

**Annotation**: Automatically generated text descriptions from crystal structures using Robocrystallographer, combined with properties sourced from databases.

## 🔬 Methodology

**Methods**:
- Regression tasks using MAD:MAE ratio
- Classification tasks using ROC AUC

**Metrics**:
- Mean Absolute Error (MAE)
- Area Under ROC Curve (AUC)

**Calculation**: MAD:MAE ratio is calculated for regression tasks, with a target ratio of at least 5.0 for a good model.

**Interpretation**: Higher MAD:MAE ratios indicate better performance, while AUC measures the model's ability to discriminate between classes in classification tasks.

**Baseline Results**: Baseline model CGCNN outperformed LLMs in several tasks, particularly in datasets with longer descriptions.

**Validation**: Results averaged over multiple runs for predictive models; evaluated separately for each dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
