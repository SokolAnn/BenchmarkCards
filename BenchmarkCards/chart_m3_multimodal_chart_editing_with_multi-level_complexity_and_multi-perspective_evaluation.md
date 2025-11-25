# Chart M3 (Multimodal Chart Editing with Multi-level Complexity and Multi-perspective Evaluation)

## 📊 Benchmark Details

**Name**: Chart M3 (Multimodal Chart Editing with Multi-level Complexity and Multi-perspective Evaluation)

**Overview**: Chart M3 is a new benchmark for multimodal chart editing, where user intent is expressed through a combination of natural language and visual indicators. It contains 1,000 samples spanning four levels of editing difficulty, each including triplets in the form of (chart, code, multimodal instructions).

**Data Type**: multimodal chart editing samples

**Domains**:
- Computer Vision
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/MLrollIT/ChartM3)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate multimodal large language models’ capabilities through chart editing tasks with natural language instructions and visual indicators.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Chart Editing

**Limitations**: N/A

## 💾 Data

**Source**: Curated datasets for visual indicator-guided and text-guided chart editing tasks.

**Size**: 1,000 samples

**Format**: N/A

**Annotation**: Automatically generated bounding box annotations and quality control via GPT-4 validation.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Delta Structural Similarity Index Measure (ΔSSIM)
- Directive Compliance Ratio

**Calculation**: Metrics assess the visual appearance and code correctness after chart modifications.

**Interpretation**: High ΔSSIM indicates visual fidelity, while the directive compliance ratio measures correct modifications.

**Validation**: Evaluated across multiple MLLMs, testing the models' visual comprehension and code generation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
