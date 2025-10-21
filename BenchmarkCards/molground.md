# MolGround

## 📊 Benchmark Details

**Name**: MolGround

**Overview**: MolGround is a benchmark designed to evaluate a model's referential abilities in molecular understanding by explicitly associating molecular concepts with specific structural components. It consists of 117,000 question-answer pairs across five subtasks.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Cheminformatics
- Molecular Science

**Languages**:
- English

**Similar Benchmarks**:
- ChemBench4K
- MoleculeQA

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To enhance the referential aspect of molecular understanding and to evaluate models' grounding abilities in the context of molecular science.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Chemical Named Entity Recognition
- Name-Structure Mapping
- Referential Substructure Localization
- Substructure Relationship Grounding
- Substructure Frequency Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Collected from existing molecular captioning datasets and published chemical literature.

**Size**: 117,000 question-answer pairs

**Format**: N/A

**Annotation**: Annotated with the help of human experts and a grounding agent.

## 🔬 Methodology

**Methods**:
- Evaluator with baselines LLMs including GPT-4o and LLaMA
- Prototype of a grounding agent for data collection and validation

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated based on the performance of models on the defined tasks.

**Interpretation**: Higher accuracy and F1-scores indicate better grounding and recognition capabilities of models.

**Baseline Results**: Models struggle, with performances generally below 0.5 accuracy in most tasks.

**Validation**: Metrics calculated through the evaluation of model outputs against ground truth data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
