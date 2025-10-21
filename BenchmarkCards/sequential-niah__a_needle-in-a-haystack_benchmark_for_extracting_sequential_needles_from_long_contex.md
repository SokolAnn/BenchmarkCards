# Sequential-NIAH: A Needle-In-A-Haystack Benchmark for Extracting Sequential Needles from Long Contexts

## 📊 Benchmark Details

**Name**: Sequential-NIAH: A Needle-In-A-Haystack Benchmark for Extracting Sequential Needles from Long Contexts

**Overview**: The Sequential-NIAH benchmark is designed to evaluate the capability of large language models (LLMs) to extract sequential information items, known as needles, from long contexts. It includes three needle generation pipelines: synthetic-temporal, real-temporal, and real-logical orders, with context lengths ranging from 8K to 128K, comprising 14,000 samples.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- ∞Bench
- L-Eval
- LongBench
- LongEval
- LooGLE
- Zero-SCROLLS
- FactGuard

**Resources**:
- [GitHub Repository](https://github.com/miraclefish/Sequential-NIAH-Benchmark.git)
- [Resource](https://huggingface.co/datasets/yuyijiong/LongData-Corpus)

## 🎯 Purpose and Intended Users

**Goal**: To assess LLMs' ability to retrieve sequential information from long contexts in realistic scenarios.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Information Retrieval

**Limitations**: Model evaluations may be biased by the dataset's domain, and unoptimized API parameters could affect performance and fairness.

## 💾 Data

**Source**: Synthetic and real data generated for LLM evaluation.

**Size**: 14,000 samples (10,000 for training, 2,000 for development, 2,000 for testing)

**Format**: CSV

**Annotation**: The data is annotated using an evaluation model trained on synthetic data.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the comparison of LLM-generated answers with ground truth answers.

**Interpretation**: Higher accuracy indicates better capability to extract and order retrieved information.

**Baseline Results**: The best model achieved a maximum accuracy of 63.50% on the test set.

**Validation**: The evaluation model achieved an accuracy of 99.49% in training on synthetic data.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
