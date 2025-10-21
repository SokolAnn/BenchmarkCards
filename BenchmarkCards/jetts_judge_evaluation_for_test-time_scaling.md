# JETTS (Judge Evaluation for Test-Time Scaling)

## 📊 Benchmark Details

**Name**: JETTS (Judge Evaluation for Test-Time Scaling)

**Overview**: The JETTS benchmark evaluates judge performance in three domains (math reasoning, code generation, and instruction following) under three task settings: response reranking, step-level beam search, and critique-based response refinement.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RewardBench
- ProcessBench

**Resources**:
- [GitHub Repository](https://github.com/SalesforceAIResearch/jetts-benchmark)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the effectiveness of LLM-judges in test-time scaling scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Response Reranking
- Step-Level Beam Search
- Critique-Based Refinement

**Limitations**: N/A

## 💾 Data

**Source**: Responses generated from multiple large language models trained for different tasks.

**Size**: N/A

**Format**: N/A

**Annotation**: Responses were generated automatically without manual annotation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Normalized Helpfulness

**Calculation**: Metrics are calculated based on judge performance across various tasks and datasets.

**Interpretation**: Positive normalized helpfulness means the judge aids in improving the model generation.

**Baseline Results**: Responses are compared against greedy decoding performance and random selection.

**Validation**: Performance is validated through comparisons with existing models and evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
