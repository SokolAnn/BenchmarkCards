# LOTA-BENCH

## 📊 Benchmark Details

**Name**: LOTA-BENCH

**Overview**: LOTA-BENCH is a benchmark for language-oriented task planning for embodied agents. It enables automatic evaluation and quantification of task planning performance.

**Data Type**: natural language instructions and actions

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/lbaa2022/LLMTaskPlanning)

## 🎯 Purpose and Intended Users

**Goal**: To provide a systematic benchmark suite that quantifies the performance of task planners for home-service embodied agents.

**Target Audience**:
- ML Researchers
- Robotics Practitioners

**Tasks**:
- Task Planning
- Action Execution

**Limitations**: The benchmark does not encompass low-level action planning or visual understanding.

## 💾 Data

**Source**: ALFRED dataset and Watch-And-Help (WAH) dataset, extended version WAH-NL.

**Size**: 416 instructions for training set and 195 for test set

**Format**: N/A

**Annotation**: Collected via the Prolific crowdsourcing platform

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Baseline task planner testing

**Metrics**:
- Task success rate

**Calculation**: Performance is assessed by comparing the final state of the simulator with predefined goal conditions.

**Interpretation**: Higher task success rates indicate better performance of the language model in executing task plans.

**Baseline Results**: GPT-3 (text-davinci-003) succeeded with a success rate of 21.36% on ALFRED.

**Validation**: The benchmark allows for rigorous evaluation of LLM-based task planners against two dataset-simulator pairs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
