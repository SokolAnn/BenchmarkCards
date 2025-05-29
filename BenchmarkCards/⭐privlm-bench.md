# PrivLM-Bench

## 📊 Benchmark Details

**Name**: PrivLM-Bench

**Overview**: PrivLM-Bench is a multi-perspective privacy evaluation benchmark for language models (LMs), designed to quantify privacy leakage without ignoring inference data privacy. It defines multifaceted privacy objectives and utilizes a unified pipeline for private fine-tuning while performing privacy attacks to evaluate existing privacy-preserving language models (PPLMs).

**Data Type**: Text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/HKUST-KnowComp/PrivLM-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To empirically and intuitively evaluate the privacy leakage of language models.

**Target Audience**:
- Researchers in natural language processing
- Developers of privacy-preserving language models
- Data scientists

**Tasks**:
- Evaluate privacy performance of PPLMs
- Conduct comparative studies on LMs
- Verify PPLM implementations

**Limitations**: None

## 💾 Data

**Source**: GLUE benchmark datasets

**Size**: Three datasets: MNLI, SST2, QNLI

**Format**: Text classification tasks

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Full fine-tuning
- Prompt tuning
- Prefix tuning
- Infilling

**Metrics**:
- Accuracy
- Area Under Curve (AUC)
- True Positive Rate (TPR)
- Micro-level Precision
- Recall
- F1 Score

**Calculation**: Empirical evaluations based on privacy attack effectiveness

**Interpretation**: Attack performance is used as a metric for privacy leakage.

**Validation**: Comparison against baseline PPLMs and multiple tuning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Leakage
- Privacy Violations

**Atlas Risks**:
- **Privacy**: Personal information in data, Data privacy rights alignment
- **Accuracy**: Poor model accuracy
- **Governance**: Lack of system transparency

**Potential Harm**: Potential for privacy breaches through data extraction and inference attacks on sensitive personal data.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The research ensures that data used does not contain actual personal identifiable information and adheres to privacy laws.

**Data Licensing**: Not Applicable

**Consent Procedures**: The paper ensures that no identifiable personal data is used without consent.

**Compliance With Regulations**: The study adheres to EU GDPR and CCPA guidelines.
