# OptimalThinkingBench

## 📊 Benchmark Details

**Name**: OptimalThinkingBench

**Overview**: OptimalThinkingBench is a unified benchmark that jointly evaluates overthinking and underthinking in LLMs, encouraging the development of models that balance performance and efficiency.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing
- Computer Science
- Mathematics
- Game Theory
- Reasoning

**Languages**:
- English

**Similar Benchmarks**:
- N/A

**Resources**:
- [GitHub Repository](https://github.com/facebookresearch/RAM/tree/main/projects/otb)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate and improve models in terms of their ability to think optimally without overthinking on simple tasks and underthinking on complex ones.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Understanding User Intent
- Complex Reasoning
- Task-Specific Optimizations

**Limitations**: N/A

## 💾 Data

**Source**: Generated using a synthetic recipe based on a wide array of domains and task types.

**Size**: 2,000 questions

**Format**: JSON

**Annotation**: Automatically validated using LLM-based verification methods.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- LLM-as-a-Judge verification

**Metrics**:
- Overthinking-Adjusted Accuracy (OAA)
- F1 Score

**Calculation**: Metrics calculated per defined thresholds of thinking tokens used, summarized through integrated metrics.

**Interpretation**: Higher scores indicate better performance with minimal overthinking across tasks.

**Baseline Results**: No model scored above 50% across evaluations.

**Validation**: Cross-validated against both sub-benchmarks and standard accuracy measures.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Poor model accuracy
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
