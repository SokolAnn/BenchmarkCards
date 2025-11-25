# DermaGraph

## 📊 Benchmark Details

**Name**: DermaGraph

**Overview**: DermaGraph is a novel Graph-RAG dataset comprising diverse dermatological conditions, facilitating both multimodal and unimodal querying within the context of medical Visual Question Answering (VQA).

**Data Type**: multimodal

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To support scalable research in zero-shot multimodal medical applications via a comprehensive dataset designed for dermatological VQA tasks.

**Target Audience**:
- ML Researchers
- Medical Professionals

**Tasks**:
- Visual Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: A total of 50 common dermatological conditions sourced from the National Health Service (NHS) website, organized into a structured CSV format for graph-based retrieval.

**Size**: N/A

**Format**: CSV

**Annotation**: Manual curation and organization by domain experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics are computed based on the accuracy of the model's responses to the queries from the DermaGraph dataset.

**Interpretation**: Higher accuracy indicates better model performance in answering medical queries.

**Baseline Results**: BIND (FlanT5XXL) achieved a performance rate of 83.33% on the DermaGraph accuracy measure.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
