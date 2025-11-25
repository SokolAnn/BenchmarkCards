# Safe-Embed

## 📊 Benchmark Details

**Name**: Safe-Embed

**Overview**: This paper introduces new pairwise datasets and the Categorical Purity (CP) metric to assess the ability of sentence encoders to distinguish between safe and unsafe prompts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- XSTest
- Do-Not-Answer

**Resources**:
- [GitHub Repository](https://github.com/JwdanielJung/Safe-Embed)

## 🎯 Purpose and Intended Users

**Goal**: To systematically measure the Safety-Critical knowledge of various sentence encoders and improve their capabilities as safety detectors.

**Target Audience**:
- ML Researchers
- Safety Engineers
- Model Developers

**Tasks**:
- Safety Classification
- Safety Detection

**Limitations**: The evaluation only considers short, simple prompts written in English; more complex unsafe prompts were not included.

## 💾 Data

**Source**: Newly created pairwise datasets including Safety-Challenging and Safety-Taxonomy datasets.

**Size**: 1,900 total prompts (250 Safety-Challenging, 939 Do-Not-Answer)

**Format**: CSV

**Annotation**: Manual creation of unsafe prompts to match safe prompts.

## 🔬 Methodology

**Methods**:
- Statistical Analysis
- Categorical Purity Metric Evaluation

**Metrics**:
- Categorical Purity (CP)

**Calculation**: CP is calculated by measuring the cosine similarity among prompts within the same category.

**Interpretation**: A higher CP score indicates better categorization of unsafe prompts.

**Baseline Results**: SBERT-all achieved a CP score of 0.747, ST5-XXL achieved 0.823 for successful categorization.

**Validation**: Results validated against established datasets like XSTest and Do-Not-Answer.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: This benchmark aims to prevent harmful outputs in LLMs from unsafe prompts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
