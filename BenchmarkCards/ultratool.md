# UltraTool

## 📊 Benchmark Details

**Name**: UltraTool

**Overview**: UltraTool is a comprehensive evaluation benchmark designed to improve and evaluate LLMs’ ability in tool utilization within real-world scenarios, focusing on the entire process of using tools including planning, creating, and applying them in complex tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/JoeYing1019/UltraTool)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation of LLMs' capabilities in tool utilization across various dimensions related to planning, tool creation, and usage.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Tool Utilization Evaluation
- Planning Tasks
- Tool Creation Assessment

**Limitations**: N/A

## 💾 Data

**Source**: Real-world user queries, collected and refined by experts across various domains.

**Size**: 5,824 samples

**Format**: N/A

**Annotation**: Manual annotation and refinement by domain experts using a structured approach.

## 🔬 Methodology

**Methods**:
- Multi-Dimensional Point-Wise LLM-as-Judge Method
- Key-Value based Accuracy
- Key-Value based Levenshtein Distance

**Metrics**:
- Accuracy
- Completeness
- Executability
- Syntactic Soundness
- Structural Rationality
- Efficiency

**Calculation**: Metrics are calculated based on the responses against the structured plans derived from user queries.

**Interpretation**: Higher scores indicate better performance in planning and tool utilization capabilities of LLMs.

**Baseline Results**: N/A

**Validation**: Extensive evaluation across various LLMs and comparison with human benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential dependencies on specific tool availability affecting generalizability.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All data are de-identified, safeguarding privacy concerns.

**Data Licensing**: Not Applicable

**Consent Procedures**: Used de-identified data, consent not applicable as it involves simulated user interactions.

**Compliance With Regulations**: Not Applicable
