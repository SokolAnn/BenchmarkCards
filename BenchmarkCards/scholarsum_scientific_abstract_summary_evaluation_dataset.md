# ScholarSum (Scientific abstract summary evaluation Dataset)

## 📊 Benchmark Details

**Name**: ScholarSum (Scientific abstract summary evaluation Dataset)

**Overview**: ScholarSum is a meta-evaluation benchmark designed specifically for scholarly summaries, consisting of thousands of human-annotated abstracts from diverse academic domains. It provides a comprehensive dataset for assessing automatic evaluation metrics and measuring the correlation between these metrics and human judgments.

**Data Type**: academic abstracts with facet-level annotations

**Domains**:
- Natural Language Processing
- Computer Science
- Biomedical

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/iriscxy/ScholarSum)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate scholarly summaries and inspire the development of better evaluation metrics for automatic summarization systems.

**Target Audience**:
- ML Researchers
- Domain Experts
- Model Developers

**Tasks**:
- Text Summarization Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from PubMed and arXiv.

**Size**: Thousands of annotations for hundreds of abstracts

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Human evaluation
- Facet-aware metric evaluation using LLMs

**Metrics**:
- Facet-aware Metric (FM)

**Calculation**: Scores are computed based on the weights assigned to different facets of the abstracts.

**Interpretation**: Scores reflect how well the generated summary aligns with the original abstract across different facets.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias, Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Creative Commons (CC) license

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
