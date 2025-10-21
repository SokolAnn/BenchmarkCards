# 4DBInfer (4D Benchmarking Toolbox for Graph-Centric Predictive Modeling on Relational DBs)

## 📊 Benchmark Details

**Name**: 4DBInfer (4D Benchmarking Toolbox for Graph-Centric Predictive Modeling on Relational DBs)

**Overview**: 4DBInfer is a toolbox that introduces a diverse collection of large-scale relational database benchmarks and a framework for evaluating predictive models on relational database data. It addresses the lack of suitable public benchmarks for training and evaluation purposes in predictive machine learning tasks applied to relational databases.

**Data Type**: tabular

**Domains**:
- Database Management
- Machine Learning

**Languages**:
- N/A

**Similar Benchmarks**:
- RDBench
- RelBench
- CRLR

**Resources**:
- [GitHub Repository](https://github.com/awslabs/multi-table-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmarking toolbox that allows for systematic evaluation and comparison of predictive models on relational databases.

**Target Audience**:
- ML Researchers
- Database Engineers
- Data Scientists

**Tasks**:
- Customer Retention Prediction
- Click-through-rate Prediction
- Product Purchase Prediction
- Conversion Rate Prediction
- User Churn Prediction
- Rating Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Various relational database datasets created for benchmarking purposes.

**Size**: Up to billions of rows across different RDB datasets.

**Format**: Tabular data across multiple inter-connected tables.

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Tabular model training
- Graph-based model training

**Metrics**:
- Accuracy
- AUC
- RMSE
- Mean Reciprocal Rank (MRR)

**Calculation**: Metrics are calculated based on standard machine learning evaluation methods applied to prediction results.

**Interpretation**: Higher AUC indicates better model performance in binary classification tasks, while lower RMSE indicates better performance in regression tasks.

**Baseline Results**: Results vary by dataset and task; specific baseline performances are detailed in experimental sections.

**Validation**: Cross-validation methods applied to ensure model robustness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
