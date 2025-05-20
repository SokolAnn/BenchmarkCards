# BBQ: A Hand-Built Bias Benchmark for Question Answering

## 📊 Benchmark Details

**Name**: BBQ

**Overview**: BBQ is a dataset of question sets that highlight attested social biases against people belonging to protected classes along nine social dimensions relevant for U.S. English-speaking contexts. It evaluates model responses in terms of how *consistently* responses reflect social biases and under what contexts these biases override correct answers.

**Data Type**: Dataset

**Domains**:
- Question Answering
- Natural Language Processing

**Languages**:
- English (Original)
- Korean ([Cho et al., 2024 - K-BBQ](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00661/120915))
- Dutch, Spanish, Turkish ([Kranen et al., 2024 - Multilingual BBQ Adaptation](https://arxiv.org/pdf/2406.07243))

**Similar Benchmarks**:
- UnQover

**Resources**:
- [GitHub Repository](https://github.com/nyu-mll/BBQ)
- [Original Paper (NeurIPS 2021 Datasets and Benchmarks Track)](https://arxiv.org/abs/2110.08193)

## 🎯 Purpose and Intended Users

**Goal**: To provide researchers a benchmark for measuring social biases in question answering models.

**Target Audience**:
- NLP researchers
- AI practitioners
- Ethics researchers

**Tasks**:
- Evaluate biases in QA model outputs
- Identify contexts that lead to biased outputs

**Limitations**: The dataset focuses on biases relevant to the U.S. context and may not generalize to different cultural settings. It is English-only, though work has expanded BBQ into other languages (e.g., Korean, Dutch, Spanish, Turkish).

**Out of Scope Uses**:
- Generalizing results to non-U.S. languages or contexts

## 💾 Data

**Source**: Constructed by authors

**Size**: 58,492 unique examples

**Format**: Templated question + answer option sets

**Annotation**: Validated by crowdworkers

## 🔬 Methodology

**Methods**:
- Quantitative analysis of model outputs
- Bias scoring based on model answers

**Metrics**:
- Accuracy
- Bias score

**Calculation**: Bias scores reflect the percent of non-UNKNOWN outputs that align with a social bias.

**Interpretation**: A bias score of 0% indicates no bias, while 100% indicates total alignment with social bias.

**Baseline Results**: N/A

**Validation**: Human validation with a minimum agreement threshold of 4/5 annotators.

## ⚠️ Targeted Risks

**Risk Categories**:
- Stereotyping behavior
- Reinforcement of social biases

**Atlas Risks**:
- **Fairness**: Data bias
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: Tested biases against various social categories including gender, race, socioeconomic status.

**Potential Harm**: Reinforcement of harmful stereotypes in model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Released under the CC-BY 4.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
