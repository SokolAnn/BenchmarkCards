# POLYEVAL

## 📊 Benchmark Details

**Name**: POLYEVAL

**Overview**: POLYEVAL is a benchmark consisting of queries and documents collected from real-world healthcare scenarios, focusing on various medical contexts such as medical policy, hospital recommendations, and healthcare inquiries, with multiple annotations regarding timeliness and authoritativeness.

**Data Type**: text

**Domains**:
- Healthcare

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a diverse and representative evaluation benchmark for retrieval-augmented generation models in medical applications.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers
- Domain Experts

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: 1,447 real-world user queries collected from a medical-related online platform in China along with 21,276 relevant documents searched from various sources including expert knowledge, online search engines, and news.

**Size**: 21,276 documents

**Format**: N/A

**Annotation**: Annotated by human annotators, including three highly-skilled annotators for relevance, complement, and utility, with authority levels approximated from source authority.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- HIT
- NDCG

**Calculation**: Calculated based on user query relevance and document effectiveness in answering medical inquiries.

**Interpretation**: Higher scores indicate better retrieval performance and effective generation of relevant content.

**Baseline Results**: Evaluate models augmented with retrieval using public retrieval models like BM25, GTE, BGE-M3, and jina embedding.

**Validation**: Extensive experiments were conducted to validate the benchmark on various tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Fairness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: Potential risk of bias in the queries and documents collected impacting the performance evaluation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Patient data was collected and anonymized to maintain privacy standards.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Complies with local regulations governing medical data usage.
