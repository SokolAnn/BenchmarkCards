# FOFO (Format-Following Benchmark)

## 📊 Benchmark Details

**Name**: FOFO (Format-Following Benchmark)

**Overview**: FOFO is a benchmark for evaluating large language models' ability to follow complex, domain-specific formats, which is crucial for their application as AI agents. It tests LLMs on various real-world format requirements and instructions.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- AlpacaEval
- MT-Bench

**Resources**:
- [GitHub Repository](https://github.com/SalesforceAIResearch/FoFo)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the format-following capability of large language models in various domains.

**Target Audience**:
- AI Researchers
- ML Developers
- Domain-Specific AI Practitioners

**Tasks**:
- Format Following

**Limitations**: N/A

## 💾 Data

**Source**: Developed through an AI-Human collaborative method.

**Size**: 494 FORMAT-INSTRU

**Format**: JSON

**Annotation**: Generated and verified by human experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Evaluated as a binary classification problem with detailed explanations.

**Interpretation**: Higher accuracy indicates better format-following capability of models.

**Baseline Results**: N/A

**Validation**: Evaluated against both automated metrics and human judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
