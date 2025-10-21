# MCPWorld

## 📊 Benchmark Details

**Name**: MCPWorld

**Overview**: MCPWorld is the first automatic CUA testbed for API, GUI, and API-GUI hybrid agents, offering robust, accurate evaluation by directly monitoring application behavior through techniques like dynamic code instrumentation.

**Data Type**: task execution scenarios

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- AgentStudio
- AndroidWorld
- WindowsAgentArena

**Resources**:
- [GitHub Repository](https://github.com/SAAgent/MCPWorld)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate and standardize the benchmarking of next-generation computer use agents leveraging rich external tools.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Task Completion
- User Interaction Evaluation

**Limitations**: Future work will incorporate a broader range of agent architectures to enable comprehensive comparative analyses.

## 💾 Data

**Source**: Data collected from 10 widely-used open-source desktop applications.

**Size**: 201 tasks

**Format**: N/A

**Annotation**: Currently includes well-curated and annotated user tasks covering diversified use cases and difficulty levels.

## 🔬 Methodology

**Methods**:
- Dynamic Binary Instrumentation
- Targeted Code Injection
- API-Driven State Querying

**Metrics**:
- Task Success Rate
- Key Step Completion Rate

**Calculation**: Metrics calculated based on the percentage of tasks completed successfully within the time limit.

**Interpretation**: Higher rates indicate better performance of agents across various task types.

**Baseline Results**: Initial tests reported task completion accuracy of 75.12%.

**Validation**: Tested across various interaction modalities.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
