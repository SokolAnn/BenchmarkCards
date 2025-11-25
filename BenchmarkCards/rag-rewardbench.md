# RAG-RewardBench

## 📊 Benchmark Details

**Name**: RAG-RewardBench

**Overview**: RAG-RewardBench is the first benchmark for evaluating reward models in Retrieval Augmented Generation (RAG) settings, designed to assess alignment with human preferences through 1,485 high-quality preference pairs.

**Data Type**: preference pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RewardBench

**Resources**:
- [Resource](https://huggingface.co/datasets/jinzhuoran/RAG-RewardBench/)
- [GitHub Repository](https://github.com/jinzhuoran/RAG-RewardBench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for reward models in RAG scenarios to enhance preference alignment for retrieval augmented language models.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Preference Alignment
- Multi-hop Reasoning
- Citation Accuracy
- Conflict Robustness

**Limitations**: N/A

## 💾 Data

**Source**: 18 datasets from various domains using multiple retrievers to ensure diversity.

**Size**: 1,485 preference pairs

**Format**: JSON

**Annotation**: Preference judgments are based on evaluations performed by LLMs as judges, reflecting human annotations.

## 🔬 Methodology

**Methods**:
- LLM-as-a-judge
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on a standard evaluation framework contrasting chosen versus rejected responses.

**Interpretation**: An accuracy score of over 50% indicates a model's ability to select better responses.

**Baseline Results**: The best-performing model achieved 78.3% accuracy on RAG-RewardBench.

**Validation**: Validation procedures included correlation checks between model evaluations and human annotations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
