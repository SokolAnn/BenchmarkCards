# Text2Vis

## 📊 Benchmark Details

**Name**: Text2Vis

**Overview**: Text2Vis is a benchmark designed to assess text-to-visualization models covering over 20 chart types and diverse data science queries. It features 1,985 samples, each with data tables, natural language queries, short answers, visualization code, and annotated charts.

**Data Type**: multimodal

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- VisEval
- WikiSQL
- nvBench
- ADVISor

**Resources**:
- [GitHub Repository](https://github.com/vis-nlp/Text2Vis)

## 🎯 Purpose and Intended Users

**Goal**: To provide a comprehensive benchmark for evaluating large language models in real-world text-to-visualization tasks.

**Target Audience**:
- ML Researchers
- Data Scientists
- Model Developers

**Tasks**:
- Data Visualization Generation
- Multimodal Reasoning

**Limitations**: Although Text2Vis provides a comprehensive benchmark for evaluating text-to-visualization generation models, it may not fully capture the range of complexities found in specialized domains.

## 💾 Data

**Source**: Curated from various sources including Statista, Pew Research, Our World In Data, and OECD, with synthetic tables generated using LLMs.

**Size**: 1,985 samples

**Format**: JSON

**Annotation**: Manually curated and annotated by experts in data science.

## 🔬 Methodology

**Methods**:
- Automated evaluation
- Model-based evaluation
- Manual evaluation

**Metrics**:
- Code Execution Success
- Answer Match
- Readability
- Chart Correctness

**Calculation**: The metrics are calculated based on predefined criteria, including matching generated answers to ground truth and visually evaluating generated charts.

**Interpretation**: A pass is considered when the code executes successfully, the answer matches the ground truth, and both readability and chart correctness scores are at least 3.5.

**Baseline Results**: Baseline model results vary; GPT-4o achieved a final pass rate of 26%, while improvements with the agentic framework increased this to 42%.

**Validation**: The benchmark was validated through automated evaluation across 11 models, with human evaluations conducted on a stratified sample of outputs.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Fairness**: Data bias
- **Robustness**: Extraction attack, Evasion attack

**Demographic Analysis**: Analysis includes a diverse set of 60 countries with varying demographic contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All datasets used in Text2Vis are publicly available and have been manually verified for accuracy.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
