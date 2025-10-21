# ACCESS DENIED INC: The First Benchmark Environment for Sensitivity Awareness

## 📊 Benchmark Details

**Name**: ACCESS DENIED INC: The First Benchmark Environment for Sensitivity Awareness

**Overview**: ACCESS DENIED INC is a benchmarking environment developed to evaluate the sensitivity awareness of LLMs in adhering to predefined access rights rules concerning sensitive information in corporate data management.

**Data Type**: tabular

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/DrenFazlija/AccessDeniedInc)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how sensitivity-aware language models are in managing sensitive corporate data according to access rights rules.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: The benchmark currently uses synthetic data and does not account for real-world complexities.

## 💾 Data

**Source**: Generated mock-corporate dataset derived from the Adult dataset.

**Size**: 45,233 employees

**Format**: CSV

**Annotation**: Automatically generated questionnaire for assessing models' sensitivity awareness.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Semi-automated grading system

**Metrics**:
- Accuracy

**Calculation**: Grading based on model responses correctness with respect to predefined access rights rules.

**Interpretation**: Higher accuracy indicates better sensitivity awareness and compliance with company policy.

**Baseline Results**: Models showed varied performance with Grok-2 achieving higher sensitivity awareness.

**Validation**: Automated grading system allows for efficient evaluation of LLM responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: The dataset construction minimizes bias by randomizing names and features.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
