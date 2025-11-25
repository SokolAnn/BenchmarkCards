# MemoryAgentBench

## 📊 Benchmark Details

**Name**: MemoryAgentBench

**Overview**: MemoryAgentBench is a unified benchmark specifically designed to evaluate memory agents across four core competencies: accurate retrieval, test-time learning, long-range understanding, and selective forgetting. The benchmark includes transformed existing long-context datasets and newly constructed datasets to simulate multi-turn interactions.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- GAIA
- SWE-Bench
- LOCOMO
- LongMemEval

**Resources**:
- [GitHub Repository](https://github.com/username/repository)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing memory agents and their capabilities in memory management.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Accurate Retrieval
- Test-Time Learning
- Long-Range Understanding
- Selective Forgetting

**Limitations**: N/A

## 💾 Data

**Source**: Reconstructed from existing long-context datasets and newly created datasets.

**Size**: 534K examples (total across all tasks)

**Format**: JSON

**Annotation**: Automated generation and processing of datasets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Recall@5

**Calculation**: Metrics are calculated based on the performance of memory agents against the provided tasks.

**Interpretation**: Higher scores indicate better performance in memory capabilities across evaluated tasks.

**Baseline Results**: Performance against standard LLMs and existing benchmarks.

**Validation**: Benchmark evaluated through multiple interactions with varied agent architectures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Data poisoning

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
