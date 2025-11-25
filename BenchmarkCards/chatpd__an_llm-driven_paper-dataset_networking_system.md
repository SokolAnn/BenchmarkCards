# ChatPD: An LLM-driven Paper-Dataset Networking System

## 📊 Benchmark Details

**Name**: ChatPD: An LLM-driven Paper-Dataset Networking System

**Overview**: ChatPD is a system that utilizes Large Language Models to automate dataset information extraction from academic papers and construct a structured paper-dataset network, facilitating dataset discovery and recommendations.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PapersWithCode

**Resources**:
- [GitHub Repository](https://github.com/ChatPD-web/ChatPD)
- [Resource](https://chatpd-web.github.io/chatpd-web)

## 🎯 Purpose and Intended Users

**Goal**: To automate the extraction of dataset information from academic papers and construct a structured paper-dataset network for dataset discovery.

**Target Audience**:
- ML Researchers
- Data Scientists
- Academic Researchers

**Tasks**:
- Dataset Discovery
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Papers collected from arXiv (cs.AI) between 2018 to 2024

**Size**: 60,126 papers, 4,224 dataset entities, 137,004 paper-dataset usage records

**Format**: JSON

**Annotation**: Automated using Large Language Models

## 🔬 Methodology

**Methods**:
- Automated metrics
- Information Extraction

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on the accuracy of extracted dataset information and entity resolution.

**Interpretation**: Higher precision and recall indicate better ability to accurately extract dataset information.

**Validation**: Evaluation based on manually annotated dataset usage in academic papers

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-SA-4

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
