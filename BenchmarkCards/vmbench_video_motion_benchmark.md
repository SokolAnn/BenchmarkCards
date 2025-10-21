# VMBench (Video Motion Benchmark)

## 📊 Benchmark Details

**Name**: VMBench (Video Motion Benchmark)

**Overview**: VMBench is the first benchmark focused on comprehensive video motion assessment, featuring perception-aligned motion metrics to systematically evaluate the motion generation quality of video generation models. It includes diverse motion types covering 969 categories and integrates human preference annotations to validate the metrics.

**Data Type**: video

**Domains**:
- Computer Vision

**Languages**:
- N/A

**Similar Benchmarks**:
- VBench
- Evalcrafter

**Resources**:
- [GitHub Repository](https://github.com/GD-AIGC/VMBench)

## 🎯 Purpose and Intended Users

**Goal**: To establish a standardized evaluation framework for assessing the authenticity of motion in generated videos aligned with human perception.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Video Generation

**Limitations**: N/A

## 💾 Data

**Source**: Generated videos from various text-to-video models using the MMPG framework.

**Size**: 6,300 videos

**Format**: N/A

**Annotation**: Human preference annotations validated the metrics, resulting in systematic evaluations.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Commonsense Adherence Score (CAS)
- Motion Smoothness Score (MSS)
- Object Integrity Score (OIS)
- Perceptible Amplitude Score (PAS)
- Temporal Coherence Score (TCS)

**Calculation**: Each metric is calculated based on specific algorithms designed to align with human perception.

**Interpretation**: Scores closer to 1 indicate better alignment with human perception of motion quality.

**Baseline Results**: Metrics were validated with a 35.3% improvement in Spearman’s correlation over baseline methods.

**Validation**: Human-aligned validation was conducted with three domain experts annotating video samples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Robustness**: Evasion attack
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
