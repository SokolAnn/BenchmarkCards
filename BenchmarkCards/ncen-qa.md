# NCEN-QA

## 📊 Benchmark Details

**Name**: NCEN-QA

**Overview**: NCEN-QA is a new dataset in finance for benchmarking question-answering tasks derived from N-CEN reports on funds. It serves as a robust platform for evaluating automatic workflow generation systems in handling question-answering tasks related to funds.

**Data Type**: question-answering pairs

**Domains**:
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://www.sec.gov/files/formn-cen.pdf)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of NCEN-QA is to evaluate workflow generation systems in finance, particularly for question-answering tasks using data from N-CEN reports.

**Target Audience**:
- ML Researchers
- Finance Professionals
- Industry Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Data is sourced from N-CEN reports filed by registered investment companies available on the public database Edgar from the U.S. Securities and Exchange Commission (SEC).

**Size**: 600 question-answer pairs

**Format**: N/A

**Annotation**: Manually created question-answer pairs based on information extracted from N-CEN reports.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated by comparing generated answers to ground truth, with specific criteria for entity names and numerical values.

**Interpretation**: Higher accuracy indicates better performance in generating correct answers to the posed questions.

**Baseline Results**: The proposed methods significantly outperformed baseline methods like GPT-Context-Retrieval.

**Validation**: Performance is validated through thorough experiments against standard methodologies and ablation studies on the dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: FlowMind ensures that LLMs do not directly interact with proprietary data, thus protecting data integrity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
