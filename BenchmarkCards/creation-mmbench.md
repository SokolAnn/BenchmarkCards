# Creation-MMBench

## 📊 Benchmark Details

**Name**: Creation-MMBench

**Overview**: Creation-MMBench is a multimodal benchmark specifically designed to evaluate the creative capabilities of MLLMs in real-world, image-based tasks, consisting of 765 test cases across 51 detailed tasks with tailored evaluation criteria.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- MLLM-Bench
- AlignMMBench
- MMBench

**Resources**:
- [GitHub Repository](https://github.com/open-compass/Creation-MMBench)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive assessment of multimodal large language models' creative capabilities by evaluating model performance on various real-world creative tasks.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Creative Writing
- Visual Analysis
- Contextual Understanding

**Limitations**: N/A

## 💾 Data

**Source**: Constructed dataset including a diverse set of real-world scenarios with images and role-based tasks.

**Size**: 765 test cases

**Format**: N/A

**Annotation**: Manually curated tasks with specific roles and instructions to guide the generation of creative outputs.

## 🔬 Methodology

**Methods**:
- MLLM-as-a-Judge methodology
- Pairwise Comparison
- Unitary Scoring

**Metrics**:
- Visual Factuality Score
- Reward

**Calculation**: Metrics are calculated based on instance-level criteria comparing generated responses to reference content.

**Interpretation**: Higher scores indicate better performance in generating creative and contextually appropriate responses.

**Baseline Results**: N/A

**Validation**: Extensive evaluations conducted comparing various MLLMs on the same tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Robustness

**Atlas Risks**:
- **Fairness**: Decision bias
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
