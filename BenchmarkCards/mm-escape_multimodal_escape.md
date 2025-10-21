# MM-Escape (Multimodal Escape)

## 📊 Benchmark Details

**Name**: MM-Escape (Multimodal Escape)

**Overview**: MM-Escape is an extensible benchmark for evaluating complex multimodal reasoning abilities in MLLMs, based on real-world escape games. It emphasizes both the reasoning process and task completion.

**Data Type**: multimodal

**Domains**:
- Artificial Intelligence

**Languages**:
- English

**Similar Benchmarks**:
- EscapeBench
- TextWorld

**Resources**:
- [GitHub Repository](https://github.com/THUNLP-MT/EscapeCraft)
- [Resource](https://thunlp-mt.github.io/EscapeCraft)

## 🎯 Purpose and Intended Users

**Goal**: To advance comprehensive evaluation of multimodal reasoning for MLLMs through quantitative assessment of intermediate reasoning processes and task completion performance.

**Target Audience**:
- ML Researchers
- Model Developers
- Domain Experts

**Tasks**:
- Multimodal Room Escape

**Limitations**: N/A

## 💾 Data

**Source**: Automatically generated 3D room environments from a procedural generation framework.

**Size**: 63 scenes

**Format**: 3D Scene Files

**Annotation**: Automatically generated with 3D furniture models and gameplay logic.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Average Escape Rate (ER)
- Prop Gain
- Grab Success Rate (GSR)
- Steps
- Grab Ratio

**Calculation**: Metrics are calculated based on interactions and success rates during gameplay.

**Interpretation**: Higher ER indicates better performance in escaping the room; also assesses intermediate steps and prop interactions.

**Baseline Results**: Results show performance metrics across Difficulty-1, Difficulty-2, and Difficulty-3 scenarios.

**Validation**: Evaluated through gameplay demonstrations and model interactions in the escape environment.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
