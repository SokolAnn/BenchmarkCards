# TIME (Temporal Reasoning Benchmark)

## 📊 Benchmark Details

**Name**: TIME (Temporal Reasoning Benchmark)

**Overview**: TIME is a multi-level benchmark designed for evaluating temporal reasoning in real-world scenarios, consisting of 38,522 QA pairs across three datasets: TIME-WIKI, TIME-NEWS, and TIME-DIAL, each containing multiple tasks focusing on different aspects of temporal reasoning.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TimeBench
- TRAM

**Resources**:
- [GitHub Repository](https://github.com/sylvain-wei/TIME)
- [Resource](https://huggingface.co/datasets/SylvainWei/TIME)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation framework for assessing the temporal reasoning capabilities of large language models across different real-world scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Temporal Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Various datasets including Wikidata, news articles, and multi-session dialogues

**Size**: 38,522 question-answer pairs

**Format**: N/A

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Exact Match (EM)
- F1 Score

**Calculation**: Metrics are calculated based on lexical overlap and exact matches between predicted and ground truth answers.

**Interpretation**: Higher F1 scores indicate better performance in temporal reasoning tasks, with specific thresholds for categorizing performance.

**Validation**: Extensive experiments conducted on 24 models to validate the benchmark.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The benchmark utilizes anonymized data sourced from Wikidata, reducing privacy risks but still needing oversight.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
