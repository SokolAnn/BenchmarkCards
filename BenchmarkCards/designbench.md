# DesignBench

## 📊 Benchmark Details

**Name**: DesignBench

**Overview**: DesignBench is a multi-framework, multi-task evaluation benchmark for assessing MLLMs' capabilities in automated front-end engineering, encompassing three widely-used UI frameworks (React, Vue, and Angular) and evaluating on three essential front-end tasks (generation, edit, and repair) in real-world development workflows.

**Data Type**: webpage samples

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- WebSight
- Web2Code
- WebCode2M
- Design2Code

**Resources**:
- [GitHub Repository](https://github.com/WebPAI/DesignBench)
- [Resource](https://webpai.github.io/DesignBench/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive evaluation framework for assessing multimodal large language models in the context of front-end code generation tasks.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Design Generation
- Design Edit
- Design Repair

**Limitations**: N/A

## 💾 Data

**Source**: Data is collected from GitHub projects and the top 500 globally visited websites, encompassing 900 webpage samples across various frameworks.

**Size**: 900 webpage samples

**Format**: N/A

**Annotation**: Annotated by experts and PhD students, ensuring quality and clarity in user instructions and UI modifications.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- MLLM Score
- Compilation Success Rate (CSR)
- Code Modification Similarity (CMS)

**Calculation**: Metrics are calculated based on the comparison of generated code against ground truth code and human evaluations.

**Interpretation**: Higher scores indicate better performance in generating correct and usable UI code.

**Baseline Results**: Evaluated using nine leading MLLMs across three fundamental tasks.

**Validation**: Validated through extensive testing and human evaluation to ensure metric reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Data poisoning, Hallucination

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
