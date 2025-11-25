# mFollowIR (Multilingual Benchmark for Instruction Following in Retrieval)

## 📊 Benchmark Details

**Name**: mFollowIR (Multilingual Benchmark for Instruction Following in Retrieval)

**Overview**: mFollowIR is a multilingual benchmark for measuring instruction-following ability in retrieval models, built on the TREC NeuCLIR narratives in Russian, Chinese, and Persian. It allows for evaluation of cross-lingual and multilingual retrieval model capabilities.

**Data Type**: reranking tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Russian
- Chinese
- Persian

**Similar Benchmarks**:
- FollowIR

**Resources**:
- [GitHub Repository](https://github.com/orionw/FollowIR)

## 🎯 Purpose and Intended Users

**Goal**: To provide a test bed for instruction-following retrieval models across multiple languages.

**Target Audience**:
- ML Researchers
- Natural Language Processing Practitioners
- Information Retrieval Researchers

**Tasks**:
- Instruction Following
- Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from the TREC NeuCLIR narratives with human-annotated edits.

**Size**: 123 queries

**Format**: N/A

**Annotation**: Annotated by native and fluent speakers to ensure quality translations and narrative alterations.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- nDCG@20
- p-MRR

**Calculation**: p-MRR is calculated by checking the position of newly non-relevant documents and comparing their ranks with the original rankings.

**Interpretation**: A higher p-MRR indicates better instruction-following ability, with scores that can range from -1.0 (incorrect) to 1.0 (correct).

**Validation**: Evaluation was performed on both cross-lingual and multilingual settings using a variety of retrieval models.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
