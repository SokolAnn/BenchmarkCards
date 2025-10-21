# PLUGH

## 📊 Benchmark Details

**Name**: PLUGH

**Overview**: PLUGH is a benchmark designed to evaluate spatial understanding and reasoning capabilities of Large Language Models (LLMs) through five distinct tasks based on fictional texts.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/altsoph/PLUGH)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the spatial reasoning capabilities of Large Language Models using a formalized set of tasks derived from narrative texts.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Graph Reconstruction
- Character’s Path Reconstruction
- Reversed Character’s Path Reconstruction
- Novel Shortest Path
- Temporal Hinted Shortest Path

**Limitations**: N/A

## 💾 Data

**Source**: Data extracted from 48 different games, comprising 5 tasks with 125 input texts representing 61 different spatial graphs.

**Size**: 125 examples

**Format**: JSON

**Annotation**: Automatically generated from game transcripts and processed using LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- F1 Score
- Normalized Levenshtein distance

**Calculation**: Metrics calculated based on model output comparison with ground truth annotations.

**Interpretation**: Higher F1 scores indicate better performance, while lower normalized Levenshtein distance signifies closer matches to expected paths or graphs.

**Baseline Results**: Results across various models are provided, demonstrating performance variability.

**Validation**: Data validation included checks for location presence in generated text and duplicates in graphs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
