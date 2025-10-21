# SensorBench

## 📊 Benchmark Details

**Name**: SensorBench

**Overview**: SensorBench is a comprehensive benchmark to systematically evaluate LLMs' capabilities in sensor data processing. It incorporates diverse real-world sensor datasets across various tasks and investigates LLM performance on simpler and complex tasks.

**Data Type**: temporal sensor signals

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/nesl/LLM_sensor_processing)

## 🎯 Purpose and Intended Users

**Goal**: To provide a structured reference for future research evaluating LLM performance in sensory data processing.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Signal Reconstruction
- Change Point Detection
- Outlier Detection
- Echo Cancellation
- Imputation
- Period Detection
- Resampling
- Spectrum Analysis
- Adaptive Filtering

**Limitations**: Focuses on single-channel temporal sensor signals; does not address multimodal sensor signals.

## 💾 Data

**Source**: Generated from MATLAB tutorials and established DSP textbooks.

**Size**: 250 sensor processing challenges

**Format**: N/A

**Annotation**: Tasks are designed from real-world applications validated against academic references.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Mean Squared Error (MSE)
- F1 Score
- Signal-to-Distortion Ratio (SDR)
- Win Rate
- Failure Rate

**Calculation**: Metrics are calculated by comparing LLM output against ground truth across different tasks.

**Interpretation**: Higher scores in F1 Score and SDR indicate better performance, while lower MSE indicates better accuracy.

**Baseline Results**: LLMs' performance is benchmarked against human experts in various sensor processing tasks.

**Validation**: Rigorous evaluation protocol with repeated experiments for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: Analysis includes expert performance across different tasks to identify bias in LLM capabilities.

**Potential Harm**: The benchmark aims to detect and improve sensor processing errors in LLM outputs.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
