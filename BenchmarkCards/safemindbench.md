# SafeMindBench

## 📊 Benchmark Details

**Name**: SafeMindBench

**Overview**: SafeMindBench is a multimodal benchmark with 5,558 samples spanning four task categories (Instr-Risk, Env-Risk, Order-Fix, Req-Align) designed to systematically evaluate safety risks in embodied agents.

**Data Type**: instruction-image pairs

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- EAsafetyBench
- SafePlan-Bench
- SafeAgentBench
- IS-Bench
- EARBench

**Resources**:
- [Resource](https://arxiv.org/abs/2509.25885)

## 🎯 Purpose and Intended Users

**Goal**: To provide a rigorous evaluation suite that helps advance the systematic study and mitigation of safety risks in embodied LLM agents.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Safety Evaluation
- Robustness Testing

**Limitations**: N/A

## 💾 Data

**Source**: Dataset generated using LLMs and human verification, comprising various safety scenarios.

**Size**: 5,558 samples

**Format**: JSON

**Annotation**: Generated via LLM synthesis followed by human verification.

## 🔬 Methodology

**Methods**:
- Automated metrics
- LLM-based evaluation

**Metrics**:
- Safety Rate (SR)
- Success Rate (SuccR)
- Effectiveness Rate (ER)

**Calculation**: Metrics are calculated based on the proportion of tasks completed without constraint violations and the successful completion of tasks as intended.

**Interpretation**: Higher SR indicates better compliance with safety constraints; higher SuccR indicates successful task completion.

**Baseline Results**: Performance compared against leading LLMs and embodied agent architectures.

**Validation**: Extensive experiments across various task scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Robustness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
