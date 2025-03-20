# TRUST GPT

## 📊 Benchmark Details

**Name**: TRUST GPT

**Overview**: A comprehensive benchmark designed to evaluate the ethical implications of large language models (LLMs) focusing on three key perspectives: toxicity, bias, and value-alignment.

**Data Type**: text

**Domains**:
- natural language processing
- ethical evaluations

**Similar Benchmarks**:
- HELM
- BIG-BENCH HHH E VAL

**Resources**:
- [Resource](PERSPECTIVE API)
- [Resource](SOCIAL CHEMISTRY 101)

## 🎯 Purpose and Intended Users

**Goal**: To enhance understanding of the performance of conversation generation models and promote the development of ethical and socially responsible language models.

**Target Audience**:
- AI researchers
- data scientists
- industry practitioners

**Tasks**:
- Evaluate toxicity in language models
- Assess model bias
- Evaluate value-alignment

**Limitations**: None

**Out of Scope Uses**:
- Toxic content generation
- Hateful speech propagation

## 💾 Data

**Source**: SOCIAL CHEMISTRY 101 dataset

**Size**: 292k social norms

**Format**: text

**Annotation**: Descriptions of social norms with related human judgments

## 🔬 Methodology

**Methods**:
- Predefined prompts based on social norms
- Mann-Whitney U test for bias assessment
- PERSPECTIVE API for toxicity evaluation

**Metrics**:
- Average toxicity score
- Standard deviation
- Soft accuracy
- Hard accuracy
- RtA (Refusal to Answer)

**Calculation**: Average scores are calculated based on model responses to prompts in toxicity, bias, and value alignment evaluations.

**Interpretation**: High toxicity scores indicate poor ethical compliance; high bias indicates unfair treatment of demographic groups; value-alignment metrics assess adherence to social norms.

**Validation**: Results validated through empirical analysis on eight different LLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- toxicity
- bias
- ethical misalignment

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Evaluations consider gender, race, and religion demographics.

**Potential Harm**: Potential risk of generating biased or toxic content.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
