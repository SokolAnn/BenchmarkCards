# FeB4RAG: Evaluating Federated Search in the Context of Retrieval Augmented Generation

## 📊 Benchmark Details

**Name**: FeB4RAG: Evaluating Federated Search in the Context of Retrieval Augmented Generation

**Overview**: FeB4RAG is a novel dataset specifically designed for federated search within Retrieval-Augmented Generation (RAG) frameworks. The dataset is derived from 16 sub-collections of the BEIR benchmarking collection, includes 790 information requests tailored for chatbot applications, top results returned by each resource, and associated LLM-derived relevance judgements. It is intended to support the development and evaluation of federated search methods in the context of RAG pipelines.

**Data Type**: text (information requests and search result documents)

**Domains**:
- Natural Language Processing
- Information Retrieval

**Similar Benchmarks**:
- TREC FedWeb
- BEIR

**Resources**:
- [GitHub Repository](https://github.com/ielab/FeB4RAG)
- [Resource](https://huggingface.co/open-llm-leaderboard)
- [Resource](https://huggingface.co/RubielLabarta/LogoS-7Bx2-MoE-13B-v0.1)

## 🎯 Purpose and Intended Users

**Goal**: Provide a test collection to evaluate federated search methods (resource selection and result merging) within Retrieval-Augmented Generation (RAG) pipelines and to demonstrate the impact of federated search quality on RAG-generated responses.

**Target Audience**:
- Information Retrieval researchers
- Developers of Retrieval-Augmented Generation systems
- Model developers

**Tasks**:
- Resource Selection
- Result Merging
- Question Answering
- Information Retrieval Evaluation

**Limitations**: Uses only 16 BEIR sub-collections and dense retrievers selected as of 31/12/2023; excludes models based on APIs, models without source code, and models with more than 6 billion parameters due to computational and cost constraints; target of 50 queries per dataset not achieved for two datasets (Touché-2020: 49 queries; MS MARCO: 41 queries); relevance judgements produced using LLMs (costly) rather than full human annotation.

## 💾 Data

**Source**: Derived from 16 sub-collections of the BEIR benchmarking collection (each BEIR dataset paired with a retrieval model; listed in Table 1 of the paper).

**Size**: 790 information requests; 36.9M documents (overall collection size reported as 36.9M).

**Format**: N/A

**Annotation**: Relevance judgements produced by two LLMs (upstage/SOLAR-10.7B-Instruct-v1.0 and RubielLabarta/LogoS-7Bx2-MoE-13B-v0.1). Relevance labels use a 4-level scale: key (3), high relevance (2), minimal relevance (1), not relevant (0). For each search result, each LLM produced a label; the integer scores were averaged and rounded down to produce a final label. Search-engine-level relevance derived via graded precision scores following TREC FedWeb practice.

## 🔬 Methodology

**Methods**:
- LLM-based relevance labelling
- Graded precision scoring (search-engine-level)
- Automated agreement analysis using Cohen's Kappa
- Human pairwise preference evaluation (side-by-side) for RAG responses

**Metrics**:
- Graded Precision (0-100)
- nDCG@k
- nP@k
- Cohen's Kappa
- Pairwise preference percentage (human evaluation)

**Calculation**: Graded Precision(r, s) = ( sum_{i=1}^{10} w_i(r,s) / 10 ) × 100, where weights are w_not_relevant=0, w_minimal_relevance=0.25, w_high_relevance=0.5, w_key=1. LLM result-level scores (0-3) were averaged across two LLMs and rounded down to an integer for final labels. For agreement with human annotations, LLM labels were binarized (relevant if graded label > 0; not relevant if graded label = 0) and Cohen's Kappa computed per collection.

**Interpretation**: Graded Precision ranges from 0 to 100, where 100 indicates highest relevance. Cohen's Kappa values above 0.4 are interpreted as moderate agreement (paper reports aggregated LLM-vs-human Kappa values above 0.4, and overall fused LLM Kappa of 0.57). Human pairwise preferences indicate which RAG-federation approach yields better responses.

**Baseline Results**: Pairwise human preference comparison between a naive federated system (naive-fed) and an optimal resource-selected system (best-fed) shows best-fed responses are preferred more often across evaluated criteria (coverage, consistency, correctness, clarity); see Figure 7 for aggregated preferences.

**Validation**: LLM-based labels were validated against human annotations from the original BEIR datasets by randomly selecting one relevant and one irrelevant search result per request (where available), binarizing labels, and computing Cohen's Kappa per collection. Cross-LLM agreement was also computed across all search results (overall Kappa reported as 0.57).

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Transparency
- Governance
- Accuracy

**Atlas Risks**:
- **Robustness**: Hallucination
- **Transparency**: Uncertain data provenance
- **Governance**: Lack of system transparency, Lack of data transparency
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
