# Complex Bench

## 📊 Benchmark Details

**Name**: Complex Bench

**Overview**: Complex Bench is a benchmark for comprehensively evaluating the ability of large language models (LLMs) to follow complex instructions composed of multiple constraints. It provides a hierarchical taxonomy for complex instructions, including various types of constraints and composition types.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English
- Chinese

**Similar Benchmarks**:
- FollowBench
- CELLO
- WizardLM

**Resources**:
- [GitHub Repository](https://github.com/thu-coai/ComplexBench)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the ability of LLMs to follow complex instructions with multiple constraints effectively.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Complex Instruction Following
- Text Generation

**Limitations**: N/A

## 💾 Data

**Source**: Manually collected dataset based on a hierarchical taxonomy of complex instructions.

**Size**: 1,150 examples

**Format**: JSON

**Annotation**: Manual annotation by experts

## 🔬 Methodology

**Methods**:
- Rule-Augmented LLM-based Evaluation

**Metrics**:
- Accuracy
- Dependency-based Aggregation

**Calculation**: Aggregate scores based on dependency structure determined by different composition types.

**Interpretation**: Higher scores indicate better adherence to the constraints set by complex instructions.

**Validation**: Cross-validation by multiple annotators to ensure clarity and validity of constructed instructions.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: CC BY 4.0 for dataset, MIT for evaluation code.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
