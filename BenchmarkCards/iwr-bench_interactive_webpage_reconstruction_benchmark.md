# IWR-Bench (Interactive Webpage Reconstruction Benchmark)

## 📊 Benchmark Details

**Name**: IWR-Bench (Interactive Webpage Reconstruction Benchmark)

**Overview**: IWR-Bench is a novel benchmark for evaluating the capabilities of Large Vision-Language Models (LVLMs) in interactive webpage reconstruction from video. It features 113 tasks from real-world websites, including diverse interactive complexities and evaluation of multi-modal reasoning and code generation.

**Data Type**: video and static assets

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- Pix2Code
- Design2Code
- Interaction2Code

**Resources**:
- [GitHub Repository](https://github.com/L-O-I/IWR-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of models to reconstruct interactive webpages based on user interaction videos.

**Target Audience**:
- ML Researchers
- Model Developers
- Industry Practitioners

**Tasks**:
- Webpage Reconstruction
- Code Generation

**Limitations**: N/A

## 💾 Data

**Source**: Curated tasks from real-world websites with interaction videos and static assets.

**Size**: 113 tasks

**Format**: N/A

**Annotation**: Tasks were annotated by experts with detailed action sequences and logical assertions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Interactive Functionality Score (IFS)
- Visual Fidelity Score (VFS)
- Final Score

**Calculation**: IFS and VFS are calculated based on action success and visual fidelity assessment respectively, followed by a weighted combination to derive the Final Score.

**Interpretation**: Higher scores indicate better performance in generating functionally correct and visually accurate webpage code.

**Validation**: Robustness confirmed through cross-verified action trajectories and multiple evaluation metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
