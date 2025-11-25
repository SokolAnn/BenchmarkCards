# Information Updation

## 📊 Benchmark Details

**Name**: Information Updation

**Overview**: The Information Updation dataset simulates the task of updating outdated Wikipedia tables with the latest versions across multiple languages, specifically focusing on enhancing coherence and accuracy in information synchronization.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- Spanish
- French
- German
- Arabic
- Hindi
- Korean
- Russian
- Afrikaans
- Cebuano
- Swedish
- Dutch
- Turkish
- Chinese

**Similar Benchmarks**:
- INFOSYNC

**Resources**:
- [Resource](https://zero-shot-llm-infosync.github.io/zero-shot-llm-infosync/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the Information Updation dataset is to improve the synchronization of information across multilingual Wikipedia tables and enhance the accuracy and coherence of updates.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Information Synchronization

**Limitations**: N/A

## 💾 Data

**Source**: Wikipedia tables consisting of outdated and updated versions sampled over time.

**Size**: 950 annotated instances

**Format**: JSON

**Annotation**: Manually annotated by human annotators ensuring accuracy.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Multi-voting scheme

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on the alignment and quality of updates produced by the model involved in the Information Updation task.

**Interpretation**: A higher F1 Score indicates better model performance in accurately updating the information, with close alignment to the ground truth tables.

**Validation**: The benchmark is validated through human annotations and comparative evaluations between models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
