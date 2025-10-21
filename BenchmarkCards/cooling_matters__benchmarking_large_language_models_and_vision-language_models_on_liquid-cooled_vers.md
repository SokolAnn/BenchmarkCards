# Cooling Matters: Benchmarking Large Language Models and Vision-Language Models on Liquid-Cooled Versus Air-Cooled H100 GPU Systems

## 📊 Benchmark Details

**Name**: Cooling Matters: Benchmarking Large Language Models and Vision-Language Models on Liquid-Cooled Versus Air-Cooled H100 GPU Systems

**Overview**: This study benchmarks large language models (LLMs) and vision-language models (VLMs) on liquid-cooled and air-cooled H100 GPU systems, evaluating performance, thermal efficiency, and power consumption.

**Data Type**: performance metrics and thermal data

**Domains**:
- Computer Science
- High-Performance Computing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/iscaas/Cooling-Matters)

## 🎯 Purpose and Intended Users

**Goal**: To empirically compare liquid-cooled and air-cooled GPU systems for efficient power management and thermal performance in AI workloads.

**Target Audience**:
- Data Center Engineers
- AI Researchers
- HPC Practitioners

**Tasks**:
- Performance Benchmarking
- Energy Consumption Analysis

**Limitations**: N/A

## 💾 Data

**Source**: Performance and thermal metrics from benchmarking studies of LLMs and VLMs on H100 GPU systems.

**Size**: N/A

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Empirical benchmarking
- Synthetic stress testing
- Node-level power profiling

**Metrics**:
- TFLOPS per GPU
- Node power consumption
- GPU temperatures
- Utilization percentage

**Calculation**: Metrics were calculated based on real-time monitoring using various tools like ipmitool, GPU Burn, and Weights & Biases.

**Interpretation**: Higher TFLOPS per GPU and lower temperatures indicate better performance and efficiency under heavy workloads.

**Baseline Results**: Liquid-cooled systems achieved 54 TFLOPs/GPU compared to 46 TFLOPs/GPU for air-cooled systems during benchmarking.

**Validation**: Thermal and power measurements were compared across both cooling systems under identical workloads.

## ⚠️ Targeted Risks

**Risk Categories**:
- Efficiency
- Performance

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
