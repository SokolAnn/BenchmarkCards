# ChemCoTBench

## 📊 Benchmark Details

**Name**: ChemCoTBench

**Overview**: ChemCoTBench is a step-by-step, application-oriented benchmark for evaluating LLM reasoning in chemical applications, addressing limitations in current chemical evaluations by incorporating modular chemical operations and structured evaluability.

**Data Type**: text

**Domains**:
- Chemistry

**Languages**:
- English

**Similar Benchmarks**:
- ChemCoTDataset
- MolPuzzle
- ChemLLM

**Resources**:
- [Resource](https://huggingface.co/datasets/OpenMol/ChemCoTBench)
- [Resource](https://huggingface.co/datasets/OpenMol/ChemCoTDataset)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized evaluation platform for complex chemical reasoning and enhance LLMs' performance in chemistry-related tasks.

**Target Audience**:
- ML Researchers
- Chemists
- AI Practitioners

**Tasks**:
- Molecular Property Optimization
- Chemical Reaction Prediction
- Molecular Understanding
- Molecular Editing

**Limitations**: N/A

## 💾 Data

**Source**: Data sourced from published chemical datasets including PubChem, ChEMBL, ZINC, and patent databases such as USPTO and Reaxys.

**Size**: 1,495 samples across 22 chemical tasks

**Format**: SMILES

**Annotation**: Annotated by experts and LLM-assisted annotation, ensuring high data quality through multi-stage review.

## 🔬 Methodology

**Methods**:
- Quantitative assessments using accuracy, mean absolute error, and passage success rate.
- Expert review for validation of chemical entities.

**Metrics**:
- Accuracy
- Mean Absolute Error
- Success Rate

**Calculation**: Metrics were calculated based on the correctness of predicted outcomes, precision for regression tasks, and structural similarity measures.

**Interpretation**: High accuracy indicates strong reasoning capabilities of models in chemical tasks.

**Validation**: Hybrid validation combining expert review and automated model evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
