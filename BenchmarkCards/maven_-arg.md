# MAVEN -ARG

## 📊 Benchmark Details

**Name**: MAVEN -ARG

**Overview**: MAVEN -ARG is an event argument extraction dataset that augments MAVEN datasets with event argument annotations, making it the first all-in-one dataset supporting event detection, event argument extraction (EAE), and event relation extraction.

**Data Type**: document-level event argument extraction

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MAVEN
- MAVEN -ERE

**Resources**:
- [GitHub Repository](https://github.com/THU-KEG/MAVEN-Argument)

## 🎯 Purpose and Intended Users

**Goal**: To complete the all-in-one event understanding dataset, supporting event detection, argument extraction, and event relation extraction.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Event Detection
- Event Argument Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Annotated from MAVEN datasets using a comprehensive event argument annotation schema.

**Size**: 98,591 events, 290,613 arguments

**Format**: JSON

**Annotation**: Human annotation by a team of experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Exact Match (EM)

**Calculation**: Evaluation is based on traditional metrics adapted for multi-answer question answering tasks.

**Interpretation**: Higher scores indicate better performance in correctly identifying event arguments.

**Baseline Results**: State-of-the-art EAE models achieve moderate performance, with F1 scores around 40%.

**Validation**: N/A

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

**Data Licensing**: The MAVEN dataset is released under the CC BY-SA 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
