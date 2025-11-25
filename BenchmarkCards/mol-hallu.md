# Mol-Hallu

## 📊 Benchmark Details

**Name**: Mol-Hallu

**Overview**: Mol-Hallu is a novel free-form evaluation metric that quantifies the degree of hallucination based on the scientific entailment relationship between generated text and actual molecular properties.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MoleculeQA
- MoleculeTextQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and alleviate the LLM’s hallucination in molecular comprehension.

**Target Audience**:
- ML Researchers
- Scientific Community

**Tasks**:
- Molecular Comprehension

**Limitations**: The current benchmark lacks full fine-tuning of large models due to insufficient training resources.

## 💾 Data

**Source**: PubChem

**Size**: N/A

**Format**: N/A

**Annotation**: Automatically annotated using a chemical entity database.

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: Mol-Hallu calculates Recall and Precision by comparing entity entailment probability.

**Interpretation**: Higher Mol-Hallu scores indicate lower hallucination rates in molecular comprehension tasks.

**Validation**: HRPP stage demonstrates substantial improvements on hallucination metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Mol-Hallu evaluation may not accurately represent a model’s hallucination level over all chemistry-related scenarios.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
