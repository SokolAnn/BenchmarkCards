# Multi-Task Spatial Evaluation Dataset

## 📊 Benchmark Details

**Name**: Multi-Task Spatial Evaluation Dataset

**Overview**: This study introduces a novel multi-task spatial evaluation dataset, designed to systematically explore and compare the performance of several advanced models on spatial tasks, encompassing twelve distinct task types including spatial understanding and simple route planning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Geographic Information Systems

**Languages**:
- English

**Similar Benchmarks**:
- C-Eval
- AGIEval
- SuperCLUE
- MMLU
- GRASP
- STBench
- CityBench

**Resources**:
- [Resource](https://figshare.com/s/be55522f22bf761cfcab)

## 🎯 Purpose and Intended Users

**Goal**: To address the gap in evaluating large language models on spatial tasks by proposing a comprehensive dataset and evaluation framework for performance comparison.

**Target Audience**:
- ML Researchers
- GIS Practitioners
- Model Developers

**Tasks**:
- Spatial Understanding
- Simple Route Planning
- Geographic Literacy
- GIS Concepts
- NL2API Mapping
- Numerical Trajectory Recognition
- Toponymic Identification
- Code Explanation
- Code Generation
- Code Translation

**Limitations**: The spatial task categories used are not comprehensive and primarily focus on text-based spatial tasks, not including multimodal elements.

## 💾 Data

**Source**: The dataset integrates data from publicly available datasets, GIS textbooks, and Wikipedia knowledge snippets, with expert validation.

**Size**: 900 questions

**Format**: N/A

**Annotation**: Expert validation and question design, involving six GIS experts.

## 🔬 Methodology

**Methods**:
- Zero-shot testing
- Prompt tuning tests
- Human review of answers

**Metrics**:
- Weighted Accuracy (WA)

**Calculation**: Weighted Accuracy (WA) is calculated using the formula: WA = 2·n(s2) + 1·n(s1) / 2·(n(s0) + n(s1) + n(s2))

**Interpretation**: Higher WA indicates better performance in handling spatial tasks.

**Baseline Results**: gpt-4o achieved 71.3% WA, while gpt-3.5-turbo had a WA of 43.8%.

**Validation**: Applied comprehensive evaluation strategies with detailed scoring mechanisms.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
