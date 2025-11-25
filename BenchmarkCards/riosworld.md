# RiOSWorld

## 📊 Benchmark Details

**Name**: RiOSWorld

**Overview**: RiOSWorld is a benchmark designed to evaluate the potential risks of multimodal large language model-based agents during real-world computer manipulations, covering 492 risky tasks across various computer applications.

**Data Type**: risky tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- OSWorld
- WebArena
- AndroidWorld

**Resources**:
- [Resource](https://arxiv.org/abs/2506.00618)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety risks of multimodal large language model-based agents in realistic computer-use scenarios and highlight their vulnerabilities.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Developers

**Tasks**:
- Safety Risk Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: 492 risky tasks designed by authors, inspired by other benchmarks and verified through execution.

**Size**: 492 tasks

**Format**: JSON

**Annotation**: Manual verification by authors, ensuring executable environment and high probability of risk triggering.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Rule-based risk evaluation
- LLM-as-a-judge evaluation

**Metrics**:
- Risk Goal Intention Rate
- Risk Goal Completion Rate

**Calculation**: Metrics are derived from risk goal evaluations based on whether MLLM agents intend to trigger risks and complete risky tasks.

**Interpretation**: Higher rates indicate greater safety risk awareness deficiencies in MLLM agents.

**Baseline Results**: MLLMs exhibit an unsafe rate of over 75% on risk goal intention and 45% on risk goal completion.

**Validation**: Extensive evaluations conducted on 10 representative MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Privacy
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
