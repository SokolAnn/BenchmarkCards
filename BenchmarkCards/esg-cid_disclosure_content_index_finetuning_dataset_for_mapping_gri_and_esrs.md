# ESG-CID (Disclosure Content Index Finetuning Dataset for Mapping GRI and ESRS)

## 📊 Benchmark Details

**Name**: ESG-CID (Disclosure Content Index Finetuning Dataset for Mapping GRI and ESRS)

**Overview**: We create the ESG-Content Index Dataset (ESG-CID), a dataset leveraging disclosure content indices from ESG reports to facilitate research in the ESG domain and support the development of retrieval models for standardized ESG reporting.

**Data Type**: query-document pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- MMLU

**Resources**:
- [Resource](https://huggingface.co/datasets/airefinery/esg_cid_retrieval)

## 🎯 Purpose and Intended Users

**Goal**: To enhance ESG-specific retrieval systems.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Text Retrieval
- Information Extraction

**Limitations**: N/A

## 💾 Data

**Source**: Disclosures from sustainability and annual reports collected from various companies.

**Size**: 2,500 unique reports

**Format**: JSON

**Annotation**: Weakly supervised using disclosure content indices and refined with LLM assessments.

## 🔬 Methodology

**Methods**:
- Contrastive Learning
- Fine-tuning

**Metrics**:
- Recall@10
- Mean Reciprocal Rank at 50 (MRR@50)
- Mean Average Precision at 50 (MAP@50)

**Calculation**: Metrics are calculated based on the ranking of document pages rather than individual chunks due to the structure of the dataset.

**Interpretation**: Higher values in MRR@50 and MAP@50 indicate better retrieval of relevant document pages.

**Baseline Results**: Fine-tuned models outperform commercial embeddings and leading public models.

**Validation**: Tested under temporal data splits and cross-report style transfer.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
