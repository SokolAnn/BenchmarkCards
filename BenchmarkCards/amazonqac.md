# AmazonQAC

## 📊 Benchmark Details

**Name**: AmazonQAC

**Overview**: AmazonQAC is a new QAC (Query Autocomplete) dataset collected from Amazon Search logs containing 395M samples of actual sequences of user-typed prefixes leading to final search terms, designed to facilitate research on QAC systems.

**Data Type**: prefix strings leading to final search terms

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/amazon/AmazonQAC)

## 🎯 Purpose and Intended Users

**Goal**: To address the critical need for realistic, large-scale datasets for Query Autocomplete (QAC) and to prompt further research in QAC systems.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Query Autocomplete

**Limitations**: N/A

## 💾 Data

**Source**: Collected from Amazon Search autocomplete customer logs in the U.S.

**Size**: 395,550,004 samples

**Format**: N/A

**Annotation**: Data has been scrapped for personally identifiable information using regex.

## 🔬 Methodology

**Methods**:
- Information Retrieval
- Large Language Models

**Metrics**:
- Success@10
- Mean Reciprocal Rank (MRR)

**Calculation**: Success@10 is calculated by considering whether the final search term is included in the top 10 suggestions provided by the QAC system.

**Interpretation**: Higher values of Success@10 and MRR indicate better performance of the QAC system in providing accurate search term suggestions.

**Baseline Results**: Finetuned LLM achieved a Success@10 of 37.0%; upperbound is 69.8%.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment

**Demographic Analysis**: N/A

**Potential Harm**: Models and results derived from AmazonQAC should be assumed to inherit cultural and linguistic biases of its source.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data has been scrubbed for personally identifiable information using various regex patterns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
