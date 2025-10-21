# Holmes

## 📊 Benchmark Details

**Name**: Holmes

**Overview**: Holmes is a benchmark to assess the linguistic competence of language models, specifically designed to disentangle linguistic competence from other cognitive abilities.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://holmes-benchmark.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To assess language models' linguistic competence regarding various linguistic phenomena.

**Target Audience**:
- ML Researchers
- Language Model Developers

**Tasks**:
- Linguistic Competence Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Includes more than 200 datasets addressing linguistic phenomena such as syntax, morphology, semantics, reasoning, and discourse.

**Size**: 208 datasets

**Format**: Various formats depending on datasets

**Annotation**: Manual annotation and pre-existing datasets

## 🔬 Methodology

**Methods**:
- Classifier-based probing
- Experimental evaluations

**Metrics**:
- Macro F1 Score
- Pearson correlation

**Calculation**: Probes' performance based on the classification or regression of linguistic phenomena.

**Interpretation**: Higher scores indicate better encoding of linguistic phenomena in language model representations.

**Baseline Results**: N/A

**Validation**: Robustness tested via control tasks

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Holmes adopts existing datasets, potentially inheriting biases present in them.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Some datasets used are based on licensed resources, while others are open access.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
