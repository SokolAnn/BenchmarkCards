# PEEP (Prompts, Extracted Entities with Privacy)

## 📊 Benchmark Details

**Name**: PEEP (Prompts, Extracted Entities with Privacy)

**Overview**: PEEP is a multilingual dataset of 15,282 real user queries annotated to mark private content and paired with synthetic privacy profiles.

**Data Type**: user queries

**Domains**:
- Natural Language Processing

**Languages**:
- English
- French
- Chinese
- Russian
- Spanish
- Arabic
- German

**Resources**:
- [Resource](https://huggingface.co/datasets/guillemram97/PEEP)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective is to enhance user control over data sharing with external LLMs through privacy profiles.

**Target Audience**:
- ML Researchers
- Privacy Advocates
- Industry Practitioners

**Tasks**:
- Text Classification
- Question Answering
- Text Anonymization

**Limitations**: N/A

## 💾 Data

**Source**: Filtered real user queries from the Wildchat dataset.

**Size**: 15,282 examples

**Format**: N/A

**Annotation**: User queries are annotated with types of private information and paired with synthetic privacy profiles.

## 🔬 Methodology

**Methods**:
- Automated Evaluation
- LLM-based Evaluation

**Metrics**:
- Success Rate
- Leakage Rate

**Calculation**: Metrics calculated include success rate of responses and the leakage of protected information.

**Interpretation**: Higher success rates indicate better compliance with privacy profiles.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness
- Accuracy

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset was constructed with extensive anonymization procedures to protect user identity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
