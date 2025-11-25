# tinyBenchmarks

## 📊 Benchmark Details

**Name**: tinyBenchmarks

**Overview**: tinyBenchmarks evaluates LLMs with a significantly reduced number of examples while maintaining reliable performance estimation. It releases tiny versions of existing benchmarks to address the high costs associated with evaluating LLMs.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU
- HELM
- Open LLM Leaderboard
- AlpacaEval

**Resources**:
- [GitHub Repository](https://github.com/felipemaiapolo/tinyBenchmarks)
- [Resource](https://huggingface.co/tinyBenchmarks)

## 🎯 Purpose and Intended Users

**Goal**: To provide an efficient evaluation method for LLMs using a smaller sample of examples from existing benchmarks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering
- Text Classification

**Limitations**: N/A

## 💾 Data

**Source**: Evaluation tools and datasets released for LLM benchmarking, derived from popular benchmarks.

**Size**: 100 examples per scenario

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Stratified random sampling
- Clustering based on correctness
- Item Response Theory (IRT)

**Metrics**:
- Accuracy

**Calculation**: Performance estimation based on the accuracy of LLMs evaluated on a subset of examples.

**Interpretation**: Estimations can be compared to true performance results for assessing the efficiency of methods.

**Baseline Results**: N/A

**Validation**: The efficacy of strategies is validated through comparisons with full benchmark evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
