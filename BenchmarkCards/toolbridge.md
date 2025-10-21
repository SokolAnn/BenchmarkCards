# ToolBridge

## 📊 Benchmark Details

**Name**: ToolBridge

**Overview**: ToolBridge proposes a pipeline for the large-scale creation of datasets designed to train LLMs in leveraging external tools. The collection of over 178,000 yielded data entries, named ToolBridge, will be open-sourced to the community, marking a significant advancement in the transparency and accessibility of the data for training large language models to leverage external tools.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- ToolQA

**Resources**:
- [GitHub Repository](https://github.com/CharlesPikachu/ToolBridge)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of ToolBridge is to create a publicly available benchmark dataset for training LLMs to utilize external tools effectively.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Various open-access datasets aggregated from the community to facilitate LLMs' utilization of external tools.

**Size**: 178,023 entries

**Format**: N/A

**Annotation**: Automatically generated through a pipeline process.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the performance improvements on standard benchmarks after supervised fine-tuning on ToolBridge.

**Interpretation**: Models demonstrated significant enhancements in their ability to utilize external tools after training on ToolBridge.

**Validation**: Performance evaluated against standard benchmarks such as GSM 8k, GSM Plus, and MathBench.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Exposing personal information

**Demographic Analysis**: N/A

**Potential Harm**: ToolBridge aims to minimize inaccuracies in LLM outputs by training them to utilize external tools effectively.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
