# Assessing the Value of Visual Input: A Benchmark of Multimodal Large Language Models for Robotic Path Planning

## 📊 Benchmark Details

**Name**: Assessing the Value of Visual Input: A Benchmark of Multimodal Large Language Models for Robotic Path Planning

**Overview**: This paper assesses visual input’s utility for multimodal LLMs in robotic path planning via a comprehensive benchmark, evaluating 15 multimodal LLMs on generating valid and optimal paths in 2D grid environments.

**Data Type**: grid-based path generation scenarios

**Domains**:
- Robotics

**Languages**:
- English

**Similar Benchmarks**:
- PPNL
- EmbodiedBench

**Resources**:
- [Resource](https://arxiv.org/abs/2507.12391)

## 🎯 Purpose and Intended Users

**Goal**: To investigate the utility and current limitations of leveraging visual input alongside text for spatial planning tasks performed by contemporary multimodal LLMs.

**Target Audience**:
- ML Researchers
- Robotics Engineers

**Tasks**:
- Path Planning

**Limitations**: The performance significantly degrades on larger grids, highlighting a scalability challenge.

## 💾 Data

**Source**: Procedurally generated grid problems with varying sizes (e.g., 8x8, 20x20) and bomb densities.

**Size**: 20 pre-generated grid problems per grid size

**Format**: JSON

**Annotation**: Generated paths validated against ground truth with specified constraints.

## 🔬 Methodology

**Methods**:
- Quantitative benchmarking approach
- Comparative evaluation of multimodal LLMs

**Metrics**:
- Success Rate
- Optimality Rate
- Average Path Length Ratio
- Average Suboptimality Gap

**Calculation**: Metrics calculated based on the number of valid trials and optimal paths using pre-defined formulas.

**Interpretation**: High Success Rate indicates the effectiveness of the model in generating valid paths.

**Validation**: Results validated against ground truth for correctness and adherence to constraints.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**
- **Robustness**

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
