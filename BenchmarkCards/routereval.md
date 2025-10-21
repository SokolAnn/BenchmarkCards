# RouterEval

## 📊 Benchmark Details

**Name**: RouterEval

**Overview**: RouterEval is a benchmark tailored for router research, which includes over 200,000,000 performance records for 12 popular LLM evaluations across various areas such as common-sense reasoning, semantic understanding, etc., based on over 8,500 various LLMs.

**Data Type**: performance records

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ARC
- HellaSwag
- MMLU
- TruthfulQA
- Winogrande
- GSM8k
- IFEval
- BBH
- GPQA
- MUSR
- MATH Lvl 5
- MMLU-PRO

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic framework to assess router effectiveness and enable comprehensive evaluation of routing methods in large language models.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Router Evaluation

**Limitations**: Deployment challenges arise due to the large number of LLMs required for optimal performance.

## 💾 Data

**Source**: Performance records collected from over 8,500 LLMs across various benchmarks.

**Size**: 200,000,000 records

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Overall performance
- Reference value
- Best single model value
- Classification bias

**Calculation**: Performance calculated based on the selection vector created by the router and evaluation against reference models.

**Interpretation**: Higher performance metrics indicate better routing effectiveness.

**Baseline Results**: Details of each router's performance metrics provided under varying conditions in the tables of the paper.

**Validation**: Performance validated through analysis of multiple router candidate groups.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
