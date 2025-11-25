# ICLEval

## 📊 Benchmark Details

**Name**: ICLEval

**Overview**: ICLEval is introduced to evaluate the in-context learning abilities of large language models (LLMs), encompassing exact copying and rule learning as its key sub-abilities, with a total of 12 evaluation tasks designed specifically for this purpose.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU (Massive Multitask Language Understanding)
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/RUCBM/ICLEval)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the in-context learning ability of large language models by measuring their capability in exact copying and rule learning.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Exact Copying
- Rule Learning

**Limitations**: N/A

## 💾 Data

**Source**: Various sources including Wikipedia, common noun vocabulary, GSM8K, AQuA, and generation context from ChatGPT.

**Size**: 2,040 examples

**Format**: text

**Annotation**: Curated from existing datasets and synthesized data.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Exact Match Score

**Calculation**: Exact match score for evaluating model predictions against the correct labels as described for each task.

**Interpretation**: Higher scores indicate better performance in correctly executing in-context learning tasks as defined in the benchmark.

**Baseline Results**: N/A

**Validation**: Experimentally validated through various large language models across different scales.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Harmful outputs due to data bias in training models.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
