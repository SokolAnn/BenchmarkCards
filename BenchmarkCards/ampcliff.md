# AMPCliff

## 📊 Benchmark Details

**Name**: AMPCliff

**Overview**: This study introduces a quantitative definition and benchmarking framework AMPCliff for the activity cliff (AC) phenomenon in antimicrobial peptides composed of canonical amino acids.

**Data Type**: paired AMPs with MIC values

**Domains**:
- Healthcare

**Languages**:
- English

**Similar Benchmarks**:
- GRAMPA (Antimicrobial Peptide Dataset)

**Resources**:
- [GitHub Repository](https://github.com/Kewei2023/AMPCliff-generation)
- [Resource](https://www.healthinformaticslab.org/supp/)

## 🎯 Purpose and Intended Users

**Goal**: To quantitatively define the activity cliff phenomena in antimicrobial peptides and benchmark prediction models for detecting these phenomena.

**Target Audience**:
- ML Researchers
- Pharmaceutical Researchers

**Tasks**:
- Activity Cliffs Prediction

**Limitations**: N/A

## 💾 Data

**Source**: GRAMPA dataset

**Size**: 2758 AMPs

**Format**: N/A

**Annotation**: Quantitative measurement of antimicrobial activity through Minimum Inhibitory Concentration (MIC)

## 🔬 Methodology

**Methods**:
- Machine Learning algorithms
- Deep Learning algorithms
- Masked Language Models
- Generative Language Models

**Metrics**:
- Spearman correlation coefficient (SCC)
- Recall
- R squared (R2)
- Root Mean Square Error (RMSE)
- Mean Absolute Error (MAE)
- Pearson correlation coefficient (PCC)

**Calculation**: Metrics are calculated based on model predictions relative to actual MIC values.

**Interpretation**: Recall reflects the model's ability to accurately predict AMPCliff pairs, with higher recall indicating better performance.

**Baseline Results**: Not explicitly mentioned.

**Validation**: Comparison between traditional ML models and LMs for AMPCliff prediction using the AC split strategy.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**
- **Fairness**

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
