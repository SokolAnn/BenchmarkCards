# NoisyEQA

## 📊 Benchmark Details

**Name**: NoisyEQA

**Overview**: The NoisyEQA benchmark is designed to evaluate an agent’s ability to recognize and correct noisy questions across four common types of noise: Latent Hallucination Noise, Memory Noise, Perception Noise, and Semantic Noise.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

## 🎯 Purpose and Intended Users

**Goal**: To evaluate agents' performance against noisy questions and improve their robustness in real-world scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated using a novel LLM-powered framework.

**Size**: 500 noisy questions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Evaluation by human annotators
- LLM-based automatic scoring

**Metrics**:
- Detection Rate (DR)
- Correction Rate (CR)

**Calculation**: Metrics calculated based on the ability of agents to detect and correct noisy questions.

**Interpretation**: Higher scores indicate better performance in terms of noise detection and correction.

**Baseline Results**: N/A

**Validation**: Evaluation revealed that agents struggle with noise detection, leading to erroneous responses.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
