# API-B LEND

## 📊 Benchmark Details

**Name**: API-B LEND

**Overview**: API-B LEND is a large corpora for training and systematic testing of tool-augmented LLMs, curated from real-world datasets focusing on tasks such as API detection, slot filling, and sequencing.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolLLM
- API Bank
- ToolBench
- SeqToolQA
- ToolAlpaca

**Resources**:
- [GitHub Repository](https://github.com/IBM/API-BLEND)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse dataset for training and evaluating tool-augmented Language Learning Models (LLMs).

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- API Detection
- Slot Filling
- API Sequencing

**Limitations**: API-B LEND does not address environment interactions for an API agent and is currently focused on English API commands.

## 💾 Data

**Source**: Curated from five human-annotated datasets and LLM-assisted generation.

**Size**: 159,476 examples

**Format**: N/A

**Annotation**: Hybrid approach including human annotation and LLM-assisted generation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- F1 Score
- Precision
- Recall
- Longest Common Subsequence (LCS)

**Calculation**: F1 scores are calculated by comparing the predicted APIs with the gold ones and the predicted parameters of each API with its gold counterparts.

**Interpretation**: High F1 scores indicate better performance in detecting and parameterizing API calls.

**Baseline Results**: Models fine-tuned with API-B LEND dataset achieve better generalization performance compared to other tool-augmented LLMs.

**Validation**: Experiments include both in-distribution and out-of-distribution evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
