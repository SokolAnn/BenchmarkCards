# STEER-ME

## 📊 Benchmark Details

**Name**: STEER-ME

**Overview**: STEER-ME is a benchmark for assessing the microeconomic reasoning of large language models, focusing on non-strategic economic tasks such as supply and demand analysis.

**Data Type**: multiple-choice questions

**Domains**:
- Economics

**Languages**:
- English

**Similar Benchmarks**:
- STEER

**Resources**:
- [Resource](https://steer-benchmark.cs.ubc.ca)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the economic reasoning ability of large language models in non-strategic settings across a variety of microeconomic problems.

**Target Audience**:
- ML Researchers
- Economists
- Policy Analysts

**Tasks**:
- Economic Reasoning
- Market Analysis
- Decision Making

**Limitations**: N/A

## 💾 Data

**Source**: Created using a novel LLM-assisted data generation protocol called auto-STEER, which adapts handwritten templates into multiple economic contexts.

**Size**: 21,000 test questions

**Format**: N/A

**Annotation**: Manually validated 500 generations per element.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Normalized accuracy
- Exact-Match accuracy
- Precision
- Recall
- F1 Score

**Calculation**: Metrics calculated as averages over all questions in each element.

**Interpretation**: An LLM's score on an element reflects its performance on questions that assess economic reasoning.

**Baseline Results**: N/A

**Validation**: A total of 27 LLMs were evaluated using different metrics across various economic tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
