# REASON ZOO

## 📊 Benchmark Details

**Name**: REASON ZOO

**Overview**: REASON ZOO is a comprehensive benchmark encompassing nine diverse reasoning categories to evaluate the effectiveness of Tool-Integrated Reasoning (TIR) across various domains.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Resources**:
- [Resource](https://arxiv.org/abs/2508.15754)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate reasoning capabilities of LLMs through a diverse array of tasks and new efficiency metrics in reasoning.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Mathematical Reasoning
- Logical Reasoning
- Operations Research
- Combinatorial Puzzles

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from nine unique reasoning subcategories with specific tasks designed to evaluate various reasoning dimensions.

**Size**: 1,000 examples

**Format**: N/A

**Annotation**: Manually annotated and generated based on predefined problem sets.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics
- Model-based evaluation

**Metrics**:
- Performance-Aware Cost (PAC)
- Area Under the Performance-Cost Curve (AUC-PCC)

**Calculation**: PAC measures the computational cost required to achieve a specific performance threshold; AUC-PCC evaluates cumulative performance across varying computational budgets.

**Interpretation**: Higher PAC and AUC-PCC indicate more efficient reasoning with reduced operational overhead.

**Baseline Results**: N/A

**Validation**: Empirical evaluation of TIR-enabled models across diverse reasoning tasks.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Safety

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy
- **Robustness**: Prompt injection attack

**Demographic Analysis**: N/A

**Potential Harm**: ['Overthinking in LLMs', 'Redundant computations']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
