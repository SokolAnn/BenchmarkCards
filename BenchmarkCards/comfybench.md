# ComfyBench

## 📊 Benchmark Details

**Name**: ComfyBench

**Overview**: ComfyBench is a comprehensive benchmark for evaluating agents’ ability to design collaborative AI systems in ComfyUI, comprising 200 diverse tasks covering various instruction-following generation challenges, along with detailed annotations for 3,205 nodes and 20 workflows.

**Data Type**: task instructions and node annotations

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/comfyanonymous/ComfyUI)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate agents’ ability to design and execute collaborative AI systems autonomously using ComfyUI.

**Target Audience**:
- ML Researchers
- AI Developers

**Tasks**:
- Workflow Generation
- Instruction Following

**Limitations**: N/A

## 💾 Data

**Source**: Annotations for 3,205 nodes and 20 workflows within ComfyUI.

**Size**: 200 tasks

**Format**: JSON

**Annotation**: Detailed annotations for each task and node.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Pass Rate
- Resolve Rate

**Calculation**: Pass Rate measures the ratio of tasks with syntactically and semantically correct workflows. Resolve Rate assesses the execution success against task requirements.

**Interpretation**: A higher pass and resolve rate indicates better agent performance.

**Baseline Results**: ComfyAgent shows improved performance against various baseline agents.

**Validation**: Conducted through automated metrics and human evaluation of generated workflows.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Privacy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
