# CogniLoad

## 📊 Benchmark Details

**Name**: CogniLoad

**Overview**: CogniLoad is a novel synthetic benchmark grounded in Cognitive Load Theory (CLT) that generates natural language logic puzzles with tunable parameters to facilitate precise failure analysis and understanding of long-context reasoning in Large Language Models (LLMs).

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- LongBench
- L-Eval
- LogicBench
- BABILong

**Resources**:
- [Resource](https://huggingface.co/datasets/cogniloadteam/cogniload)
- [Resource](https://anonymous.4open.science/r/cogniload-292B/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a multi-dimensional evaluation framework for long-context reasoning in LLMs by independently controlling parameters affecting intrinsic and extraneous cognitive loads.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Logical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Generated synthetic puzzles based on Cognitive Load Theory.

**Size**: 14,000 puzzle instances per LLM configuration

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated as the proportion of correctly answered puzzles out of the total number of puzzles evaluated.

**Interpretation**: A higher accuracy indicates better reasoning capability of the model across different parameters of cognitive load.

**Validation**: Features systematic, factorial control over cognitive load dimensions.

## ⚠️ Targeted Risks

**Risk Categories**:
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
