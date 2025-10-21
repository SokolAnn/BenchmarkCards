# Protap (A Benchmark for Protein Modeling on Realistic Downstream Applications)

## 📊 Benchmark Details

**Name**: Protap (A Benchmark for Protein Modeling on Realistic Downstream Applications)

**Overview**: Protap is a comprehensive benchmark that systematically compares backbone architectures, pretraining strategies, and domain-specific models across diverse and realistic downstream protein applications, focusing on five applications including two novel specialized tasks: enzyme-catalyzed protein cleavage site prediction and targeted protein degradation.

**Data Type**: protein sequences and structures, enzyme-catalyzed cleavage data, protein-ligand interactions

**Domains**:
- Biomedical
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- TAPE
- ProteinGLUE
- PEER

**Resources**:
- [GitHub Repository](https://github.com/Trust-App-AI-Lab/protap)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating different protein modeling tasks and the effectiveness of various model architectures and pretraining strategies.

**Target Audience**:
- ML Researchers
- Bioinformaticians
- Domain Experts

**Tasks**:
- Enzyme-Catalyzed Protein Cleavage Site Prediction
- Targeted Protein Degradation by Proteolysis-Targeting Chimeras
- Protein-Ligand Interactions
- Protein Function Annotation Prediction
- Mutation Effect Prediction for Protein Optimization

**Limitations**: N/A

## 💾 Data

**Source**: MEROPS for cleavage site prediction, PROTAC-DB for targeted protein degradation, KDBNet for protein-ligand interactions, DeepFRI for function annotation, ProteinGym for mutation effect prediction.

**Size**: 542,378 protein structures

**Format**: JSON and .pickle for structures, .txt for labels, .sdf for molecular structures

**Annotation**: Annotations derived from protein databases and specialized datasets for each application.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- AUC
- AUPR
- Fmax
- Mean Squared Error

**Calculation**: Metrics are calculated based on model performance on downstream tasks involving various protein applications.

**Interpretation**: High metric values indicate better model performance in accurately predicting biological functions and interactions.

**Baseline Results**: N/A

**Validation**: The benchmark was validated through comparisons against existing models across realistic applications.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Datasets are provided under MIT License, and original sources retain their respective licenses.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
