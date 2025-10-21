# USB (Unified Safety Benchmark)

## 📊 Benchmark Details

**Name**: USB (Unified Safety Benchmark)

**Overview**: USB-SafeBench is a comprehensive safety evaluation benchmark for multimodal large language models (MLLMs), covering various risk categories and modality combinations to assess vulnerabilities and oversensitivities.

**Data Type**: text-image pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- MMSafetyBench
- Hades
- HarmBench
- SafeBench

**Resources**:
- [GitHub Repository](https://github.com/Hongqiong12/USB-SafeBench)
- [Resource](https://huggingface.co/datasets/cgjacklin/USB)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reliable safety assessment benchmark by integrating high-quality data across a wide range of risk categories and modality types for evaluating MLLMs.

**Target Audience**:
- ML Researchers
- Safety Engineers
- Model Developers

**Tasks**:
- Safety Assessment
- Vulnerability Testing

**Limitations**: Our benchmark does not include video content evaluation.

## 💾 Data

**Source**: Curated from existing safety benchmarks and supplemented with synthetic data.

**Size**: 18,126 samples

**Format**: JSON

**Annotation**: Annotated for risk category, modality combinations, image style, and data source.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Attack Success Rate (ASR)
- Average Refusal Rate (ARR)

**Calculation**: ASR calculates the percentage of harmful queries that bypass safety safeguards, while ARR measures the refusal rate on harmless inputs.

**Interpretation**: Lower ASR and ARR scores indicate better alignment and safety.

**Baseline Results**: Varies across evaluated models; commercial MLLMs generally exhibit lower ASR compared to open-source counterparts.

**Validation**: Extensive experiments conducted using various mainstream open-source and commercial MLLMs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Safety
- Accuracy
- Bias

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
