# Defects4Log

## 📊 Benchmark Details

**Name**: Defects4Log

**Overview**: Defects4Log is a benchmark for evaluating large language models (LLMs) in detecting logging code defects, containing 164 developer-verified real-world logging defects categorized into seven defect patterns.

**Data Type**: logging code defect instances

**Domains**:
- Software Engineering

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/klsc749/Defects4Log)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation dataset for testing the effectiveness of large language models in detecting logging code defects.

**Target Audience**:
- ML Researchers
- Software Engineers

**Tasks**:
- Defect Detection

**Limitations**: N/A

## 💾 Data

**Source**: Derived from multiple open-source Java projects including Hadoop, HBase, Hive, Yarn, and ActiveMQ, along with issue reports and literature reviews.

**Size**: 164 instances

**Format**: N/A

**Annotation**: Developer-verified defects categorized according to a derived taxonomy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Manual evaluation

**Metrics**:
- Accuracy

**Calculation**: The detection task is formulated as a multi-class classification problem, with accuracy computed based on the correct identification of defect patterns.

**Interpretation**: Higher accuracy indicates better performance by the LLMs in detecting and reasoning about logging code defects.

**Baseline Results**: Deepseek-R1 achieved an average accuracy of 47.6% under optimal prompting settings.

**Validation**: Results were validated through comprehensive analysis and manual verification by the authors.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
