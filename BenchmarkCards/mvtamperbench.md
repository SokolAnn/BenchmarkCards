# MVTamperBench

## 📊 Benchmark Details

**Name**: MVTamperBench

**Overview**: MVTamperBench is a benchmark that systematically evaluates MLLM robustness against five prevalent tampering techniques: rotation, masking, substitution, repetition, and dropping; based on real-world visual tampering scenarios. It comprises 3.4K original videos, expanded into over 17K tampered clips covering 19 distinct video manipulation tasks.

**Data Type**: video

**Domains**:
- Natural Language Processing

**Languages**:
- N/A

**Similar Benchmarks**:
- MMBench-Video
- BLINK
- Video-MME

**Resources**:
- [Resource](https://amitbcp.github.io/MVTamperBench/)
- [Resource](https://hf.co/datasets/Srikant86/MVTamperBench)
- [GitHub Repository](https://github.com/open-compass/VLMEvalKit)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate the robustness of MLLMs against video tampering techniques.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Video Manipulation Detection

**Limitations**: N/A

## 💾 Data

**Source**: 3.4K original videos from MVBench, augmented to create tampered clips through systematic manipulation.

**Size**: 17,435 tampered clips

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score

**Calculation**: F1 Score is calculated based on the model's performance on video manipulation detection.

**Interpretation**: Higher F1 Scores indicate better model robustness against tampering.

**Baseline Results**: N/A

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Fairness

**Atlas Risks**:
- **Robustness**: Evasion attack, Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
