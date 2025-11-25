# ArticulateRules

## 📊 Benchmark Details

**Name**: ArticulateRules

**Overview**: ArticulateRules is a dataset for evaluating how well language models can articulate rules which accurately describe their classification behavior when solving simple binary text classification tasks.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://openai.com/eval)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate how competent large language models are at providing high-level explanations of their own internal processes.

**Target Audience**:
- ML Researchers
- AI Practitioners
- Model Evaluators

**Tasks**:
- Text Classification
- Question Answering

**Limitations**: The benchmarks highlight limitations in LLMs' ability to articulate rules, particularly for GPT-3.

## 💾 Data

**Source**: Generated according to predefined rule functions with adversarial inputs included.

**Size**: 1500 examples (45 rule functions with multiple variations)

**Format**: JSONL

**Annotation**: Automatically generated based on defined rules.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Model outputs are compared to the expected results using predefined rules.

**Interpretation**: High accuracy indicates a model's ability to correctly articulate classification rules; low accuracy suggests a lack of understanding.

**Baseline Results**: GPT-3 scored below 10% articulation accuracy on most tasks, while GPT-4 achieved around 72% on select tasks.

**Validation**: Dataset validation performed by comparing model outputs against expected outcomes.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
