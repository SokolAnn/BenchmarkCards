# L2M3 (Large Language Model based Material Miner)

## 📊 Benchmark Details

**Name**: L2M3 (Large Language Model based Material Miner)

**Overview**: This research presents L2M3, a novel data mining system that automates the extraction and organization of Metal-Organic Framework (MOF) data from over 40,000 research articles into a structured format, enabling improved machine learning predictions in materials science.

**Data Type**: structured dataset of properties

**Domains**:
- Materials Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/ccdc-opensource/csd-python-api-scripts)
- [GitHub Repository](https://github.com/langchain-ai/langchain)
- [GitHub Repository](https://github.com/openai/tiktoken)

## 🎯 Purpose and Intended Users

**Goal**: To develop a systematic approach for extracting and organizing Metal-Organic Framework data to enhance accuracy in machine learning studies.

**Target Audience**:
- Materials Scientists
- Researchers in Machine Learning
- Data Scientists

**Tasks**:
- Data Extraction
- Data Organization

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from 41,681 journals on Metal-Organic Frameworks, integrating with the Cambridge Structural Database.

**Size**: 39,476 research articles

**Format**: JSON

**Annotation**: Data extraction conducted using advanced Large Language Models with human review.

## 🔬 Methodology

**Methods**:
- Automated data extraction using Large Language Models
- Data integration with Cambridge Structural Database

**Metrics**:
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated based on evaluation of extracted information from sampled papers.

**Interpretation**: Higher F1 scores indicate better performance in accurate data extraction and organization.

**Baseline Results**: Outperformed previous studies with F1 scores higher than 0.95 across multiple categories.

**Validation**: Validation performed by randomly selecting 150 papers to assess extraction accuracy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Data obtained with explicit approval from publishers to comply with their usage policies.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
