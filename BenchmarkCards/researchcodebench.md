# ResearchCodeBench

## 📊 Benchmark Details

**Name**: ResearchCodeBench

**Overview**: ResearchCodeBench is a benchmark of 212 coding challenges that evaluates LLMs’ ability to translate cutting-edge ML contributions from top 2024-2025 research papers into executable code.

**Data Type**: coding challenges

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- HumanEval
- MBPP
- LiveCodeBench
- BigCodeBench
- SUPER
- CORE-Bench
- SciCode
- MLE-Bench
- MLAgentBench
- MLGym
- PaperBench

**Resources**:
- [Resource](https://researchcodebench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate whether large language models (LLMs) can translate novel machine learning contributions from recent research papers into correct, executable code.

**Target Audience**:
- ML Researchers
- Domain Experts

**Tasks**:
- Code Generation
- Evaluation of LLMs on implementing novel ML research

**Limitations**: N/A

## 💾 Data

**Source**: 20 recently released ML papers from top venues (e.g., NeurIPS, ICLR, CVPR) and arXiv.

**Size**: 212 coding challenges

**Format**: N/A

**Annotation**: Manually annotated code snippets marked with XML-style tags to indicate regions of interest.

## 🔬 Methodology

**Methods**:
- Equivalence Tests
- Unit Tests

**Metrics**:
- Pass Rate
- Scaled Pass Rate

**Calculation**: Scaled Pass Rate is defined as the percentage of code snippets for which the model generates outputs that pass all correctness tests, weighted by the number of executable lines of code.

**Interpretation**: Higher pass rates indicate better performance in generating correct code.

**Baseline Results**: Gemini-2.5-Pro-Preview achieved the highest average performance with a 37.3% success rate.

**Validation**: Generated code is evaluated against provided correctness tests from the original paper authors or domain experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt leaking

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
