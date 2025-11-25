# NATURAL INSTRUCTIONS

## 📊 Benchmark Details

**Name**: NATURAL INSTRUCTIONS

**Overview**: We introduce NATURAL INSTRUCTIONS, a dataset of 61 distinct tasks, their human-authored instructions, and 193k task instances (input-output pairs). The instructions are obtained from crowdsourcing instructions used to create existing NLP datasets and mapped to a unified schema.

**Data Type**: input-output pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PromptSource

**Resources**:
- [Resource](https://instructions.apps.allenai.org)

## 🎯 Purpose and Intended Users

**Goal**: To build models that generalize to new tasks by encoding and understanding crowdsourcing instructions.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Generation
- Answer Generation
- Incorrect Answer Generation
- Classification
- Minimal Text Modification

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced instructions from existing NLP datasets

**Size**: 193,000 instances

**Format**: JSON

**Annotation**: Collected through crowdsourcing platforms with a unified schema.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- ROUGE-L

**Calculation**: Metrics are calculated based on the generated outputs compared to the expected outputs.

**Interpretation**: Higher ROUGE-L scores indicate better performance of models in generating accurate task outputs.

**Baseline Results**: BART achieves higher performance when using full instructions compared to without instructions.

**Validation**: Results were validated against human-annotated performance.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
