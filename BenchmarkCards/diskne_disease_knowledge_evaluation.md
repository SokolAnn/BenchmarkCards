# DisKnE (Disease Knowledge Evaluation)

## 📊 Benchmark Details

**Name**: DisKnE (Disease Knowledge Evaluation)

**Overview**: DisKnE is a new benchmark for evaluating biomedical language models' disease knowledge. It explicitly addresses the limitations of previous datasets, allowing for assessments of medical reasoning with clear training-test splits designed to avoid knowledge leakage.

**Data Type**: entailment pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/israa-alghanmi/DisKnE)

## 🎯 Purpose and Intended Users

**Goal**: To assess the disease-centred knowledge captured by pre-trained language models and evaluate their reasoning capabilities.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Natural Language Inference

**Limitations**: N/A

## 💾 Data

**Source**: Derived from MedNLI and MEDIQA-NLI using manual annotation and adversarial example generation.

**Size**: 6,772 examples

**Format**: JSON

**Annotation**: Manually annotated with types of medical reasoning and adversarial perturbation for negative examples.

## 🔬 Methodology

**Methods**:
- Model-based evaluation

**Metrics**:
- F1 Score

**Calculation**: F1 score is calculated for the positive class across different categories.

**Interpretation**: Higher F1 scores indicate better performance of the models in reasoning tasks related to disease knowledge.

**Baseline Results**: ClinicalBERT, BioBERT, SciBERT, and BERT were evaluated on the benchmark with varied performance in terms of F1 across categories.

**Validation**: The evaluation involved detailed performance analysis of various language models on the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
