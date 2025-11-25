# LIFELONG-SOTOPIA

## 📊 Benchmark Details

**Name**: LIFELONG-SOTOPIA

**Overview**: LIFELONG-SOTOPIA is designed to evaluate the social intelligence of language agents over lifelong social interactions by simulating multi-episode interactions in which agents role-play characters with specific social goals.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SOTOPIA

**Resources**:
- [Resource](https://arxiv.org/abs/2506.12666)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the social intelligence of language agents over lifelong social interactions.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Social Intelligence Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Generated scenarios based on the SOTOPIA database using the GPT-4 API.

**Size**: 41 scenarios for each relationship type.

**Format**: Text

**Annotation**: Automatically generated with human validation.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Believability (BEL)
- Goal Completion (GOAL)

**Calculation**: Scores on BEL and GOAL dimensions are calculated based on ratings assigned post evaluation.

**Interpretation**: Higher scores indicate better performance in terms of achieving social goals and believability.

**Baseline Results**: Human evaluations consistently perform better than language agents across both BEL and GOAL dimensions.

**Validation**: Evaluations conducted with both human participants and language agents to establish baseline comparisons.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
