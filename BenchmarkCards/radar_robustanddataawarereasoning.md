# Radar (RobustAndDataAwareReasoning)

## 📊 Benchmark Details

**Name**: Radar (RobustAndDataAwareReasoning)

**Overview**: Radar is a benchmark for systematically evaluating data-aware reasoning on tabular data. It focuses on the ability of language models to handle real-world data artifacts such as missing values, outliers, and inconsistencies, assessing their reasoning capabilities under various perturbations and table sizes.

**Data Type**: table query pairs

**Domains**:
- Natural Language Processing
- Healthcare
- Finance
- Education
- Sports
- Environmental Science

**Languages**:
- English

**Similar Benchmarks**:
- TableBench
- MightyTorr

**Resources**:
- [GitHub Repository](https://github.com/kenqgu/RADAR)
- [Resource](https://huggingface.co/datasets/kenqgu/RADAR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured evaluation framework that highlights language models' abilities to reason over imperfect tabular data.

**Target Audience**:
- ML Researchers
- AI Developers
- Data Scientists

**Tasks**:
- Tabular Reasoning
- Data Analysis
- Data Cleaning
- Error Detection

**Limitations**: N/A

## 💾 Data

**Source**: Crowdsourced from various domains, including education, health, and business, drawing on diverse datasets.

**Size**: 2980 table query pairs

**Format**: CSV, JSON

**Annotation**: Manually annotated by data science experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match Accuracy

**Calculation**: Exact match is calculated based on the ability of the models to correctly respond to queries over perturbed tabular data.

**Interpretation**: Higher exact match scores indicate better performance in recognizing and reasoning about data artifacts.

**Baseline Results**: Performance varies by model; frontier models show significant performance drops on perturbed data compared to clean data.

**Validation**: Evaluated using a series of perturbations that simulate real-world data artifacts and by measuring performance across varying table sizes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets are sourced from various publicly available, licensed datasets.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
