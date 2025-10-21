# AutoG: Towards Automatic Graph Construction from Tabular Data

## 📊 Benchmark Details

**Name**: AutoG: Towards Automatic Graph Construction from Tabular Data

**Overview**: This work addresses the challenges in graph construction from tabular data by establishing a formal problem and proposing a set of datasets designed for evaluating graph construction methods and an automatic generation solution.

**Data Type**: structured tabular data

**Domains**:
- Natural Language Processing
- Healthcare
- E-commerce

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/amazon-science/Automatic-Table-to-Graph-Generation)

## 🎯 Purpose and Intended Users

**Goal**: To formalize the graph construction problem and evaluate different methods for automatic graph generation from tabular data.

**Target Audience**:
- Data Scientists
- ML Researchers
- Academics

**Tasks**:
- Graph Construction
- Data Transformation
- Task-Specific Graph Evaluation

**Limitations**: The automatic generation process currently addresses only moderately complex scenarios.

## 💾 Data

**Source**: Datasets extracted from Kaggle and existing datasets focused on tabular data.

**Size**: 8 datasets covering diverse graph construction challenges

**Format**: CSV, Parquet

**Annotation**: Datasets have been prepared to reflect real-world graph construction challenges without expert pre-processing.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- AUC

**Calculation**: Metrics are calculated based on the performance of graph construction methods applied to defined tasks.

**Interpretation**: Higher performance metrics indicate better graph construction effectiveness.

**Baseline Results**: AutoG outperforms existing heuristic-based graph construction methods and approaches human-level performance.

**Validation**: Extensive experiments conducted across multiple datasets to verify results.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
