# JobHop

## 📊 Benchmark Details

**Name**: JobHop

**Overview**: JobHop is a large-scale dataset derived from anonymized resumes, offering insights into real-world occupational transitions, including the impact of career breaks on job stability and mobility within the labor market.

**Data Type**: structured career information, career trajectories

**Domains**:
- Natural Language Processing
- Labor Market Analysis

**Languages**:
- Dutch
- English
- French

**Resources**:
- [Resource](https://huggingface.co/datasets/aida-ugent/JobHop)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive dataset for analyzing labor market dynamics and predicting career paths based on real-world career trajectories.

**Target Audience**:
- Researchers
- Policymakers
- Industry Practitioners

**Tasks**:
- Labor Market Analysis
- Career Path Prediction

**Limitations**: N/A

## 💾 Data

**Source**: Anonymized resumes provided by VDAB, the public employment service in Flanders, Belgium.

**Size**: 391,194 resumes

**Format**: JSON

**Annotation**: Structured information extracted using Large Language Models and mapped to standardized ESCO occupation codes.

## 🔬 Methodology

**Methods**:
- Information extraction
- Multi-label classification

**Metrics**:
- Accuracy of career extraction
- Correct mapping to ESCO codes

**Calculation**: Calculated based on similarity scores for extracted career information.

**Interpretation**: High accuracy in mapping job experiences to ESCO codes and extracting relevant career details indicates effective modeling.

**Baseline Results**: N/A

**Validation**: Evaluated using hand-annotated datasets for accuracy testing.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset is anonymized to protect individual privacy, with no personally identifiable information included.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
