# BioMol-MQA: A Multi-Modal Question Answering Dataset For LLM Reasoning Over Bio-Molecular Interactions

## 📊 Benchmark Details

**Name**: BioMol-MQA: A Multi-Modal Question Answering Dataset For LLM Reasoning Over Bio-Molecular Interactions

**Overview**: BioMol-MQA is a new question-answering (QA) dataset on polypharmacy, composed of a multimodal knowledge graph with text and molecular structure for information retrieval and challenging questions designed to test LLM capabilities in retrieving and reasoning over multimodal data.

**Data Type**: question-answering pairs

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- MoleculeQA
- PubChemQA
- RAGBench
- ChatRAG Bench
- CRAG
- STaRK

**Resources**:
- [GitHub Repository](https://github.com/saptarshi059/biomolqa/tree/main/code/common_scripts)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate models for handling complex, real-world medical queries involving multi-modal reasoning.

**Target Audience**:
- ML Researchers
- Healthcare Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: The dataset is limited to drugs that have both text and SMILES representation; otherwise, relevant proteins only have text, creating potential imbalances.

## 💾 Data

**Source**: A multimodal knowledge graph with drug-drug and drug-protein interactions along with text and SMILES for each drug.

**Size**: 1,686 questions

**Format**: JSON

**Annotation**: Manually generated questions integrated with multimodal data.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Lexical EM
- Lexical F1
- BERTScore F1

**Calculation**: Metrics calculated by comparing generated model outputs to ground truth.

**Interpretation**: Higher scores indicate better model performance in answering questions accurately.

**Baseline Results**: Results on existing LLMs that show improvement with multimodal context.

**Validation**: Dataset validated through human evaluators and LLM performance metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Hallucination

**Demographic Analysis**: Questions crafted to explore reasoning across demographics in healthcare.

**Potential Harm**: Potential misinformation leading to adverse health decisions if models misinterpret complex queries.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
