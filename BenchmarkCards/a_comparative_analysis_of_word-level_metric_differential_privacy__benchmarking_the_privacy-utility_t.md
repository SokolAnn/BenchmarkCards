# A Comparative Analysis of Word-Level Metric Differential Privacy: Benchmarking The Privacy-Utility Trade-off

## 📊 Benchmark Details

**Name**: A Comparative Analysis of Word-Level Metric Differential Privacy: Benchmarking The Privacy-Utility Trade-off

**Overview**: This work conducts a comparative analysis of seven different word-level Differential Privacy (DP) algorithms on two NLP tasks, focusing on the privacy-utility trade-off and establishing a benchmark for evaluating these methods.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/sjmeis/MLDP)

## 🎯 Purpose and Intended Users

**Goal**: To provide a uniform and fair evaluation for word-level Metric Local Differential Privacy (MLDP) methods.

**Target Audience**:
- Researchers
- Practitioners

**Tasks**:
- Sentiment Analysis
- Topic Classification

**Limitations**: The choice of datasets and the specific experimental parameters may limit generalizability.

## 💾 Data

**Source**: IMDb Movie Review Dataset and AG News Dataset

**Size**: 50,000 reviews in total for IMDb; 130,000 articles in total for AG News

**Format**: N/A

**Annotation**: Manual labeling of sentiment in IMDb, category labeling in AG News

## 🔬 Methodology

**Methods**:
- Comparative analysis
- Algorithm testing
- Baseline comparison

**Metrics**:
- Accuracy
- Plausible Deniability (PD)
- Perturbation Percentage (PP)
- Cosine Similarity (CS)
- Least-Occurring Words (LOW)

**Calculation**: Metrics were calculated based on performance against a set of baselines, using statistical methods to analyze the trade-offs between privacy and utility.

**Interpretation**: A higher accuracy signifies better model performance, while lower values in privacy metrics indicate better privacy guarantees.

**Baseline Results**: Baseline accuracy for sentiment analysis was reported as 84.75 and for topic classification 73.63.

**Validation**: Results were validated through multiple runs and statistical comparisons against baselines.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The study emphasizes the importance of privacy-preserving techniques to safeguard sensitive information processed through text data.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
