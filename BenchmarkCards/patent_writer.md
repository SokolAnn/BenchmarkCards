# PATENT WRITER

## 📊 Benchmark Details

**Name**: PATENT WRITER

**Overview**: PATENT WRITER is the first unified benchmarking framework for evaluating LLMs in patent abstract generation, assessing output quality through a comprehensive suite of metrics and application in downstream patent classification and retrieval tasks.

**Data Type**: claim-abstract pairs

**Domains**:
- Natural Language Processing
- Legal

**Languages**:
- English

**Resources**:
- [Resource](https://anonymous.4open.science/r/pwriter-A95C)
- [Resource](https://patentsview.org/download/data-download-tables)

## 🎯 Purpose and Intended Users

**Goal**: To provide a unified framework for benchmarking the capabilities of LLMs in patent abstract generation.

**Target Audience**:
- ML Researchers
- Domain Experts
- Patent Attorneys

**Tasks**:
- Patent Abstract Generation
- Patent Classification
- Patent Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: U.S. patents granted in 2022 from PatentsView, including claim-abstract pairs drawn from various CPC subclasses.

**Size**: Approximately 21,000 records

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics
- Robustness evaluation under input perturbations
- Qualitative analysis

**Metrics**:
- BLEU
- ROUGE
- BERTScore
- Accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics are calculated based on comparisons between generated patent abstracts and original texts.

**Interpretation**: Higher scores on NLP metrics indicate closer alignment with human-written abstracts.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
