# VTTS-80K

## 📊 Benchmark Details

**Name**: VTTS-80K

**Overview**: VTTS-80K is a dataset tailored for iterative perception, designed to enhance multimodal reasoning capabilities of large language models by providing fine-grained annotations for visual reasoning, including QA pairs enriched with annotated spatio-temporal cues and corresponding chains of thought.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/OpenGVLab/VideoChat-R1)

## 🎯 Purpose and Intended Users

**Goal**: To facilitate iterative perceptual refinement and support the training of multimodal large language models in handling spatio-temporal reasoning tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Question Answering
- Image Reasoning
- Temporal Grounding
- Spatial Grounding

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from existing datasets including GOT, Charades, and RefCOCO with QA pairs and annotations for relevant spatio-temporal segments.

**Size**: 80,000 QA pairs, 15,000 temporal clues, 30,000 spatial clues

**Format**: N/A

**Annotation**: Manual annotation by experts based on video/image content.

## 🔬 Methodology

**Methods**:
- Reinforcement Learning
- Iterative Perception

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the model's ability to accurately predict spatio-temporal segments and answer questions related to the visual content.

**Interpretation**: A high accuracy indicates the model's ability to effectively reason over multimodal inputs using the trained perceptual framework.

**Baseline Results**: N/A

**Validation**: The effectiveness of iterative perception was validated through extensive experiments on various benchmarks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness

**Atlas Risks**:
- **Fairness**: Data bias
- **Privacy**: Personal information in data
- **Societal Impact**: Impact on education: plagiarism, Impact on cultural diversity

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
