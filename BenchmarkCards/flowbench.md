# FlowBench

## 📊 Benchmark Details

**Name**: FlowBench

**Overview**: FlowBench is a comprehensive benchmark for evaluating workflow generation systems, including a variety of task types and node complexities, aimed at testing the capabilities of workflow generation models such as ComfyGPT.

**Data Type**: workflow-description pairs

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- ComfyGen
- ComfyBench

**Resources**:
- [GitHub Repository](https://github.com/comfygpt/comfygpt)

## 🎯 Purpose and Intended Users

**Goal**: To provide a robust evaluation framework for workflow generation methods in AI systems.

**Target Audience**:
- ML Researchers
- Workflow Generation Practitioners

**Tasks**:
- Workflow Generation

**Limitations**: N/A

## 💾 Data

**Source**: ComfyUI community websites through web crawling.

**Size**: 13,571 workflow-description pairs

**Format**: JSON

**Annotation**: Manual refinement and filtering

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Pass Accuracy (PA)
- Pass Instruct Alignment (PIA)
- Format Validation (FV)
- Pass Node Diversity (PND)

**Calculation**: Metrics are calculated by evaluating the performance of generated workflows against specified criteria, such as execution success and instruction alignment.

**Interpretation**: Higher scores indicate better performance in generating accurate and diverse workflows.

**Validation**: The model's performance is validated against predefined metrics established in the FlowBench dataset.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
