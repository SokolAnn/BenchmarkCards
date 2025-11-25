# RepoBugs

## 📊 Benchmark Details

**Name**: RepoBugs

**Overview**: RepoBugs is a new benchmark comprising 124 typical repository-level bugs from open-source repositories designed specifically for evaluating repository-level automatic program repair tasks.

**Data Type**: bug-fixing pairs

**Domains**:
- Software Engineering

**Languages**:
- Python

**Similar Benchmarks**:
- QuixBugs
- Defects4J

**Resources**:
- [Resource](https://doi.org/10.1145/3639478.3647633)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of LLMs on repository-level automatic program repair tasks.

**Target Audience**:
- Researchers in Software Engineering
- ML Researchers

**Tasks**:
- Automatic Program Repair

**Limitations**: N/A

## 💾 Data

**Source**: Crawled open-source Python repositories from GitHub, manually crafted by experts.

**Size**: 124 bugs

**Format**: N/A

**Annotation**: Manual disruption by experts

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Repair rate
- Correct format
- Correct repair
- Correct explanation

**Calculation**: Manual evaluation of repair success based on criteria.

**Interpretation**: High repair rates indicate effective context extraction and model performance.

**Baseline Results**: Repair rate of preliminary method for GPT-3.5 was 22.58%.

**Validation**: Evaluation results provided by experts with programming experience.

## ⚠️ Targeted Risks

**Risk Categories**:
- Performance
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
