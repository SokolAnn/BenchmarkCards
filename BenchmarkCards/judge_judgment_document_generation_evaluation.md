# JuDGE (Judgment Document Generation Evaluation)

## 📊 Benchmark Details

**Name**: JuDGE (Judgment Document Generation Evaluation)

**Overview**: JuDGE is a novel benchmark for evaluating the performance of judgment document generation in the Chinese legal system, designed to reflect real-world judicial reasoning and provide a comprehensive dataset of legal cases paired with their corresponding judgment documents.

**Data Type**: fact-judgment pairs

**Domains**:
- Legal

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/oneal2000/JuDGE)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of the benchmark is to provide a standardized evaluation framework for judgment document generation that mirrors real-world legal reasoning.

**Target Audience**:
- Legal researchers
- AI developers
- NLP researchers

**Tasks**:
- Judgment Document Generation

**Limitations**: N/A

## 💾 Data

**Source**: Judgment documents collected from the China Judgments Online platform, supplemented with statutes and past judgments from legal corpora.

**Size**: 2,505 fact-judgment pairs

**Format**: Structured JSON

**Annotation**: Expertly annotated by law students based on document quality and correctness.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Penalty Accuracy
- Convicting Accuracy
- Referencing Accuracy
- Document Similarity

**Calculation**: Metrics are calculated by comparing the quality of generated judgment documents against the ground truth across multiple dimensions.

**Interpretation**: Higher scores indicate better alignment with legal standards and accuracy in generated documents.

**Baseline Results**: N/A

**Validation**: Evaluated by comparing generated documents against a set of ground truth judgment documents.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All entries have undergone anonymization to eliminate sensitive information.

**Data Licensing**: Distributed under the MIT license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
