# Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?

## 📊 Benchmark Details

**Name**: Fundamental Problems With Model Editing: How Should Rational Belief Revision Work in LLMs?

**Overview**: This paper critiques the standard formulation of the model editing problem and proposes a semi-synthetic testbed for model editing research. It introduces a dataset based on Wikidata for evaluating model edits against labels given by an idealized Bayesian agent.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/peterbhase/LLM-belief-revision)

## 🎯 Purpose and Intended Users

**Goal**: To provide a formal testbed for evaluating model editing methods in language models against Bayesian standards.

**Target Audience**:
- ML Researchers
- AI Ethics Researchers
- Model Developers

**Tasks**:
- Model Editing
- Belief Revision

**Limitations**: N/A

## 💾 Data

**Source**: Generated from Wikidata with a focus on factual entailment and logical coherence.

**Size**: 204 million tokens

**Format**: Text

**Annotation**: Developed with semi-synthetic methods including Bayesian posteriors for training and evaluation.

## 🔬 Methodology

**Methods**:
- LoRA Fine-tuning
- Bayesian Model Fitting

**Metrics**:
- Generative Accuracy
- Probabilistic Coherence
- Logical Coherence

**Calculation**: Metrics are calculated by comparing model probabilities against Bayesian posterior probabilities and logical axioms.

**Interpretation**: Better model edits should achieve high generative accuracy and maintain logical coherence with Bayesian principles.

**Validation**: The benchmark is validated against a Bayesian model’s expectations after editing an LLM.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
