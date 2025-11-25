# STORY SUMM

## 📊 Benchmark Details

**Name**: STORY SUMM

**Overview**: A benchmark for evaluating methods of faithfulness in summarization, using LLM summaries of narrative stories with localized faithfulness labels and error explanations.

**Data Type**: story-summary pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/melaniesubbiah/storysumm)

## 🎯 Purpose and Intended Users

**Goal**: To improve evaluation methods for faithfulness in narrative summarization.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Short stories collected from Reddit subreddits: r/shortstories and r/shortscarystories.

**Size**: 96 story-summary pairs

**Format**: N/A

**Annotation**: Annotations were provided by human annotators who labeled summaries as faithful/unfaithful.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Model-based evaluation

**Metrics**:
- Balanced accuracy

**Calculation**: Metrics are calculated by comparing human labels to model-generated labels across various protocols.

**Interpretation**: Good performance indicates high fidelity in the automatic evaluation of narrative summarization.

**Baseline Results**: No metric achieves more than 70% balanced accuracy.

**Validation**: Different annotation protocols were tested to find effective methods for evaluating faithfulness.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Misrepresentation of narrative content']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
