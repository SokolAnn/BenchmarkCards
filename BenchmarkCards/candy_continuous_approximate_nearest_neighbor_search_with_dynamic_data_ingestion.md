# CANDY (Continuous Approximate Nearest Neighbor Search with Dynamic Data Ingestion)

## 📊 Benchmark Details

**Name**: CANDY (Continuous Approximate Nearest Neighbor Search with Dynamic Data Ingestion)

**Overview**: CANDY is a benchmark for evaluating Continuous Approximate K Nearest Neighbor (AKNN) algorithms under conditions of dynamic data ingestion. It addresses the limitations of existing benchmarks by assessing both retrieval effectiveness and update efficiency in dynamic environments.

**Data Type**: text, image, audio

**Domains**:
- Natural Language Processing
- Computer Vision
- Audio

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/intellistream/candy)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for AKNN algorithms that operate under continuous data ingestion, assessing their adaptability and performance in dynamic scenarios.

**Target Audience**:
- ML Researchers
- Data Scientists
- Software Developers

**Tasks**:
- Approximate Nearest Neighbor Search

**Limitations**: CANDY is limited to single-threaded, in-memory, and CPU-only conditions and does not yet leverage advancements such as SSDs or GPUs.

## 💾 Data

**Source**: Real-world and synthetic datasets including Glove, SIFT, Msong, Sun, DPR, Trevi, and WTE.

**Size**: 50,000 vectors initially loaded; 50,000 new vectors ingested at 4,000 rows/second

**Format**: Vector representations, compatible with LibTorch and PyTorch

**Annotation**: Data simulated based on controlled environment conditions for dynamic data ingestion.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Performance evaluations

**Metrics**:
- Query recall
- Query latency

**Calculation**: Recall is calculated as the proportion of true nearest neighbors correctly identified, while latency measures the time from query submission to result return.

**Interpretation**: Higher recall indicates better retrieval accuracy, and lower latency corresponds to faster performance.

**Baseline Results**: Comparative performance against existing static benchmarks.

**Validation**: Extensive evaluations performed across multiple datasets under varying conditions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
