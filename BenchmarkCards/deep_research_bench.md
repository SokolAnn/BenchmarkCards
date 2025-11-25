# Deep Research Bench

## 📊 Benchmark Details

**Name**: Deep Research Bench

**Overview**: Deep Research Bench is a benchmark designed to evaluate LLM agents on complex web research tasks reflecting real-world problems faced by analysts in various industries. It provides a controlled testing environment with a large frozen set of scraped web pages, enabling reliable evaluations over time.

**Data Type**: task instances

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- GAIA

**Resources**:
- [Resource](https://drb.futuresearch.ai/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capabilities of large language models (LLMs) on real-world web research tasks through a benchmark framework.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Find Number
- Find Dataset
- Find Original Source
- Validate Claim
- Derive Number
- Gather Evidence
- Populate Reference Class
- Compile Dataset

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from web research tasks reflecting real-world use cases.

**Size**: 89 instances

**Format**: N/A

**Annotation**: Answers carefully verified by skilled humans.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Binary score
- Precision
- Recall
- F1 Score

**Calculation**: Scores are calculated based on specific criteria for each task type, including success criteria and consistency with ground truth.

**Interpretation**: Scores reflect how well models perform on tasks against established criteria based on human assessments and automated evaluations.

**Baseline Results**: N/A

**Validation**: Continuous updates and evaluations as new models are released.

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

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
