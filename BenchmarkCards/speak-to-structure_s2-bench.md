# Speak-to-Structure (S2-Bench)

## 📊 Benchmark Details

**Name**: Speak-to-Structure (S2-Bench)

**Overview**: S2-Bench is the first benchmark designed to evaluate the open-domain natural language-driven molecule generation capabilities of LLMs, structured around tasks that reflect real-world molecular design challenges.

**Data Type**: molecule generation tasks

**Domains**:
- Natural Language Processing
- Chemistry

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2412.14642)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark for evaluating LLMs on their ability to create diverse molecular candidates from natural language descriptions.

**Target Audience**:
- ML Researchers
- Chemists
- Drug Discovery Scientists

**Tasks**:
- Molecule Editing
- Molecule Optimization
- Customized Molecule Generation

**Limitations**: N/A

## 💾 Data

**Source**: S2-Bench is constructed programmatically using large chemical databases like PubChem and Zinc-250K.

**Size**: 45,000 test samples for S2-Bench, with OpenMolIns providing up to 1,200,000 instruction-molecule pairs.

**Format**: N/A

**Annotation**: Automated evaluation based on objective molecular properties and structural rules.

## 🔬 Methodology

**Methods**:
- Automated evaluation metrics
- Task-specific success rates

**Metrics**:
- Success Rate
- Similarity
- Novelty
- Validity

**Calculation**: Metrics are calculated based on the model's adherence to task requirements and the quality of generated molecules.

**Interpretation**: Higher scores indicate better alignment with desired molecular properties and structural integrity.

**Baseline Results**: The benchmark evaluates multiple LLMs, with performance comparisons documented in detailed tables.

**Validation**: S2-Bench's design ensures diverse and robust evaluation of LLM capabilities in molecule generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
