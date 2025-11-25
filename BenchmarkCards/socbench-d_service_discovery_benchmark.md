# SOCBench-D (Service Discovery Benchmark)

## 📊 Benchmark Details

**Name**: SOCBench-D (Service Discovery Benchmark)

**Overview**: SOCBench-D is a novel service discovery benchmark comprising natural language queries and expected endpoints to evaluate RAG for OpenAPI endpoint discovery comprehensively across numerous domains.

**Data Type**: query-endpoint pairs

**Domains**:
- Energy
- Materials
- Industrials
- Consumer Discretionary
- Consumer Staples
- Healthcare
- Financials
- Information Technology
- Communication Services
- Utilities
- Real Estate

**Languages**:
- English

**Similar Benchmarks**:
- RestBench

**Resources**:
- [GitHub Repository](https://github.com/IAAS/SOCBench)
- [Resource](https://dx.doi.org/10.21227/vdm4-k186)

## 🎯 Purpose and Intended Users

**Goal**: To benchmark service discovery with natural language queries across the most relevant domains and evaluate Retrieval Augmented Generation (RAG) techniques.

**Target Audience**:
- Researchers
- Industry Practitioners

**Tasks**:
- Endpoint Discovery

**Limitations**: N/A

## 💾 Data

**Source**: Generated OpenAPIs using a Large Language Model (LLM).

**Size**: 550 queries

**Format**: JSON

**Annotation**: Automated generation and validation using LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Precision
- Recall

**Calculation**: Metrics calculated based on the accuracy of endpoint retrieval against expected results across various domains.

**Interpretation**: Higher precision indicates better filtering of relevant endpoint information; higher recall reflects the ability to retrieve more correct endpoints.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through the creation of multiple instances and checking endpoint correctness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
