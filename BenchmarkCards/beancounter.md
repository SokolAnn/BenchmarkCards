# BeanCounter

## 📊 Benchmark Details

**Name**: BeanCounter

**Overview**: BeanCounter is a public dataset consisting of more than 159B tokens extracted from businesses' disclosures, designed to provide a low-toxicity, high-quality source of domain-specific content for training large language models.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Finance

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/BeanCounter)

## 🎯 Purpose and Intended Users

**Goal**: To provide a large-scale, high-quality dataset for training language models that can improve performance in business-oriented NLP tasks while reducing toxicity.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Text Classification
- Named Entity Recognition
- Toxicity Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Extracted from public domain business disclosures via EDGAR.

**Size**: 159.4B tokens

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Toxicity Score

**Calculation**: Metrics were calculated based on model performance evaluations on domain-specific tasks and toxicity generation analysis.

**Interpretation**: Improved model performances indicate the effectiveness of the BeanCounter dataset in training multi-billion parameter models.

**Validation**: Evaluation procedures involved comparing models pre-trained on BeanCounter against their base models on specific tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The dataset includes personal identifiable information which is publicly available as per SEC regulations.

**Data Licensing**: Not Applicable

**Consent Procedures**: The entities have consented to make the information publicly available.

**Compliance With Regulations**: The dataset is compliant with SEC guidelines on public disclosure.
