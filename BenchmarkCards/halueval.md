# HaluEval

## 📊 Benchmark Details

**Name**: HaluEval

**Overview**: A large-scale collection of generated and human-annotated hallucinated samples for evaluating the performance of LLMs in recognizing hallucinations.

**Data Type**: Generated and human-annotated samples

**Domains**:
- Natural Language Processing
- Language Models

**Languages**:
- English

**Similar Benchmarks**:
- BEGIN benchmark
- AIS benchmark

**Resources**:
- [GitHub Repository](https://github.com/RUCAIBox/HaluEval)

## 🎯 Purpose and Intended Users

**Goal**: To understand what types of content and to which extent LLMs tend to hallucinate.

**Target Audience**:
- Researchers
- Practitioners in AI

**Tasks**:
- Evaluate LLMs' capability to recognize hallucinations
- Analyze hallucinated content

**Limitations**: Limited by the capacity of ChatGPT in generating hallucinated samples.

**Out of Scope Uses**:
- Real-world applications without further vetting
- Misuse of hallucinated samples

## 💾 Data

**Source**: Generated using ChatGPT and annotated by human labelers.

**Size**: 35,000 samples (5,000 general queries and 30,000 task-specific examples)

**Format**: N/A

**Annotation**: Human annotations for hallucination identification

## 🔬 Methodology

**Methods**:
- Two-stage sampling-then-filtering approach
- Human annotation for verification

**Metrics**:
- Accuracy in recognizing hallucinations

**Calculation**: N/A

**Interpretation**: Performance evaluation based on the ability to recognize hallucinations

**Baseline Results**: ChatGPT achieved 62.59% accuracy in question answering.

**Validation**: Human labelers established reliability through max-voting methodology.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Privacy
- Fairness
- Explainability

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Privacy**: Exposing personal information
- **Fairness**: Data bias
- **Explainability**: Unexplainable output

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential for misuse of hallucinated samples', 'User misinformation']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All user data anonymized during annotation.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
