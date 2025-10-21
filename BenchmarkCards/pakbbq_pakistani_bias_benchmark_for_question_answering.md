# PakBBQ (Pakistani Bias Benchmark for Question Answering)

## 📊 Benchmark Details

**Name**: PakBBQ (Pakistani Bias Benchmark for Question Answering)

**Overview**: PakBBQ is a culturally and regionally adapted bias benchmark for evaluating large language models in the Pakistani context, comprising over 214 templates and 17180 question-answer pairs across 8 bias dimensions in English and Urdu.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Urdu

**Similar Benchmarks**:
- BBQ (Bias Benchmark for Question Answering)

**Resources**:
- [GitHub Repository](https://github.com/PakBBQ)

## 🎯 Purpose and Intended Users

**Goal**: To enable more rigorous auditing and mitigation of social biases in QA models deployed in Pakistan, and to provide a blueprint for culturally sensitive bias benchmarks in other underrepresented regions.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated data based on cultural adaptations and validations by native speakers.

**Size**: 17,180 question-answer pairs

**Format**: JSONL

**Annotation**: Annotated by native speakers representing diverse regional backgrounds.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Overall Accuracy
- Bias Score
- Context-Conditioned Accuracy
- Template-Type Accuracy

**Calculation**: Metrics are computed based on the number of correct responses across various contexts and bias conditions.

**Interpretation**: High accuracy indicates effective bias mitigation, while bias scores reflect the model's reliance on social stereotypes.

**Baseline Results**: N/A

**Validation**: Evaluation of multiple LLMs under zero-shot conditions for both English and Urdu.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Safety

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
