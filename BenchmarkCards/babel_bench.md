# BABEL BENCH

## 📊 Benchmark Details

**Name**: BABEL BENCH

**Overview**: BABEL BENCH is a benchmark framework that evaluates the proficiency of large language models (LLMs) in managing multimodal multistructured data with code execution, incorporating a dataset comprising 247 curated problems that challenge the models with tasks in perception, commonsense reasoning, logical reasoning, and more.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- SuperGLUE
- MMLU
- MME

**Resources**:
- [GitHub Repository](https://github.com/FFD8FFE/babelbench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate LLM capabilities in multimodal understanding, table interpretation, and code generation, while testing perceptual and reasoning skills.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Perception
- Commonsense Reasoning
- Logical Reasoning

**Limitations**: N/A

## 💾 Data

**Source**: Human-annotated questions based on textual questions, images and structured tables.

**Size**: 247 examples

**Format**: N/A

**Annotation**: Annotations performed by domain experts, with a quality review process for consistency.

## 🔬 Methodology

**Methods**:
- Automated evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the correctness of model responses compared to the ground-truth answers.

**Interpretation**: A score of 0 indicates no correct predictions, while higher scores indicate better performance.

**Baseline Results**: Baseline performance of models is reported in terms of accuracy across different questions.

**Validation**: N/A

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Robustness
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC-BY-4.0

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
