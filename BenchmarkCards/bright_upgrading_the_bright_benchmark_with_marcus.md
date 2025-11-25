# BRIGHT+ (Upgrading the BRIGHT Benchmark with MARCUS)

## 📊 Benchmark Details

**Name**: BRIGHT+ (Upgrading the BRIGHT Benchmark with MARCUS)

**Overview**: We introduce BRIGHT+, a high-quality refinement of the BRIGHT benchmark tailored for retrieval-augmented reasoning. By identifying and addressing two major flaws—content redundancy and semantic discontinuity—we developed MARCUS, an LLM-powered clean-and-split pipeline that produces coherent, retrievable chunks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- BRIGHT
- BEIR
- MTEB

**Resources**:
- [Resource](https://arxiv.org/abs/2506.07116)

## 🎯 Purpose and Intended Users

**Goal**: To support future research on robust, reasoning-centric retrieval.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Multi-hop reasoning

**Limitations**: MARCUS improves corpus quality for retrieval-augmented reasoning but incurs high computational costs and relies on BRIGHT-specific supervision.

## 💾 Data

**Source**: Originally derived from the BRIGHT corpus and StackExchange-derived subdomains.

**Size**: 18,187 chunks

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation metrics based on retrieval performance
- NDCG@10

**Metrics**:
- nDCG@10

**Calculation**: nDCG@10 is calculated based on the relevance and ranking quality of retrieved documents.

**Interpretation**: Higher nDCG@10 indicates better retrieval effectiveness.

**Validation**: Tests performed with various retrievers, processing times, and query formulations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: Incorporation of LLMs may introduce biases or hallucinations; prompting strategies mitigate these risks.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Our proposed pipeline operates on existing textual data and does not involve the collection of personally identifiable information.

**Data Licensing**: Released under a research-friendly license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
