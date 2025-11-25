# SOS-BENCH (Substance Outweighs Style Benchmark)

## 📊 Benchmark Details

**Name**: SOS-BENCH (Substance Outweighs Style Benchmark)

**Overview**: The largest standardized, reproducible LLM meta-benchmark to gauge progress on alignment with helpful, honest, harmless (HHH) principles. It combines 19 existing world knowledge, instruction following, and safety benchmarks for a holistic view of model performance.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MT-Bench
- Alpaca Eval
- Arena-Hard-Auto

**Resources**:
- [GitHub Repository](https://github.com/penfever/sos-bench)

## 🎯 Purpose and Intended Users

**Goal**: To introduce a new alignment benchmark with ground truth, designed to measure progress on alignment metrics.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Alignment Evaluation
- Safety Assessment
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: SOS-BENCH combines multiple existing benchmarks for evaluation.

**Size**: 152,380 data points

**Format**: N/A

**Annotation**: Ground truth answers are provided for questions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Accuracy

**Calculation**: Aggregates are reported using the average of normalized accuracies, with 95% confidence intervals.

**Interpretation**: Higher performance in terms of HHH principles indicates better alignment.

**Validation**: The benchmark validates its methods through large-scale comparisons with other benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: Potential harms from implicit biases in LLM-judges.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
