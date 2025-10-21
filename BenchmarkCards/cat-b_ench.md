# CAT-B ENCH

## 📊 Benchmark Details

**Name**: CAT-B ENCH

**Overview**: CAT-B ENCH is a benchmark of Step Order Prediction questions, designed to evaluate how well large language models (LLMs) understand causal and temporal dependencies in cooking recipe plans.

**Data Type**: question-answering pairs

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/vanyacohen/CaT-Bench)
- [GitHub Repository](https://github.com/StonyBrookNLP/CaT-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the causal and temporal reasoning abilities of large language models (LLMs) over instructional plans.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Step Order Prediction
- Step Order Explanation

**Limitations**: N/A

## 💾 Data

**Source**: Modified Recipe Flow Graph Corpus containing cooking recipes annotated with substep procedure dependencies.

**Size**: 4,260 questions

**Format**: N/A

**Annotation**: Manually annotated by the authors.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- Precision
- Recall

**Calculation**: Metrics calculated as per standard definitions in model evaluation.

**Interpretation**: Higher scores indicate better understanding of causal and temporal dependencies.

**Baseline Results**: Best zero-shot F1 of 0.59, with improvements using explanation-based generation yielding up to 0.73 F1.

**Validation**: Model performance validated through human evaluation and automated metrics.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Output bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
