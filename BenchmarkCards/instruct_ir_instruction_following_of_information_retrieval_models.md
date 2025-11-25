# INSTRUCT IR (Instruction Following of Information Retrieval Models)

## 📊 Benchmark Details

**Name**: INSTRUCT IR (Instruction Following of Information Retrieval Models)

**Overview**: INSTRUCT IR is designed to evaluate instruction-following ability of retrieval models with diverse user-aligned instructions for each query, reflecting real-world search scenarios.

**Data Type**: instruction-query-target pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BEIR
- LoTTE
- X2
- MTEB
- M-BEIR

**Resources**:
- [GitHub Repository](https://github.com/kaistAI/InstructIR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the instruction-following capabilities of information retrieval models and to improve alignment with user instructions.

**Target Audience**:
- ML Researchers
- Information Retrieval Specialists

**Tasks**:
- Information Retrieval

**Limitations**: The challenge lies in accurately simulating real user instructions within an automated data generation setting.

## 💾 Data

**Source**: Generated from the MSMARCO dataset using GPT-4 for instruction creation and target adjustment.

**Size**: 9,906 instances

**Format**: JSON

**Annotation**: Automatically generated and filtered through a multi-stage pipeline.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Normalized Cumulative Discount Gain (nDCG)
- Robustness Score

**Calculation**: Robustness score is calculated based on the minimum nDCG score of models responding to the same query with different instructions.

**Interpretation**: Higher nDCG and Robustness scores indicate better instruction-following capabilities of models.

**Validation**: Human evaluation ensured quality and validity of generated datasets through majority voting among annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
