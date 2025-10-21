# StructText: A Synthetic Table-to-Text Approach for Benchmark Generation with Multi-Dimensional Evaluation

## 📊 Benchmark Details

**Name**: StructText: A Synthetic Table-to-Text Approach for Benchmark Generation with Multi-Dimensional Evaluation

**Overview**: StructText is an end-to-end framework for automatically generating high-fidelity benchmarks for key-value extraction from text using existing tabular data, facilitating text-to-table extraction research and evaluation.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance
- Healthcare
- Legal

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/ibm-research/struct-text)
- [GitHub Repository](https://github.com/ibm/struct-text)

## 🎯 Purpose and Intended Users

**Goal**: To generate and evaluate benchmarks for text-to-table extraction tasks using synthetic generated texts from existing tabular data.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Text-to-Table Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic text generated from tabular data

**Size**: 71,539 examples

**Format**: JSON

**Annotation**: Automatically generated

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Precision
- Recall
- F1 Score
- Factuality
- Hallucination
- Coherence

**Calculation**: Metrics are calculated from the performance of extraction coupled with LLM as judge assessments across different dimensions.

**Interpretation**: Scores measure how accurately the models can generate and extract information while maintaining coherence and factual consistency.

**Baseline Results**: Precision for SEC Financial dataset is 0.344; Recall is 0.669; F1 Score is 0.455.

**Validation**: The benchmark was validated through extensive evaluation of generated reports and numerical and temporal accuracy assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: N/A - Not discussed

**Data Licensing**: Creative Commons BY-NC-ND 4.0 International License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
