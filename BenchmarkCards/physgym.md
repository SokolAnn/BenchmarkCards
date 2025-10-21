# PHYSGYM

## 📊 Benchmark Details

**Name**: PHYSGYM

**Overview**: PHYSGYM is a novel benchmark suite and simulation platform for evaluating interactive LLM-based scientific reasoning, designed for systematic control over task complexity and prior knowledge.

**Data Type**: interactive physics problems

**Domains**:
- Natural Language Processing
- Physics

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2507.15550)

## 🎯 Purpose and Intended Users

**Goal**: To assess the scientific discovery capabilities of large language model based agents in interactive physics environments.

**Target Audience**:
- ML Researchers
- Physics Educators
- AI Developers

**Tasks**:
- Hypothesis formation
- Experimental design
- Data analysis

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from 97 physics problems selected from PHYBench.

**Size**: 97 examples

**Format**: Structured JSON data

**Annotation**: Manually provided step-by-step reasoning processes verified by domain experts.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Symbolic evaluation
- LLM-based equivalence assessment

**Metrics**:
- Success Rate
- Coefficient of Determination (R2)
- Mean Squared Error (MSE)

**Calculation**: Calculated based on the performance of models through the match between proposed and ground-truth equations.

**Interpretation**: A higher success rate indicates better alignment of the model's hypotheses with the true physics underlying the scenarios.

**Baseline Results**: N/A

**Validation**: Measured through comparison of model performance across different settings of prior knowledge.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
