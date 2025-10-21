# SylloBio-NLI

## 📊 Benchmark Details

**Name**: SylloBio-NLI

**Overview**: SylloBio-NLI is a novel framework for evaluating large language models on biomedical syllogistic reasoning by leveraging external ontologies to instantiate diverse syllogistic arguments.

**Data Type**: natural language arguments

**Domains**:
- Natural Language Processing
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- GLoRE
- NLI4CT

**Resources**:
- [GitHub Repository](https://github.com/neuro-symbolic-ai/SylloBio-NLI)

## 🎯 Purpose and Intended Users

**Goal**: To advance the availability of resources for biomedical syllogistic reasoning and evaluate the capabilities of state-of-the-art NLI models.

**Target Audience**:
- ML Researchers
- Biomedical Researchers
- NLP Practitioners

**Tasks**:
- Textual Entailment
- Premise Selection

**Limitations**: N/A

## 💾 Data

**Source**: A specialized dataset generated using Reactome, encompassing natural language syllogistic arguments.

**Size**: 12,098 entity-gene names and total of 211,840 instances

**Format**: N/A

**Annotation**: Automated generation leveraging domain-specific ontologies and thesauri.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall
- Reasoning Accuracy

**Calculation**: Metrics are calculated by comparing predictions to annotated labels.

**Interpretation**: Higher scores indicate better reasoning capabilities of the LLMs.

**Validation**: Performance was validated through extensive experiments comparing zero-shot and few-shot prompting.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
