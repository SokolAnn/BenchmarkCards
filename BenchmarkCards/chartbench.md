# ChartBench

## 📊 Benchmark Details

**Name**: ChartBench

**Overview**: ChartBench is a comprehensive benchmark designed to assess chart comprehension and data reliability through complex visual reasoning, including 42 categories, 66.6k charts, and 600k question-answer pairs.

**Data Type**: chart and question-answer pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ChartQA
- PlotQA
- OpenCQA
- Chart-to-text
- ChartX
- ChartLlama

**Resources**:
- [Resource](https://chartbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the chart comprehension abilities of Multimodal Large Language Models (MLLMs), focusing on their capability to reason visually without heavy reliance on data point annotations.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Chart Recognition
- Value Extraction
- Value Comparison
- Global Conception
- Number Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated and collected from sources such as Kaggle, anonymized for privacy, and created using various plotting methods and styles.

**Size**: 66,624 charts and 600,000 question-answer pairs

**Format**: JSON, CSV

**Annotation**: Predominantly unannotated charts requiring visual inference.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy
- Acc+
- CoR

**Calculation**: Acc+ measures MLLMs' performance through both positive and negative assertions, requiring correct judgment on visual logic; CoR determines the failure to utilize chart information effectively.

**Interpretation**: Higher accuracy indicates better comprehension of charts, while CoR measures susceptibility to random guessing in interpreting charts.

**Baseline Results**: Different models were compared on performance metrics, indicating varying capabilities of MLLMs in understanding charts, particularly unannotated ones.

**Validation**: Extensive experimental evaluations conducted on multiple models using the proposed benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Inaccurate data interpretation due to model biases and reliance on visual cues without annotations.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is anonymized during collection and processing to protect participant identities.

**Data Licensing**: Not Applicable

**Consent Procedures**: Obtained informed consent from participants involved in the study.

**Compliance With Regulations**: Not Applicable
