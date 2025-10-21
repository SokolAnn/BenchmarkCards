# MAPEX: A Multi-Agent Pipeline for Keyphrase Extraction

## 📊 Benchmark Details

**Name**: MAPEX: A Multi-Agent Pipeline for Keyphrase Extraction

**Overview**: MAPEX introduces a multi-agent pipeline for keyphrase extraction that coordinates LLM-based agents through multiple modules to enhance the extraction quality, adapting dynamically to document lengths.

**Data Type**: keyphrase extraction data

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- Inspec
- SemEval2010
- SemEval2017
- DUC2001
- NUS
- Krapivin

**Resources**:
- [GitHub Repository](https://github.com/NKU-LITI/MAPEX)

## 🎯 Purpose and Intended Users

**Goal**: To improve the performance of keyphrase extraction through multi-agent collaboration and a dual-path strategy based on document length.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Keyphrase Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Inspec, SemEval-2010, SemEval-2017, DUC2001, NUS, Krapivin datasets.

**Size**: 1,971 documents

**Format**: N/A

**Annotation**: Manual annotation by domain experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 score calculated using precision and recall metrics based on the predicted and actual keyphrases.

**Interpretation**: Higher F1 score indicates better performance in capturing relevant keyphrases.

**Baseline Results**: State-of-the-art unsupervised method was 22.81% F1@5.

**Validation**: Validated through extensive experiments on benchmark datasets.

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
