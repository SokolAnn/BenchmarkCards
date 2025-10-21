# LFPBench

## 📊 Benchmark Details

**Name**: LFPBench

**Overview**: LFPBench is the first benchmark dataset for validating the legal fact prediction (LFP) task and its application in legal judgment prediction (LJP). It contains evidence items, legal facts, and judgment outcomes collected from 657 first-instance litigation cases in China, covering 10 different types of civil cases.

**Data Type**: evidence items and legal facts

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese

**Resources**:
- [GitHub Repository](https://github.com/HPRCEST/LFPBench)

## 🎯 Purpose and Intended Users

**Goal**: To automate the prediction of legal facts for the subsequent legal judgment prediction (LJP) task.

**Target Audience**:
- Legal Researchers
- Natural Language Processing Researchers

**Tasks**:
- Legal Fact Prediction
- Legal Judgment Prediction

**Limitations**: The evidence information in LFPBench may be summarized and lack details, making it challenging to predict legal facts. The dataset does not cover criminal or administrative litigation cases.

## 💾 Data

**Source**: The data was extracted from judicial judgments in China using publicly available documents from the China Judgments Online database.

**Size**: 657 cases

**Format**: N/A

**Annotation**: Manually annotated by legal experts and students.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics were calculated based on the predictions of legal judgments from evidence using the LFP and LJP systems.

**Interpretation**: The results indicate the effectiveness of LFP in reducing accuracy drops in evidence-based LJP compared to fact-based LJP.

**Validation**: The dataset was validated by comparing model predictions against ground-truth legal judgments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**

**Demographic Analysis**: N/A

**Potential Harm**: Judicial datasets may inadvertently perpetuate biases present in historical legal decisions.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All sensitive information has been anonymized to protect personal privacy.

**Data Licensing**: The dataset uses publicly accessible legal documents, complying with copyright regulations.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
