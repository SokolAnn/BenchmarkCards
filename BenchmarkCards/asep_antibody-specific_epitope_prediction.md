# AsEP (Antibody-specific Epitope Prediction)

## 📊 Benchmark Details

**Name**: AsEP (Antibody-specific Epitope Prediction)

**Overview**: AsEP is the largest dataset of antibody-antigen complex structures, containing clustered epitope groups for developing and evaluating epitope prediction methods. The dataset provides an easy-to-use interface in Python with graph representations of antibody-antigen complexes.

**Data Type**: graph

**Domains**:
- Healthcare
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/biochunan/AsEP-dataset)
- [Resource](https://doi.org/10.5281/zenodo.11495514)

## 🎯 Purpose and Intended Users

**Goal**: To establish a benchmark dataset for epitope prediction in antibody-antigen interactions and facilitate research in this area.

**Target Audience**:
- ML Researchers
- Domain Experts
- Biochemists

**Tasks**:
- Epitope Prediction
- Graph-based Link Prediction

**Limitations**: N/A

## 💾 Data

**Source**: The dataset was sourced from the Antibody Database (AbDb) and processed from original PDB files.

**Size**: 1,723 antibody-antigen complexes

**Format**: PDB, JSON

**Annotation**: Manually annotated with surface residues and CDR regions filtered from the original dataset.

## 🔬 Methodology

**Methods**:
- Graph Neural Networks
- Node Classification
- Link Prediction

**Metrics**:
- Matthew's Correlation Coefficient (MCC)
- Precision
- Recall
- F1 Score
- Area Under ROC Curve (AUC-ROC)

**Calculation**: Metrics are calculated using standard formulas for binary classification, including true positives, false positives, etc.

**Interpretation**: MCC values close to 1 indicate better model performance, while lower values suggest poor predictions.

**Baseline Results**: Performance benchmarked using several existing methods with notable improvements using the introduced method WALLE.

**Validation**: Tested using a random split based on the ratio of epitope to antigen surface residues and a split by epitope groups.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons Attribution 4.0 International (CC BY 4.0)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
