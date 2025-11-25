# HDAV (High-definition Audio-Visual dataset)

## 📊 Benchmark Details

**Name**: HDAV (High-definition Audio-Visual dataset)

**Overview**: HDAV is a novel large-scale human video dataset containing 2,203 identities, featuring diverse body gestures and detailed annotations, aimed at facilitating broad generalization for audio-driven human video synthesis.

**Data Type**: audio-video pairs

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- CCV2
- MVHumanNet

**Resources**:
- [GitHub Repository](https://github.com/Breakthrough/PySceneDetect)
- [GitHub Repository](https://github.com/Zulko/moviepy)

## 🎯 Purpose and Intended Users

**Goal**: The goal of the HDAV dataset is to provide a comprehensive resource for the training and evaluation of models in 3D human generation and audio-driven video synthesis.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- 3D Video Synthesis
- Gesture Recognition

**Limitations**: N/A

## 💾 Data

**Source**: The dataset consists of 3,425 online videos collected from the internet and 1,325 videos from existing datasets, which are manually annotated with detailed properties.

**Size**: 15 hours of video

**Format**: N/A

**Annotation**: Manual annotation with detailed properties such as gender and clothing type.

## 🔬 Methodology

**Methods**:
- Video synthesis using audio inputs
- Motion generation leveraging large language models
- Diffusion-based video generation with MoE

**Metrics**:
- Fréchet Inception Distance (FID)
- Learned Perceptual Image Patch Similarity (LPIPS)
- t-LPIPS

**Calculation**: Metrics are calculated comparing generated video quality against ground truth and established benchmarks.

**Interpretation**: Lower values in FID and LPIPS indicate better quality, with subjective measures assessing user impressions of motion and visual fidelity.

**Validation**: The dataset is validated through comparative analysis against existing benchmarks and user studies.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Privacy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Privacy**: Personal information in data

**Demographic Analysis**: N/A

**Potential Harm**: ['Potential misuse for generating deceptive content.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
