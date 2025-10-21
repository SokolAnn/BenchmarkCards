# GenoTEX

## 📊 Benchmark Details

**Name**: GenoTEX

**Overview**: GenoTEX provides a benchmark dataset for the automated analysis of gene expression data focused on gene-trait association problems. It includes analysis code and results, expert-curated annotations, and a standardized analysis pipeline.

**Data Type**: gene expression data

**Domains**:
- Healthcare
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Liu-Hy/GenoTEX)

## 🎯 Purpose and Intended Users

**Goal**: To support the evaluation and development of automated methods for gene expression data analysis using LLM-based agents.

**Target Audience**:
- Bioinformaticians
- ML Researchers

**Tasks**:
- Gene-trait Association Analysis
- Data Preprocessing
- Statistical Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Gene Expression Omnibus (GEO) and The Cancer Genome Atlas (TCGA)

**Size**: 41.5 GB

**Format**: CSV, JSON

**Annotation**: Manually annotated by bioinformaticians

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Accuracy
- Area Under Receiver Operating Characteristic curve (AUROC)

**Calculation**: Metrics are calculated as described in the methodology section of the paper.

**Interpretation**: The performance metrics indicate the effectiveness of different automated methods on the benchmark tasks.

**Baseline Results**: GenoAgent achieved an AUROC score of 0.74, while human expert performance was at 0.89.

**Validation**: Evaluation through metrics defined for dataset filtering, preprocessing, and statistical analysis.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Data poisoning, Evasion attack
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is processed to avoid personally identifiable information.

**Data Licensing**: CC BY 4.0 (Creative Commons Attribution 4.0 International License)

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
