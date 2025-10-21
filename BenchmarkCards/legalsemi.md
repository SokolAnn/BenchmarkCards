# LegalSemi

## 📊 Benchmark Details

**Name**: LegalSemi

**Overview**: LegalSemi is a benchmark specifically curated for legal scenario analysis, comprising 54 legal scenarios annotated by legal experts based on the IRAC (Issue, Rule, Application, Conclusion) framework from Malaysian Contract Law. It aims to address limitations in existing datasets by providing a structured knowledge base (SKE) for enhancing legal reasoning tasks.

**Data Type**: legal scenarios with IRAC annotations

**Domains**:
- Legal

**Languages**:
- English

**Similar Benchmarks**:
- SARA
- SIRAC
- Legal Bench

**Resources**:
- [Resource](https://doi.org/10.1007/s10506-025-09467-5)

## 🎯 Purpose and Intended Users

**Goal**: To provide a curated benchmark for legal scenario analysis using the IRAC framework, enhancing the research and application of large language models in legal reasoning.

**Target Audience**:
- ML Researchers
- Legal Technology Developers
- Legal Practitioners

**Tasks**:
- Legal Scenario Analysis
- IRAC Reasoning Tasks

**Limitations**: N/A

## 💾 Data

**Source**: Curated from legal textbooks and real-world legal problems, annotated by legal experts.

**Size**: 54 legal scenarios

**Format**: Structured JSON

**Annotation**: Rigorous annotation by legal experts following the IRAC framework.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on the comparison of human and automated evaluations of legal reasoning tasks.

**Interpretation**: A model's performance is considered good when it generates accurate and coherent legal analyses.

**Baseline Results**: N/A

**Validation**: Performance of LLMs evaluated through comparison against a structured knowledge base and expert evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
