# AGENT IF (Benchmarking Instruction Following of Large Language Models in Agentic Scenarios)

## 📊 Benchmark Details

**Name**: AGENT IF (Benchmarking Instruction Following of Large Language Models in Agentic Scenarios)

**Overview**: AGENT IF is the first benchmark for systematically evaluating LLM instruction following ability in agentic scenarios, constructed from 50 realistic applications involving long and complex instructions with multiple constraints.

**Data Type**: instruction-following tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- IFEval
- FollowBench
- SysBench

**Resources**:
- [GitHub Repository](https://github.com/THU-KEG/AgentIF)
- [Resource](https://huggingface.co/datasets/THU-KEG/AgentIF)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic evaluation framework for LLMs' instruction-following capabilities in real-world agentic scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Real-world agentic applications and industrial frameworks, including open-source agentic systems.

**Size**: 707 examples

**Format**: N/A

**Annotation**: Manually annotated instructions and constraints by human annotators.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-based evaluation
- Code verification

**Metrics**:
- Constraint Success Rate (CSR)
- Instruction Success Rate (ISR)

**Calculation**: CSR is calculated by the proportion of individual constraints met, while ISR measures the percentage of instructions with all constraints satisfied.

**Interpretation**: Higher CSR and ISR indicate better performance in following complex and constraint-laden instructions.

**Baseline Results**: Current LLMs show poor performance, with the best model achieving a CSR of only 59.8.

**Validation**: Validated by a hybrid method including human, code-based, and LLM evaluations.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: ['Misuse risk in instruction following leading to inappropriate actions by agents.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The data will be released under the GPL-3.0 license.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Data collection complied with internal review board approval.
