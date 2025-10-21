# FOLLOW IR

## 📊 Benchmark Details

**Name**: FOLLOW IR

**Overview**: FOLLOW IR is a benchmark that explicitly measures the instruction following ability of information retrieval (IR) models, comprising a dataset of human annotations on three highly-judged TREC collections.

**Data Type**: question-instruction pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MTEB
- BEIR

**Resources**:
- [GitHub Repository](https://github.com/orionw/FollowIR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation benchmark for IR models to follow complex user instructions.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Following
- Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Three TREC collections: TREC Robust 2004, TREC Common Core 2017, TREC News 2021.

**Size**: Approx. 1836 instruction pairs

**Format**: N/A

**Annotation**: Instructions modified by expert annotators; documents manually re-annotated as relevant or not-relevant.

## 🔬 Methodology

**Methods**:
- Standard Retrieval Metrics
- Pairwise Evaluation

**Metrics**:
- Mean Average Precision (MAP)
- Normalized Discounted Cumulative Gain (nDCG)
- p-MRR

**Calculation**: p-MRR measures rank-wise changes between queries with original versus altered instructions.

**Interpretation**: Higher scores indicate better instruction following by retrieval models.

**Baseline Results**: FOLLOW IR-7B shows marked improvements over prior models.

**Validation**: Evaluated using rank changes before and after instruction modifications.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
