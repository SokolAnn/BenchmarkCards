# IBACBench

## 📊 Benchmark Details

**Name**: IBACBench

**Overview**: IBACBench is the first benchmark for evaluating the synthesis and auditing capabilities of DePLOI, designed to test access control policy implementations, leveraging existing NL2SQL benchmarks and real-world policies.

**Data Type**: access control policies and SQL implementations

**Domains**:
- Database Management

**Languages**:
- English

**Similar Benchmarks**:
- Spider
- Dr. Spider
- BIRD

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the synthesis and auditing quality of access control implementations using policy representations based on IBAC-DB.

**Target Audience**:
- Database Administrators
- Machine Learning Researchers
- Industry Practitioners

**Tasks**:
- Access Control Auditing
- Policy Synthesis

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation using GPT-4 and real-world access control datasets.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Attribute Subset Execution Accuracy
- F1 Score

**Calculation**: Attribute Subset Execution Accuracy counts semantically equivalent but tuple-inequivalent answers as correct. F1 Score assesses compliance with access control policies.

**Interpretation**: Higher scores indicate better synthesis and auditing accuracy, with specific attention to capturing complex role and permission relationships.

**Validation**: Validation through comparison against existing NL2SQL benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
