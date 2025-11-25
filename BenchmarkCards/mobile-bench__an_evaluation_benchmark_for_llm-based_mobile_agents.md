# Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents

## 📊 Benchmark Details

**Name**: Mobile-Bench: An Evaluation Benchmark for LLM-based Mobile Agents

**Overview**: Mobile-Bench is a novel benchmark for evaluating the capabilities of LLM-based mobile agents, providing a dataset of 832 entries and over 200 tasks designed for multi-APP collaboration scenarios.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AndroidEnv
- MobileEnv
- WebShop

**Resources**:
- [GitHub Repository](https://github.com/XiaoMi/MobileBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for LLM-based mobile agents, assessing their planning, reasoning, and interaction capabilities in real-world mobile environments.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multi-App Interaction

**Limitations**: The Mobile-Bench may struggle with general large models which exhibit pronounced illusions in API calls.

## 💾 Data

**Source**: Real user queries combined with generated data from LLMs.

**Size**: 832 examples

**Format**: N/A

**Annotation**: Mixed: real data from user queries and generated tasks through GPT-4.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- PassRate
- CheckPoint coverage

**Calculation**: CheckPoint coverage is calculated as the weighted sum of the scores based on package usage, key phrases, and API calls.

**Interpretation**: Interpretation revolves around determining the ability of the LLM-based agents to navigate and complete tasks in the predefined mobile environment.

**Baseline Results**: Performance results based on LLMs like GPT-3.5 and GPT-4, showing variations in PassRate across task types.

**Validation**: Quality verification processes include cross-source validation of user-generated and GPT-4 generated tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Privacy measures are in place, focusing on de-identification of user data collected.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
