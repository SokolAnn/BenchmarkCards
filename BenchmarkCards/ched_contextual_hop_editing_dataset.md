# CHED (Contextual Hop Editing Dataset)

## 📊 Benchmark Details

**Name**: CHED (Contextual Hop Editing Dataset)

**Overview**: CHED is a benchmark designed to evaluate the context robustness of knowledge editing methods in language models, assessing how well they perform when presented with distracting preceding contexts.

**Data Type**: knowledge editing pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- CounterFact
- MQuAKE
- RippleEdits

**Resources**:
- [GitHub Repository](https://github.com/holi-lab/CoRE)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging evaluation for knowledge editing techniques by incorporating realistic context scenarios that affect editing performance.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Editing

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset using prefix contexts derived from Wikidata and existing knowledge editing instances.

**Size**: 21,782 triplets with 314,385 hop-word prefix contexts

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Efficacy
- Generalization
- Specificity
- General Ability
- Fluency

**Calculation**: Calculated based on the model's ability to correctly edit knowledge while excluding original entries.

**Interpretation**: High efficacy indicates successful knowledge editing under context variability.

**Validation**: Evaluated using various existing knowledge editing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
