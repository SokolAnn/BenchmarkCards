# SOFA (Social Fairness)

## 📊 Benchmark Details

**Name**: SOFA (Social Fairness)

**Overview**: SOFA is a large-scale benchmark designed to address the limitations of existing fairness collections, expanding the analysis of social biases in language models to include a diverse range of identities and stereotypes.

**Data Type**: probing statements

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CROWS-PAIRS
- STEREO SET

**Resources**:
- [Resource](https://huggingface.co/datasets/copenlu/sofa)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate social biases encoded in language models by probing their responses across a diverse set of identities and stereotypes.

**Target Audience**:
- ML Researchers
- Fairness Auditors
- AI Ethics Practitioners

**Tasks**:
- Fairness Benchmarking
- Social Bias Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Combining stereotypes from the SOCIAL BIAS INFERENCE CORPUS (SBIC) and identities from the lexicon by Czarnowska et al. (2021).

**Size**: 1,490,120 probes

**Format**: N/A

**Annotation**: Generated from human-annotated text sources.

## 🔬 Methodology

**Methods**:
- Perplexity-based evaluation

**Metrics**:
- Perplexity (PPL)
- Delta Disparity Score (DDS)

**Calculation**: Perplexity is calculated using the exponentiated average negative log-likelihood of a sequence.

**Interpretation**: Low PPL values indicate higher likelihood for certain stereotypes, suggesting presence of bias.

**Baseline Results**: N/A

**Validation**: Evaluated by testing against existing benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: Analysis conducted across various identity dimensions such as gender, religion, disability, and nationality.

**Potential Harm**: The benchmark aims to identify and measure the encoded biases which lead to unfair treatments in language model outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
