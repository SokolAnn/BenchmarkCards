# SearchInstruct

## 📊 Benchmark Details

**Name**: SearchInstruct

**Overview**: SearchInstruct is a novel framework for constructing high-quality instruction datasets for supervised fine-tuning (SFT) by combining targeted document retrieval with grounded answer generation.

**Data Type**: instruction-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- Persian
- English

**Resources**:
- [GitHub Repository](https://github.com/mostafaamiri/SearchInstruct)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of SearchInstruct is to enhance the generation of supervised fine-tuning datasets for large language models, particularly in specialized domains.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from domain-specific queries and external documents retrieved from the web or APIs.

**Size**: 8,932 instances in culinary and 7,560 instances in tourism domains

**Format**: N/A

**Annotation**: Automatically generated through query expansion and dynamic document retrieval.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Instruction-Following Accuracy

**Calculation**: Metrics are calculated based on the correctness of the model outputs in response to human-generated instructions and queries.

**Interpretation**: Higher scores indicate better performance in following user instructions accurately within specialized domains.

**Baseline Results**: N/A

**Validation**: Empirical evaluation through human annotators and comparative assessments of model performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Risk of bias propagation from web-sourced documents.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
