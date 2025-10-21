# Codebook Datasets for LLM Measurement

## 📊 Benchmark Details

**Name**: Codebook Datasets for LLM Measurement

**Overview**: This paper gathers and curates three real-world political science codebooks covering protest events, political violence, and manifestos, and proposes a five-stage framework for evaluating LLMs in measuring political science concepts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- SQuAD

**Resources**:
- [Resource](https://dataverse.harvard.edu/dataverse/politicalscience)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve the ability of LLMs to accurately follow codebooks for various political science concepts.

**Target Audience**:
- Political Scientists
- Data Scientists
- AI Researchers

**Tasks**:
- Multi-Class Classification

**Limitations**: N/A

## 💾 Data

**Source**: Three curated real-world political science codebooks: BFRS dataset, CCC dataset, and Manifesto Project corpus.

**Size**: 20,978 training instances (BFRS), 4,710 training instances (CCC), 8,081 training instances (Manifestos)

**Format**: CSV

**Annotation**: Hand-coded by experts

## 🔬 Methodology

**Methods**:
- Label-free Behavioral Testing
- Zero-shot Evaluation
- Supervised Finetuning

**Metrics**:
- F1 Score

**Calculation**: Weighted F1 scores evaluated based on predictions and actual labels in the datasets.

**Interpretation**: Higher F1 scores indicate better alignment with the definitions provided in the codebooks.

**Baseline Results**: N/A

**Validation**: Zero-shot evaluations and error analyses were performed to determine model capabilities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets will be posted on the Harvard Dataverse in encrypted format to prevent contamination.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
