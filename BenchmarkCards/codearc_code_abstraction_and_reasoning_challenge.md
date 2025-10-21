# CodeARC (Code Abstraction and Reasoning Challenge)

## 📊 Benchmark Details

**Name**: CodeARC (Code Abstraction and Reasoning Challenge)

**Overview**: CodeARC provides a more realistic and challenging testbed for evaluating LLM-based inductive program synthesis through interactive input generation and self-correction. It features 1114 diverse functions in a general-purpose Python context to assess inductive reasoning capabilities.

**Data Type**: function synthesis tasks

**Domains**:
- Computer Science

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/Anjiang-Wei/CodeARC)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate reasoning capabilities of LLMs in the context of inductive program synthesis and to provide a challenging interactive evaluation protocol.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Inductive Program Synthesis

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from initial input-output examples and synthesized functions, curated from existing program synthesis tasks.

**Size**: 1114 functions

**Format**: N/A

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Interactive evaluation with function calls and oracle feedback

**Metrics**:
- Success rate

**Calculation**: Success rate is determined by the proportion of synthesized functions that pass correctness tests from the differential testing oracle within allocated budgets.

**Interpretation**: Higher success rates indicate better inductive reasoning capabilities and function synthesis performance.

**Baseline Results**: OpenAI o3-mini achieved a success rate of 52.7% in evaluations.

**Validation**: Evaluated through differential testing tools to ensure reliability of synthesized functions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Robustness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Robustness**: Evasion attack

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
