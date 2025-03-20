# Cost-Effective Hallucination Detection for LLMs

## 📊 Benchmark Details

**Name**: Cost-Effective Hallucination Detection for LLMs

**Overview**: This work addresses challenges for post-hoc hallucination detection in production settings using a multi-scoring framework that combines different scores for improved performance while remaining cost-effective.

**Data Type**: N/A

**Domains**:
- question answering
- fact checking
- summarization

**Languages**:
- N/A

**Similar Benchmarks**:
- TriviaQA
- FEVER
- HaluEval
- BIG-bench

**Resources**:
- [Resource](arXiv preprint)

## 🎯 Purpose and Intended Users

**Goal**: To develop a framework for detecting hallucinations in the outputs of large language models.

**Target Audience**:
- Research communities
- Businesses utilizing LLMs

**Tasks**:
- Evaluate hallucination detection methodologies
- Develop risk-aware decision making tools

**Limitations**: N/A

**Out of Scope Uses**:
- Non-LLM based applications
- Applications without risk assessment needs

## 💾 Data

**Source**: Diverse datasets including TriviaQA, HaluEval, FEVER, BIG-bench

**Size**: 17944 question-answer pairs (TriviaQA), 14027 examples (FEVER), 10000 examples (HaluEval), 8664 examples (BIG-bench)

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Confidence scoring
- Calibration techniques
- Multi-scoring framework
- Cost-effective multi-scoring

**Metrics**:
- Brier score
- F1 score
- Accuracy

**Calculation**: Combination of multiple scoring signals via logistic regression to optimize performance and cost.

**Interpretation**: Scores reflect the distinct aspects of hallucinations across different methods.

**Baseline Results**: N/A

**Validation**: Empirical validation against various datasets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
