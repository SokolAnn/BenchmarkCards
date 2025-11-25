# ORQA (Operations Research Question Answering)

## 📊 Benchmark Details

**Name**: ORQA (Operations Research Question Answering)

**Overview**: This benchmark evaluates the generalization capabilities of Large Language Models (LLMs) in the specialized technical domain of Operations Research (OR) by assessing their ability to emulate the knowledge and reasoning skills of OR experts in addressing complex optimization problems.

**Data Type**: multi-choice question answering

**Domains**:
- Operations Research

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/nl4opt/ORQA)

## 🎯 Purpose and Intended Users

**Goal**: To assess the reasoning capabilities and generalization abilities of LLMs in the context of Operations Research through a benchmark dataset.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: The dataset contains real-world optimization problems crafted by Operations Research experts.

**Size**: 1,513 instances

**Format**: JSON

**Annotation**: Annotated by Operations Research experts with graduate-level education or extensive experience in optimization modeling.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- F1 Score

**Calculation**: Metrics are calculated by comparing LLM-generated answers with the correct answers.

**Interpretation**: Higher accuracy indicates better reasoning and understanding of the optimization models by the LLMs.

**Baseline Results**: Human expert accuracy was reported at 93% on a random set of instances.

**Validation**: The dataset includes a validation set of 45 instances used for in-context learning examples.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Privacy
- Robustness
- Fairness
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
