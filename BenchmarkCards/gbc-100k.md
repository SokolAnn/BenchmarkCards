# GBC-100K

## 📊 Benchmark Details

**Name**: GBC-100K

**Overview**: GBC-100K is a large-scale multimodal dataset of individual human behaviors with multi-level textual annotations, bridging the gap between high-level behavior understanding and low-level motion synthesis.

**Data Type**: video-SMPL pairs

**Domains**:
- Robotics
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/user/repo)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate research in behavior generation for humanoid characters through the use of a structured framework integrating language-driven behavioral planning and physics-based motion control.

**Target Audience**:
- ML Researchers
- Robotics Researchers

**Tasks**:
- Behavior Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected from various internet sources including YouTube-8M, Kinetics, HMDB, and others.

**Size**: 100,000 clips

**Format**: video

**Annotation**: Annotated with hierarchical granularity of semantic and motion plans driven by target goals.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Success Rate
- Physical Error
- Fréchet Inception Distance
- R-Precision

**Calculation**: Metrics are calculated based on the methods described in the methodology section of the paper.

**Interpretation**: Lower Physical Error indicates more physically plausible sequences, while higher Success Rate reflects better practical utility of generated behaviors.

**Baseline Results**: N/A

**Validation**: Experimental results demonstrate significant improvements in temporal stability and action fidelity over extended sequences compared to existing methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Bias

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
