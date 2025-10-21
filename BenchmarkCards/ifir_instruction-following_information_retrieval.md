# IFIR (Instruction-Following Information Retrieval)

## 📊 Benchmark Details

**Name**: IFIR (Instruction-Following Information Retrieval)

**Overview**: IFIR is a comprehensive benchmark designed to evaluate instruction-following information retrieval capabilities in expert domains like finance, law, healthcare, and scientific literature, encompassing 2,426 high-quality instruction-following examples with varying complexity.

**Data Type**: instruction-following queries

**Domains**:
- Finance
- Law
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- FOLLOW IR
- INSTRUCT IR

**Resources**:
- [GitHub Repository](https://github.com/SighingSnow/IFIR)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate instruction-following capabilities of information retrievers across specialized domains and provide insights for model development.

**Target Audience**:
- ML Researchers
- Domain Experts
- Information Retrieval Practitioners

**Tasks**:
- Information Retrieval
- Instruction Following

**Limitations**: The dataset has a limited number of queries accompanied by instructions and does not provide a training dataset for future works.

## 💾 Data

**Source**: Adapted from established traditional information retrieval benchmarks in expert domains (Finance, Law, Healthcare, Scientific Literature).

**Size**: 2,426 queries

**Format**: JSON

**Annotation**: Human-validated instruction-following queries.

## 🔬 Methodology

**Methods**:
- Human evaluation
- LLM-based evaluation metrics

**Metrics**:
- nDCG
- INSTFOL

**Calculation**: Both metrics evaluate the performance of the instruction-following retrieval systems, with INSTFOL specifically assessing the improvement gained by incorporating instructions.

**Interpretation**: Higher nDCG and INSTFOL scores indicate better instruction-following capabilities and effective retrieval.

**Baseline Results**: Baseline performance was assessed against traditional retrieval models and instruction-tuned models.

**Validation**: Extensive human expert validation during dataset construction.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
