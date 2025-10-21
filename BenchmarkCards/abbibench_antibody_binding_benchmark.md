# AbBiBench (Antibody Binding Benchmark)

## 📊 Benchmark Details

**Name**: AbBiBench (Antibody Binding Benchmark)

**Overview**: AbBiBench provides a unified, biologically grounded evaluation framework for antibody binding affinity maturation and design by utilizing antibody-antigen (Ab-Ag) complexes as functional units.

**Data Type**: sequence data and binding affinity measurements

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/AbBibench/Antibody_Binding_Benchmark_Dataset)
- [GitHub Repository](https://github.com/MSBMI-SAFE/AbBiBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark framework for evaluating models that predict and design high-affinity antibodies.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Affinity Prediction
- Antibody Sequence Design

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets containing experimental binding affinity studies from public repositories.

**Size**: 155,853 mutated heavy chain antibodies across 9 antigens

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Correlation analysis between model likelihood and experimental affinity
- Zero-shot prediction of binding affinity
- Design of antibody variants

**Metrics**:
- Spearman correlation
- Precision at K

**Calculation**: Correlation calculated between model likelihoods and experimentally measured binding affinities.

**Interpretation**: Higher correlation indicates better model performance in predicting strong binders.

**Baseline Results**: N/A

**Validation**: Models evaluated using curated datasets of experimentally determined binding affinities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
