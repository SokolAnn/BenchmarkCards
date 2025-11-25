# VideoGameQA-Bench

## 📊 Benchmark Details

**Name**: VideoGameQA-Bench

**Overview**: VideoGameQA-Bench is a comprehensive benchmark designed to evaluate vision-language models (VLMs) specifically for video game quality assurance (QA) tasks, including visual unit testing, visual regression testing, glitch detection, and bug report generation.

**Data Type**: image and video samples

**Domains**:
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- GlitchBench

**Resources**:
- [Resource](https://asgaardlab.github.io/videogameqa-bench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a standardized benchmark for evaluating the performance of vision-language models in various video game quality assurance tasks.

**Target Audience**:
- ML Researchers
- Game Developers
- Quality Assurance Engineers

**Tasks**:
- Visual Unit Testing
- Glitch Detection
- Bug Report Generation
- Visual Regression Testing
- Needle-in-a-Haystack

**Limitations**: N/A

## 💾 Data

**Source**: Real-world gameplay images from Steam and gameplay videos from YouTube, combined with synthetic samples generated using the Unity game engine.

**Size**: 4,786 samples consisting of 2,236 image-based samples and 1,200 video-based samples

**Format**: JSON

**Annotation**: Manual annotation and verification of collected samples by researchers

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated based on model outputs against ground truth annotations.

**Interpretation**: Higher scores indicate better model performance in detecting glitches or errors in video game QA tasks.

**Baseline Results**: N/A

**Validation**: Models evaluated on diverse tasks including visual unit tests, UI validation, and glitch detection

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Steam Subscriber Agreement, CC-BY-NC 4.0 for GamePhysics, YouTube Standard License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
