# Crowdsourced Stereotype Pairs

## 📊 Benchmark Details

**Name**: Crowdsourced Stereotype Pairs (Crows-Pairs)

**Overview**: A Challenge Dataset for Measuring Social Biases in Masked Language Models.

**Data Type**: Test Data

**Domains**:
- Natural Language Processing
- Social Bias Evaluation

**Languages**:
- English

**Similar Benchmarks**:
- StereoSet
- WinoBias

**Resources**:
- [GitHub Repository](https://github.com/nyu-mll/crows-pairs)

## 🎯 Purpose and Intended Users

**Goal**: To measure social biases in language models against protected demographic groups in the US.

**Target Audience**:
- Researchers in NLP
- Developers of machine learning models
- Ethics researchers

**Tasks**:
- Evaluate bias in masked language models
- Measure stereotype use in sentence generation

**Limitations**: Dataset does not cover all potential biases beyond the specified nine categories.

**Out of Scope Uses**:
- Training language models directly using this dataset
- Using the dataset as a source of examples of written English

## 💾 Data

**Source**: Amazon Mechanical Turk

**Size**: 1508 examples

**Format**: Pairs of sentences (stereotype vs anti-stereotype)

**Annotation**: Crowdsourced validation by multiple annotators

## 🔬 Methodology

**Methods**:
- Crowdsourcing for data collection
- Majority vote for validation of examples

**Metrics**:
- Comparison of likelihood of stereotypical vs less stereotypical sentences

**Calculation**: Percentage of examples where the model prefers the more stereotyping sentence.

**Interpretation**: A model that shows a higher preference for stereotyping sentences indicates more bias.

**Baseline Results**: BERT, RoBERTa, and ALBERT models were evaluated, with results showing significant bias in all models.

**Validation**: 5 validation annotations per example with majority agreement required for validity.

## ⚠️ Targeted Risks

**Risk Categories**:
- Social Bias
- Cultural Insensitivity

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Focused on historically disadvantaged groups in the US.

**Potential Harm**: Propagation of harmful stereotypes affecting marginalized communities.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All personal identifying information about crowdworkers has been removed.

**Data Licensing**: Not Applicable

**Consent Procedures**: Crowdworkers notified about sensitive nature of task.

**Compliance With Regulations**: Not Applicable
