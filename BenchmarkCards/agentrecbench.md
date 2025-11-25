# AgentRecBench

## 📊 Benchmark Details

**Name**: AgentRecBench

**Overview**: AgentRecBench is the first comprehensive benchmark for evaluating the emerging LLM-powered agentic recommender systems, providing standardized evaluation protocols to systematically assess these methods across diverse scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [Resource](https://huggingface.co/datasets/SGJQovo/AgentRecBench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate both emerging agentic recommender systems and traditional recommendation methods across diverse scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Yelp, GoodReads, and Amazon datasets processed into a unified interaction environment.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Hit Rate@ N (HR@ N)

**Calculation**: Measured as the probability that the ground-truth item appears in the top-N ranked positions.

**Interpretation**: A higher Hit Rate@ N indicates better recommendation performance.

**Baseline Results**: Evaluated against 10 agentic and classic recommendation methods.

**Validation**: Validated through the AgentSociety Challenge with numerous competing teams.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
