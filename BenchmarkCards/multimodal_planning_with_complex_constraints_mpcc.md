# Multimodal Planning with Complex Constraints (MPCC)

## 📊 Benchmark Details

**Name**: Multimodal Planning with Complex Constraints (MPCC)

**Overview**: MPCC is designed to systematically evaluate the planning capabilities of multimodal large language models (MLLMs) under complex multimodal constraints, focusing on real-world tasks and varying difficulty levels.

**Data Type**: planning tasks

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- PlanBench
- ALFRED
- Behavior-1K

**Resources**:
- [GitHub Repository](https://github.com/j-yyyyy/MPCC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of MLLMs in multimodal planning tasks with complex constraints.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Multimodal Planning

**Limitations**: N/A

## 💾 Data

**Source**: Real-world scenarios generated using a code generator and filtered for constraint specifications.

**Size**: 2,700 planning tasks

**Format**: N/A

**Annotation**: Manually filtered to ensure accurate constraints and diversity.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Feasible Plan Rate
- Optimal Plan Rate

**Calculation**: Feasible plans are determined by meeting budget ceilings, temporal coordination requirements, and spatial proximity limits.

**Interpretation**: Higher rates of feasible and optimal plans indicate better performance under complex constraints.

**Baseline Results**: N/A

**Validation**: Dataset validated through two-stage human checks involving experts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Robustness
- Accuracy

**Atlas Risks**:
- **Fairness**
- **Robustness**
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
