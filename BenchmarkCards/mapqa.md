# MapQA

## 📊 Benchmark Details

**Name**: MapQA

**Overview**: MapQA is a novel dataset that provides question-answer pairs and includes the geometries of geo-entities referenced in the questions, addressing the limitations of existing geospatial QA datasets. It consists of 3,154 QA pairs across nine geospatial question types requiring reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/knowledge-computing/MapQA-dataset)

## 🎯 Purpose and Intended Users

**Goal**: To advance research on geospatial question answering by providing a comprehensive dataset and evaluating methods tailored for the MapQA problem setting.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Geospatial Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: OpenStreetMap (OSM)

**Size**: 3,154 question-answer pairs

**Format**: CSV and JSON

**Annotation**: Heuristic labeling functions crafted by domain experts.

## 🔬 Methodology

**Methods**:
- Retrieval-based QA
- Text-to-SQL generation using Large Language Models

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the correctness of generated answers matching ground-truth data.

**Interpretation**: Higher accuracy indicates better performance in answering geospatial question types.

**Baseline Results**: Benchmarked against existing retrieval models and LLMs.

**Validation**: Evaluated using two regions (Southern California and Illinois) with performance compared across different question types.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
