# Visual Number Benchmark (VisNumBench)

## 📊 Benchmark Details

**Name**: Visual Number Benchmark (VisNumBench)

**Overview**: VisNumBench evaluates the number sense abilities of Multimodal Large Language Models (MLLMs) across a wide range of visual numerical tasks, comprising about 1,900 multiple-choice question-answer pairs derived from both synthetic and real-world visual data.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [Resource](https://wwwtttjjj.github.io/VisNumBench/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the intuitive numerical abilities of MLLMs across various visual numerical tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Numerical Reasoning
- Visual Understanding

**Limitations**: Limited performance of even the best MLLMs compared to human levels.

## 💾 Data

**Source**: Images from existing datasets, captured by authors, and generated using a Python program.

**Size**: 1,900 question-answer pairs

**Format**: JSON

**Annotation**: Manually designed question-answer pairs based on visual attributes.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the percentage of correctly answered questions out of the total.

**Interpretation**: Higher accuracy reflects better number sense abilities of MLLMs.

**Baseline Results**: Humans achieved 95.33% average accuracy on the benchmark.

**Validation**: Evaluated 17 MLLMs across two datasets (synthetic and real).

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
