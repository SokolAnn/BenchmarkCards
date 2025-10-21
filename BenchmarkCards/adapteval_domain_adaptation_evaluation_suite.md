# AdaptEval (Domain Adaptation Evaluation Suite)

## 📊 Benchmark Details

**Name**: AdaptEval (Domain Adaptation Evaluation Suite)

**Overview**: AdaptEval includes a domain benchmark and a set of metrics to facilitate the analysis of domain adaptation abilities of Large Language Models on the summarization task across various domains.

**Data Type**: summarization datasets

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/meta-llama/Llama-2-7b-arxiv-4096)
- [Resource](https://huggingface.co/meta-llama/Llama-2-13b-arxiv-4096)
- [Resource](https://huggingface.co/mistralai/Mistral-7B-v0.1)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the domain adaptation abilities of Large Language Models across scientific, medical, and governmental domains using a set of adapted evaluation metrics.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Summarization

**Limitations**: N/A

## 💾 Data

**Source**: Data from arXiv, PubMed, and GovReport datasets.

**Size**: 360,000 examples

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- ROUGE
- BERTScore
- Domain Vocabulary Overlap (DVO)
- Domain Token Distribution Shift

**Calculation**: Metrics are computed based on generated outputs compared to reference summaries and domain-specific vocabulary.

**Interpretation**: Higher scores in ROUGE and BERTScore indicate better summarization quality, while DVO and token distribution shift metrics assess domain adaptation.

**Baseline Results**: N/A

**Validation**: Models validated through performance across various domains.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

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
