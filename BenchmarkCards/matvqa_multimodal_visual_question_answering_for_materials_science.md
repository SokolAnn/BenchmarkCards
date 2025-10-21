# MatVQA (Multimodal Visual Question Answering for Materials Science)

## 📊 Benchmark Details

**Name**: MatVQA (Multimodal Visual Question Answering for Materials Science)

**Overview**: MatVQA is a benchmark designed to evaluate research-level multimodal reasoning in materials science. It includes 1325 multiple-choice questions across four critical structure-property-performance reasoning tasks, leveraging visual and textual evidence.

**Data Type**: visual question-answering pairs

**Domains**:
- Natural Language Processing
- Materials Science

**Languages**:
- English

**Similar Benchmarks**:
- MaScQA
- SciQA
- MSE-MCQs
- MicroVQA

**Resources**:
- [Resource](https://anonymous.4open.science/r/matvqa-1E01/README.md)

## 🎯 Purpose and Intended Users

**Goal**: To provide a challenging and relevant evaluation standard for measuring MLLM capabilities in performing structured scientific reasoning and visual interpretation.

**Target Audience**:
- ML Researchers
- Materials Scientists
- Model Developers

**Tasks**:
- Causal SPP
- Comparative SPP
- Quantitative SPP
- Hypothetical Variation

**Limitations**: N/A

## 💾 Data

**Source**: Generated from recent materials literature using MArxivAgent, an automated pipeline that extracts reasoning paths from arXiv materials-science articles.

**Size**: 1,325 examples

**Format**: Multiple-choice questions

**Annotation**: Random 20% of questions vetted by domain experts to ensure accuracy.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Expert evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the proportion of correctly answered questions by models tested against the benchmark.

**Interpretation**: Higher accuracy indicates better performance in multimodal reasoning and visual question answering.

**Baseline Results**: N/A

**Validation**: 20% of the generated MCQs are randomly reviewed by domain experts for reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
