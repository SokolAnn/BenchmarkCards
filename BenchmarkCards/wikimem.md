# WikiMem

## 📊 Benchmark Details

**Name**: WikiMem

**Overview**: WikiMem is a dataset of over 5,000 natural language canaries covering 243 human-related properties from Wikidata, and a model-agnostic metric to quantify human–fact associations in LLMs.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/WikiMem-Eval-B13C)

## 🎯 Purpose and Intended Users

**Goal**: To provide a foundation for identifying and quantifying personal data in LLMs at the individual level, enabling dynamic construction of forget sets for machine unlearning and RTBF requests.

**Target Audience**:
- ML Researchers
- Regulators
- Privacy Advocates

**Tasks**:
- Privacy Auditing
- Data Removal Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Wikidata

**Size**: 5,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Data analysis

**Metrics**:
- Negative Log-Likelihood (NLL)

**Calculation**: Scores are derived from calibrated NLL ranking over counterfactuals.

**Interpretation**: Model memorization is determined by whether ground-truth values are ranked first.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study focuses on transparency and supporting RTBF compliance by measuring factual memorization, emphasizing the importance of privacy in LLMs.

**Data Licensing**: The dataset will be made publicly available under CC-BY.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
