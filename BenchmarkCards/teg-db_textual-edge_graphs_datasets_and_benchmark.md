# TEG-DB (Textual-Edge Graphs Datasets and Benchmark)

## 📊 Benchmark Details

**Name**: TEG-DB (Textual-Edge Graphs Datasets and Benchmark)

**Overview**: TEG-DB is a pioneering initiative offering a diverse collection of benchmark graph datasets with rich textual descriptions on both nodes and edges to enhance graph analysis and provide deeper insights into complex real-world networks.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Zhuofeng-Li/TEG-Benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To mitigate the challenges in the existing TAG datasets and foster collaboration in the research community for TEG exploration.

**Target Audience**:
- ML Researchers
- Data Scientists
- Graph Researchers

**Tasks**:
- Node Classification
- Link Prediction

**Limitations**: The lack of comprehensive evaluation resources may demand significant computational requirements.

## 💾 Data

**Source**: Nine datasets from various domains covering book recommendation, e-commerce, citation networks, and social networks.

**Size**: N/A

**Format**: JSON, .pt

**Annotation**: Text attribute preprocessing including filtering, truncation, and selection of relevant textual attributes.

## 🔬 Methodology

**Methods**:
- PLM-based
- GNN-based
- LLM as Predictor

**Metrics**:
- Area Under ROC Curve (AUC)
- F1 Score
- Accuracy

**Calculation**: Metrics calculated using standard evaluation processes across varied datasets in the TEG-DB.

**Interpretation**: Results signify performance in link prediction and node classification tasks, with improvements noted when using rich edge text.

**Baseline Results**: State-of-the-art models across datasets demonstrated varied performance enhancements in node classification and link prediction.

**Validation**: Comprehensive analyses conducted using multiple models across diverse datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Usage
- Model Performance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Potential significant computational resource demands could limit access for smaller organizations.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
