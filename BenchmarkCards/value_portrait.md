# Value Portrait

## 📊 Benchmark Details

**Name**: Value Portrait

**Overview**: Value Portrait is a psychometrically validated benchmark for evaluating LLMs' value orientations, constructed from real-world user interactions, which includes query-response pairs annotated with value correlations.

**Data Type**: query-response pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ValueNet
- ValueBench

**Resources**:
- [GitHub Repository](https://github.com/holi-lab/ValuePortrait)

## 🎯 Purpose and Intended Users

**Goal**: To assess the value orientations of language models using a benchmark that reflects actual user interactions and evaluates alignment with human values.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Value Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from datasets of human-LLM interactions (ShareGPT, LMSYS) and human-human advisory contexts (Reddit, Dear Abby).

**Size**: 520 query-response pairs

**Format**: JSON

**Annotation**: Annotated by human subjects using a psychometric approach to correlate responses with psychological dimensions.

## 🔬 Methodology

**Methods**:
- Human evaluation

**Metrics**:
- Correlation with Schwartz values
- Spearman correlation

**Calculation**: Using Spearman correlations between participant ratings and their assessed values.

**Interpretation**: Higher correlations indicate stronger alignment with corresponding value dimensions.

**Baseline Results**: N/A

**Validation**: Validated through internal consistency measures (Cronbach's alpha) showing high reliability across value dimensions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Demographic biases in LLMs' value perceptions were analyzed across different groups.

**Potential Harm**: Identifies potential biases in how LLMs represent various demographic groups.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Participants' data was anonymized, and all personal identifiers were replaced with unique IDs.

**Data Licensing**: Licensed under Apache 2.0 for ShareGPT and MIT for other datasets.

**Consent Procedures**: Participants granted explicit consent for their demographic information and responses to be used in research.

**Compliance With Regulations**: Compliant with human subject research ethical standards and has received Institutional Review Board (IRB) approval.
