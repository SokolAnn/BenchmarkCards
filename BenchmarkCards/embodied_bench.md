# EMBODIED BENCH

## 📊 Benchmark Details

**Name**: EMBODIED BENCH

**Overview**: EMBODIED BENCH is an extensive benchmark designed to evaluate vision-driven embodied agents, featuring 1,128 testing tasks across four environments and assessing essential agent capabilities like commonsense reasoning, instruction understanding, spatial awareness, visual perception, and long-term planning.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- VisualAgentBench
- ALFWorld

**Resources**:
- [Resource](https://embodiedbench.github.io)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for multi-modal large language models as embodied agents.

**Target Audience**:
- ML Researchers
- Roboticists
- AI Practitioners

**Tasks**:
- Object Manipulation
- Navigation
- Task Planning

**Limitations**: N/A

## 💾 Data

**Source**: Data collected from diverse environments and tasks designed to evaluate MLLM-based embodied agents.

**Size**: 1,128 testing tasks

**Format**: JSON

**Annotation**: Data was annotated manually and through instruction augmentation with GPT-4o.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Model-based evaluation

**Metrics**:
- Task success rate

**Calculation**: Task success is assessed based on achieving the objectives outlined in the instructions across diverse test tasks.

**Interpretation**: A higher task success rate indicates better performance in multi-step action execution.

**Baseline Results**: N/A

**Validation**: Extensive experiments evaluating 24 leading models and their performance in various tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
