# LLM Dataset Inference

## 📊 Benchmark Details

**Name**: LLM Dataset Inference

**Overview**: This paper introduces a new dataset inference method designed to accurately identify the datasets used to train large language models, addressing concerns about copyright and training data attribution.

**Data Type**: text sequences

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Membership Inference
- Dataset Inference

**Resources**:
- [GitHub Repository](https://github.com/pratyushmaini/llm_dataset_inference/)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to provide a framework for identifying if specific datasets were used in the training of large language models.

**Target Audience**:
- ML Researchers
- AI Ethics Professionals
- Legal Practitioners

**Tasks**:
- Dataset Attribution

**Limitations**: The method requires that the training and validation sets must be IID, and the validation set must remain completely private.

## 💾 Data

**Source**: Pythia models trained on the Pile dataset.

**Size**: 20 subsets of PILE dataset

**Format**: text

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Membership Inference Attacks
- Statistical Testing
- Linear Regression

**Metrics**:
- p-values

**Calculation**: Use statistical tests on membership scores derived from multiple MIAs to determine significance.

**Interpretation**: Lower p-values indicate a stronger likelihood that the dataset was used in training the model.

**Validation**: Validated by comparing results across multiple subsets of the Pile dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Addresses privacy concerns related to Copyright data inclusion.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
