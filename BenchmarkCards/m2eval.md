# M2EVAL

## 📊 Benchmark Details

**Name**: M2EVAL

**Overview**: M2EVAL is a new benchmark for evaluating multilingual multimodal code generation. It addresses the need for incorporating visual aids such as diagrams and flowcharts in the code generation process, thus enhancing accuracy and architectural alignment.

**Data Type**: multimodal, code-related problems including textual and visual components

**Domains**:
- Computer Science

**Languages**:
- English

**Similar Benchmarks**:
- Design2Code
- MatPlotBench
- ChartCoder
- SWE-Bench

**Resources**:
- [GitHub Repository](https://github.com/MCEVAL/MMCoder)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the performance of large language models in generating code based on both textual instructions and visual design inputs.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Code Generation
- Visual Workflow Evaluation

**Limitations**: N/A

## 💾 Data

**Source**: Curated from a variety of programming tasks involving UML diagrams and flowcharts, along with textual inputs.

**Size**: 300 problems

**Format**: JSON, image files

**Annotation**: Problems were annotated by experts using domain knowledge to ensure correctness and coherence between visual and textual information.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Execution-based evaluations

**Metrics**:
- Pass@k (execution results)

**Calculation**: The metric calculates the ratio of generated code that successfully passes predefined test cases.

**Interpretation**: A higher Pass@k score indicates better performance in generating functional code from both text and visual inputs.

**Baseline Results**: M2-CODER 7B demonstrated competitive performance with larger models (70B+).

**Validation**: Model performance evaluated via execution of generated code against test cases.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Evasion attack
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: ['Models struggle with accurate visual information utilization and programming concepts adherence.']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
