# CURATe: Benchmarking Personalised Alignment of Conversational AI Assistants

## 📊 Benchmark Details

**Name**: CURATe: Benchmarking Personalised Alignment of Conversational AI Assistants

**Overview**: CURATe is a multi-turn benchmark for evaluating personalized alignment in LLM-based AI assistants, focusing on their ability to handle user-provided safety-critical contexts. It tests models' capacities to maintain consistent awareness of user-specific information across extended interactions.

**Data Type**: multi-turn dialogue scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentBench
- MT-Bench-101
- MT-Eval

**Resources**:
- [Resource](https://anonymous.4open.science/r/llm_prag_benchmark-0C48/README.md)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve personalized alignment in dialogue agents by assessing their ability to consistently remember and utilize safety-critical user information across multiple interactions.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Developers

**Tasks**:
- Dialogue Management
- Personalized Recommendation

**Limitations**: N/A

## 💾 Data

**Source**: Five interaction scenarios created specifically for testing personalized alignment in conversational AI, each containing 337 use cases.

**Size**: 1,685 use cases

**Format**: N/A

**Annotation**: Manually iterated design process with multi-turn dialogues involving user constraints and recommendation queries.

## 🔬 Methodology

**Methods**:
- Automated Evaluation
- Human Annotation

**Metrics**:
- Pass Rate

**Calculation**: Pass rates are calculated based on whether the models correctly account for critical personal information in their responses.

**Interpretation**: A pass indicates the model acknowledged and considered the user's safety-critical constraint in recommendations.

**Baseline Results**: Mean pass rate was 88.4% for the best-performing model, with significant variation across scenarios.

**Validation**: Results validated against both automated metrics and human evaluator assessments.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Poor model accuracy
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
