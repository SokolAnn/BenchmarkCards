# CPRet (Competitive Programming Retrieval)

## 📊 Benchmark Details

**Name**: CPRet (Competitive Programming Retrieval)

**Overview**: CPRet is a retrieval-oriented benchmark suite for competitive programming that addresses the issue of duplicate problems by introducing four key retrieval tasks. It provides high-quality training data and temporally separated test sets to evaluate model performance reliably.

**Data Type**: problem-description pairs and code pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese
- Japanese

**Similar Benchmarks**:
- APPS
- CodeContests
- TACO

**Resources**:
- [GitHub Repository](https://github.com/coldchair/CPRet)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic way to evaluate retrieval models in competitive programming, focusing on handling duplicate and similar problems.

**Target Audience**:
- ML Researchers
- Competitive Programmers
- Model Developers

**Tasks**:
- Text-to-Code Retrieval
- Code-to-Code Retrieval
- Problem-to-Duplicate Retrieval
- Simplified-to-Full Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Collected from online programming platforms and problem repositories.

**Size**: 42,200 problems and 2.9 million solutions

**Format**: JSON

**Annotation**: Manual annotation for duplicates and language simplifications.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- NDCG@10

**Calculation**: N/A

**Interpretation**: Higher NDCG@10 indicates better retrieval performance.

**Validation**: Models were validated against temporally separated test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Fairness**: Data bias

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
