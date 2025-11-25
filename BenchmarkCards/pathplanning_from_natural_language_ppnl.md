# PathPlanning from Natural Language (PPNL)

## 📊 Benchmark Details

**Name**: PathPlanning from Natural Language (PPNL)

**Overview**: PPNL evaluates LLMs' spatial-temporal reasoning by formulating path planning tasks that require navigation to target locations while avoiding obstacles and adhering to constraints.

**Data Type**: path planning tasks

**Domains**:
- Artificial Intelligence
- Robotics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/username/repo)

## 🎯 Purpose and Intended Users

**Goal**: To analyze the ability of LLMs to perform spatial-temporal reasoning through path planning tasks.

**Target Audience**:
- AI Researchers
- Robotics Practitioners

**Tasks**:
- Path Planning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic grid environments generated for path planning tasks.

**Size**: 160,000 task instances

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate
- Optimal Rate
- Exact Match Accuracy
- Feasible Rate
- Distance to Goal
- Unreachable Accuracy

**Calculation**: Metrics are calculated based on the LLM's ability to navigate from initial to goal locations while avoiding obstacles.

**Interpretation**: Higher success rates and optimal rates indicate better spatial-temporal reasoning capabilities.

**Validation**: The benchmark is validated through controlled experiments with LLMs, comparing different models and prompting methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
